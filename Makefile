.PHONY: all run lint

WORKDIR=./
POETRYFLAGS=--config pyproject.toml

all: run lint

run:
	@echo "Running server..."
	@poetry run python3 manage.py runserver 8001

lint:
	@echo "Linting..."
	@black $(WORKDIR) $(POETRYFLAGS)
	@echo "Linting done!"