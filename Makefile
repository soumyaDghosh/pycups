PROJECT=cups
UV_LINT_GROUPS := "--group=lint"
SOURCES=$(wildcard *.py) $(PROJECT)

ifneq ($(OS),Windows_NT)
	OS := $(shell uname)
endif
ifdef CI
	APT := apt-get --yes
else
	APT := apt-get
endif

.DEFAULT_GOAL := help

.ONESHELL:

.SHELLFLAGS = -ec

.PHONY: help
help: ## Show this help.
	@printf "\e[1m%-30s\e[0m | \e[1m%s\e[0m\n" "Target" "Description"
	printf "\e[2m%-30s + %-41s\e[0m\n" "------------------------------" "------------------------------------------------"
	egrep --with-filename '^[^:]+\: [^#]*##' $$(echo $(MAKEFILE_LIST) | tac --separator=' ') | sed -e 's/^[^:]*://' -e 's/:[^#]*/ /' | sort -V| awk -F '[: ]*' \
	'{
		if ($$2 == "##")
		{
			$$1=sprintf(" %-28s", $$1);
			$$2=" | ";
			print $$0;
		}
		else
		{
			$$1=sprintf("  └ %-25s", $$1);
			$$2=" | ";
			$$3=sprintf(" └ %s", $$3);
			print $$0;
		}
	}' | uniq

.PHONY: setup
setup: install-uv  _setup-lint setup-precommit  ## Set up a development environment
	uv sync --group=lint

.PHONY: setup-lint
setup-lint: _setup-lint  ##- Set up a linting-only environment
	uv sync --group=lint

.PHONY: _setup-lint
_setup-lint: install-uv install-pyright

.PHONY: setup-precommit
setup-precommit: install-uv  ##- Set up pre-commit hooks in this repository.
ifeq ($(shell which pre-commit),)
	uv tool run pre-commit install
else
	pre-commit install
endif

.PHONY: clean
clean:  ## Clean up the development environment
	uv tool run pyclean .
	rm -rf build/

.PHONY: format-ruff
format-ruff: install-ruff  ##- Automatically format with ruff
	success=true
	ruff check --fix $(SOURCES) || success=false
	ruff format $(SOURCES)
	$$success || exit 1

.PHONY: format-codespell
format-codespell:  ##- Fix spelling issues with codespell
	uv run codespell --toml pyproject.toml --write-changes $(SOURCES)

.PHONY: format-pre-commit
format-pre-commit:  ##- Format the entire repository using pre-commit
	uv tool run pre-commit run

.PHONY: lint-ruff
lint-ruff: install-ruff  ##- Lint with ruff
ifneq ($(CI),)
	@echo ::group::$@
endif
	ruff check $(SOURCES)
	ruff format --diff $(SOURCES)
ifneq ($(CI),)
	@echo ::endgroup::
endif

.PHONY: lint-codespell
lint-codespell: install-codespell  ##- Check spelling with codespell
ifneq ($(CI),)
	@echo ::group::$@
endif
	uv run codespell --toml pyproject.toml $(SOURCES)
ifneq ($(CI),)
	@echo ::endgroup::
endif

.PHONY: lint-mypy
lint-mypy:  ##- Check types with mypy
ifneq ($(CI),)
	@echo ::group::$@
endif
	uv run mypy --show-traceback --show-error-codes $(PROJECT)
ifneq ($(CI),)
	@echo ::endgroup::
endif

.PHONY: lint-pyright
lint-pyright:  ##- Check types with pyright
ifneq ($(CI),)
	@echo ::group::$@
endif
ifneq ($(shell which pyright),) # Prefer the system pyright
	pyright --pythonpath .venv/bin/python
else
	uv tool run pyright --pythonpath .venv/bin/python
endif
ifneq ($(CI),)
	@echo ::endgroup::
endif

# Below are intermediate targets for setup. They are not included in help as they should
# not be used independently.

.PHONY: install-uv
install-uv:
ifneq ($(shell which uv),)
else ifneq ($(shell which snap),)
	sudo snap install --classic astral-uv
else ifneq ($(shell which brew),)
	brew install uv
else ifeq ($(OS),Windows_NT)
	pwsh -c "irm https://astral.sh/uv/install.ps1 | iex"
else
	curl -LsSf https://astral.sh/uv/install.sh | sh
endif

.PHONY: install-codespell
install-codespell:
ifneq ($(shell which codespell),)
else ifneq ($(shell which snap),)
	sudo snap install codespell
else ifneq ($(shell which brew),)
	make install-uv
	uv tool install codespell
else
	$(warning Codespell not installed. Please install it yourself.)
endif

.PHONY: install-pyright
install-pyright: install-uv
ifneq ($(shell which pyright),)
else ifneq ($(shell which snap),)
	sudo snap install --classic pyright
else
	# Workaround for a bug in npm
	[ -d "$(HOME)/.npm/_cacache" ] && chown -R `id -u`:`id -g` "$(HOME)/.npm" || true
	uv tool install pyright
endif

.PHONY: install-ruff
install-ruff:
ifneq ($(shell which ruff),)
else ifneq ($(shell which snap),)
	sudo snap install ruff
else
	make install-uv
	uv tool install ruff
endif

.PHONY: install-npm
install-npm:
ifneq ($(shell which npm),)
else ifneq ($(shell which snap),)
	sudo snap install --classic node
else ifneq ($(shell which brew),)
	brew install node
else
	$(error npm not installed. Please install it yourself.)
endif

.PHONY: format
format: format-ruff format-codespell format-pre-commit  ## Run all automatic formatters

.PHONY: lint
lint: lint-ruff lint-codespell lint-mypy lint-prettier lint-pyright  ## Run all linters
