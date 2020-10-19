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
	poetry run gendiff ~/Projects/python-project-lvl2/gendiff/file1.json gendiff/file2.json

.PHONY: gendiff test
