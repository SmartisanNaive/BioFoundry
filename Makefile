.DEFAULT_GOAL := prepare

.PHONY: help
help: ## Show available make targets.
	@echo "Available make targets:"
	@awk 'BEGIN { FS = ":.*## " } /^[A-Za-z0-9_.-]+:.*## / { printf "  %-20s %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

.PHONY: install-prek
install-prek: ## Install prek and repo git hooks.
	@echo "==> Installing prek"
	@uv tool install prek
	@if git rev-parse --git-common-dir >/dev/null 2>&1; then \
		echo "==> Installing git hooks with prek"; \
		uv tool run prek install; \
	else \
		echo "==> Skipping git hook install (not a git repository)"; \
	fi

.PHONY: prepare
prepare: install-prek ## Sync dependencies for all workspace packages and install prek hooks.
	@echo "==> Syncing dependencies for all workspace packages"
	@uv sync --frozen --all-extras --all-packages

.PHONY: prepare-build
prepare-build: ## Sync dependencies for releases without workspace sources.
	@echo "==> Syncing dependencies for release builds (no sources)"
	@uv sync --all-extras --all-packages --no-sources

.PHONY: format format-biofoundry-cli format-biofoundry-llm format-biofoundry-os
format: format-biofoundry-cli format-biofoundry-llm format-biofoundry-os ## Auto-format all workspace packages.
format-biofoundry-cli: ## Auto-format Biofoundry_CLI sources with ruff.
	@echo "==> Formatting Biofoundry_CLI sources"
	@uv run ruff check --fix
	@uv run ruff format
format-biofoundry-llm: ## Auto-format biofoundry_llm sources with ruff.
	@echo "==> Formatting biofoundry_llm sources"
	@uv run --project packages/biofoundry_llm --directory packages/biofoundry_llm ruff check --fix
	@uv run --project packages/biofoundry_llm --directory packages/biofoundry_llm ruff format
format-biofoundry-os: ## Auto-format biofoundry_os sources with ruff.
	@echo "==> Formatting biofoundry_os sources"
	@uv run --project packages/biofoundry_os --directory packages/biofoundry_os ruff check --fix
	@uv run --project packages/biofoundry_os --directory packages/biofoundry_os ruff format
.PHONY: check check-biofoundry-cli check-biofoundry-llm check-biofoundry-os
check: check-biofoundry-cli check-biofoundry-llm check-biofoundry-os ## Run linting and type checks for all packages.
check-biofoundry-cli: ## Run linting and type checks for Biofoundry_CLI.
	@echo "==> Checking Biofoundry_CLI (ruff + pyright + ty; ty is non-blocking)"
	@uv run ruff check
	@uv run ruff format --check
	@uv run pyright
	@uv run ty check || true
check-biofoundry-llm: ## Run linting and type checks for biofoundry_llm.
	@echo "==> Checking biofoundry_llm (ruff + pyright + ty; ty is non-blocking)"
	@uv run --project packages/biofoundry_llm --directory packages/biofoundry_llm ruff check
	@uv run --project packages/biofoundry_llm --directory packages/biofoundry_llm ruff format --check
	@uv run --project packages/biofoundry_llm --directory packages/biofoundry_llm pyright
	@uv run --project packages/biofoundry_llm --directory packages/biofoundry_llm ty check || true
check-biofoundry-os: ## Run linting and type checks for biofoundry_os.
	@echo "==> Checking biofoundry_os (ruff + pyright + ty; ty is non-blocking)"
	@uv run --project packages/biofoundry_os --directory packages/biofoundry_os ruff check
	@uv run --project packages/biofoundry_os --directory packages/biofoundry_os ruff format --check
	@uv run --project packages/biofoundry_os --directory packages/biofoundry_os pyright
	@uv run --project packages/biofoundry_os --directory packages/biofoundry_os ty check || true
.PHONY: build build-biofoundry-cli build-biofoundry-llm build-biofoundry-os build-bin build-bin-onedir
build: build-biofoundry-cli build-biofoundry-llm build-biofoundry-os ## Build Python packages for release.
build-biofoundry-cli: ## Build the biofoundry-cli distributions.
	@echo "==> Building biofoundry-cli distributions"
	@uv build --package biofoundry-cli --no-sources --out-dir dist
build-biofoundry-llm: ## Build the biofoundry_llm sdist and wheel.
	@echo "==> Building biofoundry_llm distributions"
	@uv build --package biofoundry_llm --no-sources --out-dir dist/biofoundry_llm
build-biofoundry-os: ## Build the biofoundry_os sdist and wheel.
	@echo "==> Building biofoundry_os distributions"
	@uv build --package biofoundry_os --no-sources --out-dir dist/biofoundry_os
build-bin: ## Build the standalone executable with PyInstaller (one-file mode).
	@echo "==> Building PyInstaller binary (one-file)"
	@uv run pyinstaller biofoundry.spec
	@mkdir -p dist/onefile
	@if [ -f dist/biofoundry.exe ]; then mv dist/biofoundry.exe dist/onefile/; elif [ -f dist/biofoundry ]; then mv dist/biofoundry dist/onefile/; fi
build-bin-onedir: ## Build the standalone executable with PyInstaller (one-dir mode).
	@echo "==> Building PyInstaller binary (one-dir)"
	@rm -rf dist/onedir dist/biofoundry
	@uv run pyinstaller biofoundry.spec
	@if [ -f dist/biofoundry/biofoundry-exe.exe ]; then mv dist/biofoundry/biofoundry-exe.exe dist/biofoundry/biofoundry.exe; elif [ -f dist/biofoundry/biofoundry-exe ]; then mv dist/biofoundry/biofoundry-exe dist/biofoundry/biofoundry; fi
	@mkdir -p dist/onedir && mv dist/biofoundry dist/onedir/

.PHONY: gen-changelog
gen-changelog: ## Generate changelog with Biofoundry_CLI.
	@echo "==> Generating changelog"
	@uv run biofoundry --yolo --prompt /skill:gen-changelog

include src/biofoundry_cli/deps/Makefile
