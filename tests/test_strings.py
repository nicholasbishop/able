# pylint: disable=missing-docstring

import unittest

import able

def parse(string):
    return able.parse(string, rule_name='string')


class TestStrings(unittest.TestCase):
    def test_double_quoted(self):
        self.assertEqual(parse('"abc"'), 'abc')

    def test_single_quoted(self):
        self.assertEqual(parse("'abc'"), 'abc')

    def test_multiline_string(self):
        self.assertEqual(parse('"a\nb\nc"'), 'a\nb\nc')
