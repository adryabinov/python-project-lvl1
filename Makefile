build:
	poetry build

install:
	poetry install

package-install:
	pip install --user dist/*.whl

brain-games:
	poetry run brain-games

.PHONY: build install brain-games