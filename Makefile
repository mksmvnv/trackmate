.PHONY: all run lint
.SILENT: all run lint

WORKDIR=$(shell pwd)/src
POETRYFLAGS=--config pyproject.toml

all: run lint

run:
	poetry run $(WORKDIR)/manage.py makemigrations tasks
	poetry run $(WORKDIR)/manage.py makemigrations profiles
	poetry run $(WORKDIR)/manage.py makemigrations users
	poetry run $(WORKDIR)/manage.py migrate
	poetry run $(WORKDIR)/manage.py runserver 0.0.0.0:8000

lint:
	poetry run black $(WORKDIR) $(POETRYFLAGS)