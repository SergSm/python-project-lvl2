install:
	poetry install

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

build:
	poetry build

gendiff:
	poetry run gendiff

test:
	poetry run pytest --cov=gendiff --cov-report xml tests/

.PHONY: gendiff test
