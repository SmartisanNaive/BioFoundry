from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from biofoundry_cli.tools.sanger import (
    SangerAlign,
    align_sanger,
    evaluate_expected_mutations,
    parse_sequence_text,
    read_sequence_input,
    reverse_complement,
)


def test_parse_plain_seq_style_file(tmp_path: Path) -> None:
    seq_file = tmp_path / "clone.seq"
    seq_file.write_text("ACGTNNRYSWKMBDHV\n", encoding="utf-8")

    sequence = read_sequence_input(str(seq_file))

    assert sequence.name == "clone.seq"
    assert sequence.sequence == "ACGTNNRYSWKMBDHV"


def test_parse_user_provided_s4_seq_if_available() -> None:
    seq_file = Path("/Volumes/Data 1/Project/Biofoundry Agent/docs/data/s4-1-T7.seq")
    if not seq_file.exists():
        pytest.skip("User-provided Sanger .seq sample is not available in this environment.")

    sequence = read_sequence_input(str(seq_file))

    assert sequence.name == "s4-1-T7.seq"
    assert len(sequence.sequence) == 882
    assert set(sequence.sequence) <= set("ACGTN")


def test_parse_fasta_and_multiline_plain_text() -> None:
    fasta = ">clone read\nACGT\nACGT\n"
    plain = "ACGT\nACGT\n"

    assert parse_sequence_text(fasta) == "ACGTACGT"
    assert parse_sequence_text(plain) == "ACGTACGT"


def test_reverse_complement_orientation_is_selected() -> None:
    reference = "AAACCGTGGTTT"
    query = reverse_complement("CCGTGG")

    result = align_sanger(reference, query)

    assert result.orientation == "reverse-complement"
    assert result.reference_start == 3
    assert result.reference_end == 9
    assert result.identity == 1.0


def test_reports_mismatch_insertion_and_deletion() -> None:
    reference = "AAAACCCCGGGG"

    mismatch = align_sanger(reference, "AAAATCCCGGGG")
    insertion = align_sanger(reference, "AAAATCCCCGGGG")
    deletion = align_sanger("ACGTACGT", "ACGACGT")

    assert any(
        diff.kind == "mismatch"
        and diff.position == 5
        and diff.reference == "C"
        and diff.query == "T"
        for diff in mismatch.differences
    )
    assert any(
        diff.kind == "insertion" and diff.position == 4 and diff.query == "T"
        for diff in insertion.differences
    )
    assert any(
        diff.kind == "deletion" and diff.position == 4 and diff.reference == "T"
        for diff in deletion.differences
    )


def test_expected_mutation_statuses() -> None:
    reference = "AAAACCCCGGGG"
    alignment = align_sanger(reference, "AAAATCCCGGGG")

    results = evaluate_expected_mutations(
        alignment,
        ["C5T", "A5T", "ins4:T", "not-a-mutation"],
        reference,
    )
    statuses = {result.mutation: result.status for result in results}

    assert statuses["C5T"] == "matched"
    assert statuses["A5T"] == "reference_mismatch"
    assert statuses["ins4:T"] == "missing"
    assert statuses["not-a-mutation"] == "invalid"


@pytest.mark.asyncio
async def test_sanger_align_tool_renders_clone_validation_report(tmp_path: Path) -> None:
    reference = tmp_path / "ref.fa"
    query = tmp_path / "clone.seq"
    reference.write_text(">ref\nAAAACCCCGGGG\n", encoding="utf-8")
    query.write_text("AAAATCCCCGGGG", encoding="utf-8")

    result = await SangerAlign()(
        SangerAlign.params(
            reference=str(reference),
            query=str(query),
            expected_mutations=["ins4:T"],
        )
    )

    assert not result.is_error
    assert "Identity:" in result.output
    assert "ins4:T: matched" in result.output
    assert "| insertion | 4 | - | T |" in result.output


def test_default_agents_register_sanger_align_tool() -> None:
    root = Path(__file__).resolve().parent.parent
    default = yaml.safe_load((root / "src/biofoundry_cli/agents/default/agent.yaml").read_text())
    okabe = yaml.safe_load((root / "src/biofoundry_cli/agents/okabe/agent.yaml").read_text())

    assert "biofoundry_cli.tools.sanger:SangerAlign" in default["agent"]["tools"]
    assert "biofoundry_cli.tools.sanger:SangerAlign" in okabe["agent"]["tools"]
