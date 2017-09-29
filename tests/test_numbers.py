import unittest

import able

def parse(string):
    return able.parse(string, rule_name='number')

class TestNumbers(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(parse('0'), 0)
