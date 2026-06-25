from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Literal, override

from biofoundry_llm.tooling import CallableTool2, ToolError, ToolOk, ToolReturnValue
from pydantic import BaseModel, Field

from biofoundry_cli.tools.utils import load_desc

DNA_ALPHABET = frozenset("ACGTRYSWKMBDHVN")
COMPLEMENT = str.maketrans(
    "ACGTRYSWKMBDHVNacgtryswkmbdhvn",
    "TGCAYRSWMKVHDBNtgcayrswmkvhdbn",
)


@dataclass(frozen=True, slots=True)
class SequenceInput:
    name: str
    sequence: str
    source: str


@dataclass(frozen=True, slots=True)
class Difference:
    kind: Literal["mismatch", "insertion", "deletion"]
    position: int
    reference: str
    query: str


@dataclass(frozen=True, slots=True)
class ExpectedMutationResult:
    mutation: str
    status: Literal["matched", "missing", "invalid", "out_of_range", "reference_mismatch"]
    detail: str


@dataclass(frozen=True, slots=True)
class AlignmentResult:
    score: int
    orientation: Literal["forward", "reverse-complement"]
    reference_start: int
    reference_end: int
    query_start: int
    query_end: int
    aligned_reference: str
    aligned_query: str
    matches: int
    mismatches: int
    insertions: int
    deletions: int
    differences: tuple[Difference, ...]

    @property
    def aligned_columns(self) -> int:
        return len(self.aligned_reference)

    @property
    def compared_bases(self) -> int:
        return self.matches + self.mismatches

    @property
    def identity(self) -> float:
        denominator = self.matches + self.mismatches + self.insertions + self.deletions
        return self.matches / denominator if denominator else 0.0


class Params(BaseModel):
    reference: str = Field(
        description="Reference DNA sequence or path to a reference sequence file."
    )
    query: str = Field(description="Sanger sequence text or path to a .seq/.txt/.fa/.fasta file.")
    reference_name: str | None = Field(default=None, description="Optional reference display name.")
    query_name: str | None = Field(default=None, description="Optional query display name.")
    expected_mutations: list[str] = Field(
        default_factory=list,
        description=(
            "Optional expected mutations to check, e.g. A123G, del45, del45:AC, ins78:T."
        ),
    )
    max_differences: int = Field(
        default=100,
        ge=1,
        le=1000,
        description="Maximum number of differences to include in the text report.",
    )


class SangerAlign(CallableTool2[Params]):
    name: str = "SangerAlign"
    params: type[Params] = Params

    def __init__(self) -> None:
        super().__init__(description=load_desc(Path(__file__).parent / "description.md"))

    @override
    async def __call__(self, params: Params) -> ToolReturnValue:
        try:
            reference = read_sequence_input(params.reference, name=params.reference_name)
            query = read_sequence_input(params.query, name=params.query_name)
            alignment = align_sanger(reference.sequence, query.sequence)
            expected = evaluate_expected_mutations(
                alignment,
                params.expected_mutations,
                reference.sequence,
            )
            report = render_report(reference, query, alignment, expected, params.max_differences)
        except ValueError as exc:
            return ToolError(message=str(exc), brief="Sanger alignment failed")
        except OSError as exc:
            return ToolError(message=f"Failed to read sequence input: {exc}", brief="Read failed")

        return ToolOk(
            output=report,
            message=(
                f"Sanger alignment completed: {alignment.identity:.2%} identity, "
                f"{len(alignment.differences)} differences."
            ),
        )


def read_sequence_input(value: str, *, name: str | None = None) -> SequenceInput:
    text = value.strip()
    if not text:
        raise ValueError("Sequence input cannot be empty.")

    source = "inline"
    maybe_path = Path(text).expanduser()
    if _looks_like_path(text):
        if not maybe_path.exists():
            raise ValueError(f"Sequence file does not exist: {text}")
        if not maybe_path.is_file():
            raise ValueError(f"Sequence path is not a file: {text}")
        raw = maybe_path.read_text(encoding="utf-8", errors="replace")
        source = str(maybe_path)
        display_name = name or maybe_path.name
    else:
        raw = text
        display_name = name or "inline sequence"

    sequence = parse_sequence_text(raw)
    if not sequence:
        raise ValueError(f"No DNA sequence found in {source}.")
    return SequenceInput(name=display_name, sequence=sequence, source=source)


def parse_sequence_text(text: str) -> str:
    lines: list[str] = []
    for line in text.splitlines() or [text]:
        stripped = line.strip()
        if not stripped or stripped.startswith(">"):
            continue
        lines.append(stripped)
    sequence = re.sub(r"[^A-Za-z]", "", "".join(lines)).upper()
    invalid = sorted(set(sequence) - DNA_ALPHABET)
    if invalid:
        raise ValueError(f"Unsupported sequence characters: {', '.join(invalid)}")
    return sequence


def reverse_complement(sequence: str) -> str:
    return sequence.translate(COMPLEMENT)[::-1].upper()


