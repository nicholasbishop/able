import unittest

from able import util

class TestWrite(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(util.serialize({}), '')

    def test_soften(self):
        self.assertEqual(
            util.serialize({'name': 'soften', 'version': '0.1.0'}),
            "name: 'soften'\nversion: '0.1.0'\n")

    def test_int(self):
        self.assertEqual(util.serialize({'int': 1}), 'int: 1\n')

    def test_float(self):
        self.assertEqual(util.serialize({'float': 1.5}), 'float: 1.5\n')
