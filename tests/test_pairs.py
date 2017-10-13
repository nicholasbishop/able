# pylint: disable=missing-docstring

import unittest

import able

def parse(string):
    return able.parse(string, rule_name='pair')


class TestPairs(unittest.TestCase):
    def test_simple_pair(self):
        self.assertEqual(parse('a: 1'), ('a', 1))