def align_sanger(reference: str, query: str) -> AlignmentResult:
    forward = _smith_waterman(reference, query, orientation="forward")
    reverse = _smith_waterman(
        reference,
        reverse_complement(query),
        orientation="reverse-complement",
    )
    if reverse.score > forward.score:
        return reverse
    return forward


def evaluate_expected_mutations(
    alignment: AlignmentResult,
    expected_mutations: list[str],
    reference: str,
) -> tuple[ExpectedMutationResult, ...]:
    if not expected_mutations:
        return ()

    ref_to_query = _aligned_reference_map(alignment)
    differences = {
        (diff.kind, diff.position, diff.reference, diff.query)
        for diff in alignment.differences
    }
    results: list[ExpectedMutationResult] = []

    for mutation in expected_mutations:
        token = mutation.strip()
        snp = re.fullmatch(r"([ACGTRYSWKMBDHVN])(\d+)([ACGTRYSWKMBDHVN])", token, re.I)
        deletion = re.fullmatch(r"del(\d+)(?::([ACGTRYSWKMBDHVN]+))?", token, re.I)
        insertion = re.fullmatch(r"ins(\d+):([ACGTRYSWKMBDHVN]+)", token, re.I)

        if snp:
            ref_base, pos_text, query_base = snp.groups()
            pos = int(pos_text)
            if pos < 1 or pos > len(reference):
                results.append(
                    _expected(token, "out_of_range", f"position {pos} is outside reference")
                )
                continue
            if reference[pos - 1] != ref_base.upper():
                detail = f"reference has {reference[pos - 1]} at {pos}, not {ref_base.upper()}"
                results.append(_expected(token, "reference_mismatch", detail))
                continue
            observed = ref_to_query.get(pos)
            status = "matched" if observed == query_base.upper() else "missing"
            detail = f"observed {observed or 'uncovered'} at reference position {pos}"
            results.append(_expected(token, status, detail))
            continue

        if deletion:
            pos_text, deleted = deletion.groups()
            pos = int(pos_text)
            if deleted:
                deleted = deleted.upper()
                matched = ("deletion", pos, deleted, "-") in differences
            else:
                matched = any(
                    diff.kind == "deletion" and diff.position == pos
                    for diff in alignment.differences
                )
            observed = "observed" if matched else "not observed"
            detail = f"deletion at reference position {pos} {observed}"
            results.append(_expected(token, "matched" if matched else "missing", detail))
            continue

        if insertion:
            pos_text, inserted = insertion.groups()
            pos = int(pos_text)
            inserted = inserted.upper()
            matched = ("insertion", pos, "-", inserted) in differences
            observed = "observed" if matched else "not observed"
            detail = f"insertion after reference position {pos} {observed}"
            results.append(_expected(token, "matched" if matched else "missing", detail))
            continue

        results.append(
            _expected(
                token,
                "invalid",
                "expected A123G, del45, del45:AC, or ins78:T format",
            )
        )

    return tuple(results)


def render_report(
    reference: SequenceInput,
    query: SequenceInput,
    alignment: AlignmentResult,
    expected: tuple[ExpectedMutationResult, ...],
    max_differences: int,
) -> str:
    ref_coverage = (alignment.reference_end - alignment.reference_start) / len(reference.sequence)
    query_coverage = (alignment.query_end - alignment.query_start) / len(query.sequence)
    query_n = query.sequence.count("N") / len(query.sequence)
    truncated = len(alignment.differences) > max_differences

    lines = [
        "# Sanger alignment report",
        "",
        "## Summary",
        f"- Reference: {reference.name} ({len(reference.sequence)} bp)",
        f"- Query: {query.name} ({len(query.sequence)} bp)",
        f"- Orientation: {alignment.orientation}",
        f"- Score: {alignment.score}",
        f"- Identity: {alignment.identity:.2%}",
        (
            f"- Reference coverage: {ref_coverage:.2%} "
            f"({alignment.reference_start + 1}-{alignment.reference_end})"
        ),
        (
            f"- Query coverage: {query_coverage:.2%} "
            f"({alignment.query_start + 1}-{alignment.query_end})"
        ),
        f"- Query N ratio: {query_n:.2%}",
        f"- Differences: {len(alignment.differences)} "
        f"({alignment.mismatches} mismatches, {alignment.insertions} inserted bases, "
        f"{alignment.deletions} deleted bases)",
    ]

    if expected:
        lines.extend(["", "## Expected mutations"])
        for item in expected:
            lines.append(f"- {item.mutation}: {item.status} ({item.detail})")

    lines.extend(["", "## Differences"])
    if not alignment.differences:
        lines.append("- No differences in the aligned region.")
    else:
        lines.append("| Type | Reference position | Reference | Query |")
        lines.append("| --- | ---: | --- | --- |")
        for diff in alignment.differences[:max_differences]:
            lines.append(f"| {diff.kind} | {diff.position} | {diff.reference} | {diff.query} |")
        if truncated:
            remaining = len(alignment.differences) - max_differences
            lines.append(f"| ... | ... | {remaining} more | ... |")

    return "\n".join(lines) + "\n"


