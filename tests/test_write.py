import unittest

from able import util

class TestWrite(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(util.serialize({}), 'able: 1\n')
