.PHONY: default install lint link-check test

default: test

install:
	pipenv install --dev --skip-lock

lint:
	black .
	flake8

lint-check:
	flake8
	black --check --diff .

test:
	PYTHONPATH=./src pytest

