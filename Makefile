lint:
	poetry run flake8 brain_games

build:
	poetry build

install:
	poetry install

publish:
	poetry publish --dry-run

package-install:
	pip install --user dist/*.whl

brain-games:
	poetry run brain-games

.PHONY: lint build install publish brain-games