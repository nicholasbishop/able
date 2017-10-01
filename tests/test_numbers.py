# pylint: disable=missing-docstring

import math
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

    def test_positive_one(self):
        self.assertEqual(parse('+1'), 1)

    def test_float(self):
        self.assertEqual(parse('1.5'), 1.5)

    def test_negative_float(self):
        self.assertEqual(parse('-1.5'), -1.5)

    def test_positive_float(self):
        self.assertEqual(parse('+1.5'), +1.5)

    def test_hex(self):
        self.assertEqual(parse('0xff'), 255)

    def test_binary(self):
        self.assertEqual(parse('0b111'), 7)

    def test_case(self):
        self.assertEqual(parse('0XA'), 10)
        self.assertEqual(parse('0B1'), 1)

    def test_nan(self):
        self.assertTrue(math.isnan(parse('nan')))
        self.assertFalse(math.isnan(parse('1.0')))

    def test_infinity(self):
        inf = float('inf')
        self.assertEqual(parse('inf'), inf)
        self.assertEqual(parse('infinity'), inf)
        self.assertEqual(parse('+infinity'), inf)
        self.assertEqual(parse('+INFINITY'), inf)
        self.assertEqual(parse('iNFiNiTY'), inf)
        self.assertEqual(parse('-inf'), -inf)
        self.assertEqual(parse('-infinity'), -inf)
