# pylint: disable=missing-docstring

import unittest

import able

def parse(string):
    return able.parse(string, rule_name='list')


class TestLists(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(parse('[]'), [])

    def test_numeric(self):
        self.assertEqual(parse('[1 2 3]'), [1, 2, 3])

    def test_text(self):
        self.assertEqual(parse('["a" "b" "c"]'), ['a', 'b', 'c'])

    def test_pair(self):
        self.assertEqual(parse('[key: "value"]'), [('key', 'value')])

    def test_mixed(self):
        self.assertEqual(parse('["a" 1 b: 2]'), ['a', 1, ('b', 2)])
