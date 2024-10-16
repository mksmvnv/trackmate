.PHONY: all run lint

export $(shell sed 's/=.*//' .env)

WORKDIR=./src
POETRYFLAGS=--config pyproject.toml

all: run lint

run:
	@echo "Running server..."
	@poetry run python3 $(WORKDIR)/manage.py runserver $(DJANGO_HOST):$(DJANGO_PORT)

lint:
	@echo "Linting..."
	@black $(WORKDIR) $(POETRYFLAGS)
	@echo "Linting done!"