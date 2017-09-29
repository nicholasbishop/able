import argparse
import os
import pprint

import tatsu

class Semantics(object):
    def number(self, ast):
        return int(ast)

    def pair(self, ast):
        key, value = ast
        return (key, value)


def get_parser():
    script_path = os.path.dirname(os.path.realpath(__file__))
    grammar_path = os.path.join(script_path, 'grammar.ebnf')
    with open(grammar_path) as grammar:
        return tatsu.compile(grammar.read())


def parse_string(string):
    parser = get_parser()
    return parser.parse(string, semantics=Semantics())


def parse_file(rfile):
    parser = get_parser()
    return parse_string(rfile.read())


def parse_cli_args():
    parser = argparse.ArgumentParser(description='parse an Able file')
    parser.add_argument('path')
    return parser.parse_args()


def main():
    cli_args = parse_cli_args()
    parser = get_parser()
    with open(cli_args.path) as rfile:
        ast = parse_file(rfile)
    pprint.pprint(ast)
