.PHONY: lint run

WORKDIR = .
FLAGS = --target-version py312

all: lint run

lint:
	@echo "Linting..."
	@black $(WORKDIR) $(FLAGS)
	@echo "Successfully linted!"

run:
	@echo "Starting server..."
	python3 manage.py runserver