import unittest

import able

def parse(string):
    return able.parse(string, rule_name='number')


class TestNumbers(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(parse('0'), 0)

    def test_one(self):
        self.assertEqual(parse('1'), 1)

    def test_negative_one(self):
        self.assertEqual(parse('-1'), -1)

    def test_float(self):
        self.assertEqual(parse('1.5'), 1.5)

    def test_negative_float(self):
        self.assertEqual(parse('-1.5'), -1.5)
