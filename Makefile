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

brain-even:
	poetry run brain-even

brain-progression:
	poetry run brain-progression

.PHONY: lint build install publish brain-games brain-even brain-progression