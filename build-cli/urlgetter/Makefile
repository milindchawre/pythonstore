.PHONY: default lint lint-check install test

default: test

install:
	pipenv install --dev --skip-lock

lint:
	black .
	flake8

link-check:
	flake8
	black --check --diff .

test:
	PYTHONPATH=./src pytest

