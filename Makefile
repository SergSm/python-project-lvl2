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

.PHONY: gendiff
