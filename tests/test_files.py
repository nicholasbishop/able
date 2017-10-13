# pylint: disable=missing-docstring

import ast
import os
import unittest

import able

class TestFiles(unittest.TestCase):
    pass


def get_test_paths():
    result = set()

    script_path = os.path.dirname(os.path.realpath(__file__))
    files_path = os.path.join(script_path, 'files')

    for name in os.listdir(files_path):
        path = os.path.join(files_path, name)
        no_extension = os.path.splitext(path)[0]
        result.add(no_extension)

    return result


def make_test_method(path):
    def method(self):
        with open(path + '.py') as expected_file:
            expected = ast.literal_eval(expected_file.read())
        with open(path + '.able') as src_file:
            actual = able.parse(src_file.read())
        self.assertEqual(actual, expected)
    return method


def make_test_methods():
    for path in get_test_paths():
        test_name = 'test_' + format(os.path.basename(path))
        setattr(TestFiles, test_name, make_test_method(path))


make_test_methods()
