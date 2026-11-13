PYTHON ?= python3
VENV := .venv
VENV_PYTHON := $(VENV)/bin/python
VENV_PIP := $(VENV_PYTHON) -m pip

.PHONY: setup run test build clean

setup:
	$(PYTHON) -m venv $(VENV)
	$(VENV_PIP) install -e '.[dev]'

run:
	$(VENV_PYTHON) -m preview

test:
	QT_QPA_PLATFORM=offscreen $(VENV_PYTHON) -m pytest

build:
	$(VENV_PYTHON) -m build

clean:
	rm -rf build dist .pytest_cache .coverage
	find preview tests -type d -name __pycache__ -prune -exec rm -rf {} +
