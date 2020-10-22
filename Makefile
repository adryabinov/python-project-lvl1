lint:
	poetry run flake8 brain_games

build:
	poetry build

install:
	poetry install

package-install:
	pip install --user dist/*.whl

brain-games:
	poetry run brain-games

.PHONY: lint build install brain-games