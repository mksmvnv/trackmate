.PHONY: all run lint

WORKDIR=./src
POETRYFLAGS=--config pyproject.toml

all: run lint

run:
	@echo "Running server..."
	@poetry run python3 $(WORKDIR)/manage.py runserver

lint:
	@echo "Linting..."
	@black $(WORKDIR) $(POETRYFLAGS)
	@echo "Linting done!"