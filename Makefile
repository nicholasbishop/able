all: lint test

lint:
	python -m pylint able setup.py tests

test:
	python -m unittest discover

.PHONY: all lint test
