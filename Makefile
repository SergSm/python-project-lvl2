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
	poetry run pytest --junit-xml=./tests/coverage.xml

.PHONY: gendiff test
