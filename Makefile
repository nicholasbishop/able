all: able/parser.py lint test

able/parser.py: able/grammar.ebnf
	python -m tatsu --outfile able/parser.py able/grammar.ebnf

lint:
	python -m pylint --ignore=parser.py able setup.py tests

test:
	python -m unittest discover

.PHONY: all lint test
