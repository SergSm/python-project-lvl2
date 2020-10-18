install:
	poetry install

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

build:
	poetry build
