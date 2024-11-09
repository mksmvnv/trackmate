.PHONY: all run lint
.SILENT: all run lint

WORKDIR=./src
POETRYFLAGS=--config pyproject.toml

all: run lint

run:
	poetry run docker-compose -f docker-compose.yml up -d --build

lint:
	poetry run black $(WORKDIR) $(POETRYFLAGS)