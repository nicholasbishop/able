import argparse
import os
import pprint

import lictionary
import tatsu

_PARSER = None

class Semantics(object):
    def decimal_integer(self, ast):
        return int(''.join(ast))

    def hex_integer(self, ast):
        return int(''.join(ast), 16)

    def binary_integer(self, ast):
        return int(''.join(ast), 2)

    def float(self, ast):
        return float(''.join(ast))

    def pair(self, ast):
        key, value = ast
        return (key, value)

    def list(self, ast):
        return lictionary.Lictionary(*ast)

    def implicit_list(self, ast):
        return lictionary.Lictionary(*ast)


def read_grammar():
    script_path = os.path.dirname(os.path.realpath(__file__))
    grammar_path = os.path.join(script_path, 'grammar.ebnf')
    with open(grammar_path) as grammar:
        return grammar.read()


def get_parser():
    global _PARSER
    if not _PARSER:
        _PARSER = tatsu.compile(read_grammar())
    return _PARSER


def parse(string, rule_name=None):
    parser = get_parser()
    return parser.parse(string, rule_name=rule_name, semantics=Semantics())


def parse_cli_args():
    parser = argparse.ArgumentParser(description='parse an Able file')
    parser.add_argument('path')
    return parser.parse_args()


def main():
    cli_args = parse_cli_args()
    parser = get_parser()
    with open(cli_args.path) as rfile:
        ast = parse(rfile.read())
    pprint.pprint(ast)