def _smith_waterman(
    reference: str,
    query: str,
    *,
    orientation: Literal["forward", "reverse-complement"],
) -> AlignmentResult:
    if not reference or not query:
        raise ValueError("Reference and query sequences must both be non-empty.")

    match_score = 2
    mismatch_score = -1
    gap_score = -2
    rows = len(reference) + 1
    cols = len(query) + 1
    scores = [[0] * cols for _ in range(rows)]
    pointers = [[0] * cols for _ in range(rows)]
    best_score = 0
    best_i = 0
    best_j = 0

    for i, ref_base in enumerate(reference, start=1):
        for j, query_base in enumerate(query, start=1):
            diag = scores[i - 1][j - 1] + (
                match_score if ref_base == query_base else mismatch_score
            )
            up = scores[i - 1][j] + gap_score
            left = scores[i][j - 1] + gap_score
            score = max(0, diag, up, left)
            scores[i][j] = score
            if score == 0:
                pointer = 0
            elif score == diag:
                pointer = 1
            elif score == up:
                pointer = 2
            else:
                pointer = 3
            pointers[i][j] = pointer
            if score > best_score:
                best_score = score
                best_i = i
                best_j = j

    if best_score == 0:
        raise ValueError("No local alignment found between reference and query.")

    aligned_ref: list[str] = []
    aligned_query: list[str] = []
    i = best_i
    j = best_j
    while i > 0 and j > 0 and pointers[i][j] != 0:
        pointer = pointers[i][j]
        if pointer == 1:
            aligned_ref.append(reference[i - 1])
            aligned_query.append(query[j - 1])
            i -= 1
            j -= 1
        elif pointer == 2:
            aligned_ref.append(reference[i - 1])
            aligned_query.append("-")
            i -= 1
        else:
            aligned_ref.append("-")
            aligned_query.append(query[j - 1])
            j -= 1

    ref_aligned = "".join(reversed(aligned_ref))
    query_aligned = "".join(reversed(aligned_query))
    differences, matches, mismatches, insertions, deletions = _collect_differences(
        ref_aligned,
        query_aligned,
        reference_start=i,
    )
    return AlignmentResult(
        score=best_score,
        orientation=orientation,
        reference_start=i,
        reference_end=best_i,
        query_start=j,
        query_end=best_j,
        aligned_reference=ref_aligned,
        aligned_query=query_aligned,
        matches=matches,
        mismatches=mismatches,
        insertions=insertions,
        deletions=deletions,
        differences=tuple(differences),
    )


def _collect_differences(
    aligned_reference: str,
    aligned_query: str,
    *,
    reference_start: int,
) -> tuple[list[Difference], int, int, int, int]:
    differences: list[Difference] = []
    matches = 0
    mismatches = 0
    insertions = 0
    deletions = 0
    ref_pos = reference_start
    idx = 0

    while idx < len(aligned_reference):
        ref_base = aligned_reference[idx]
        query_base = aligned_query[idx]
        if ref_base != "-" and query_base != "-":
            ref_pos += 1
            if ref_base == query_base:
                matches += 1
            else:
                mismatches += 1
                differences.append(Difference("mismatch", ref_pos, ref_base, query_base))
            idx += 1
            continue

        if ref_base == "-":
            inserted: list[str] = []
            position = ref_pos
            while idx < len(aligned_reference) and aligned_reference[idx] == "-":
                inserted.append(aligned_query[idx])
                idx += 1
            insertion_text = "".join(inserted)
            insertions += len(insertion_text)
            differences.append(Difference("insertion", position, "-", insertion_text))
            continue

        deleted: list[str] = []
        position = ref_pos + 1
        while idx < len(aligned_reference) and aligned_query[idx] == "-":
            deleted.append(aligned_reference[idx])
            ref_pos += 1
            idx += 1
        deletion_text = "".join(deleted)
        deletions += len(deletion_text)
        differences.append(Difference("deletion", position, deletion_text, "-"))

    return differences, matches, mismatches, insertions, deletions


def _aligned_reference_map(alignment: AlignmentResult) -> dict[int, str]:
    ref_pos = alignment.reference_start
    mapping: dict[int, str] = {}
    for ref_base, query_base in zip(
        alignment.aligned_reference,
        alignment.aligned_query,
        strict=True,
    ):
        if ref_base == "-":
            continue
        ref_pos += 1
        if query_base != "-":
            mapping[ref_pos] = query_base
    return mapping


def _expected(
    mutation: str,
    status: Literal["matched", "missing", "invalid", "out_of_range", "reference_mismatch"],
    detail: str,
) -> ExpectedMutationResult:
    return ExpectedMutationResult(mutation=mutation, status=status, detail=detail)


def _looks_like_path(value: str) -> bool:
    if "\n" in value or "\r" in value:
        return False
    path = Path(value).expanduser()
    if path.exists():
        return True
    suffix = path.suffix.lower()
    return suffix in {".seq", ".txt", ".fa", ".fasta", ".fna"}
