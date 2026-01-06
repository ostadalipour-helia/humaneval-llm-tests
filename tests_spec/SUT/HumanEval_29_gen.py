import unittest
from sut.problem_HumanEval_29 import filter_by_prefix

class Test_filter_by_prefix(unittest.TestCase):

    def test_case_0(self):
        strings = ['abc', 'bcd', 'cde', 'array']
        prefix = 'a'
        expected = ['abc', 'array']
        self.assertEqual(repr(filter_by_prefix(strings, prefix)), repr(expected))

    def test_case_1(self):
        strings = ['apple', 'banana', 'apricot', 'grape']
        prefix = 'ap'
        expected = ['apple', 'apricot']
        self.assertEqual(repr(filter_by_prefix(strings, prefix)), repr(expected))

    def test_case_2(self):
        strings = ['hello', 'world']
        prefix = 'h'
        expected = ['hello']
        self.assertEqual(repr(filter_by_prefix(strings, prefix)), repr(expected))

    def test_case_3(self):
        strings = ['cat', 'dog', 'cow']
        prefix = 'z'
        expected = []
        self.assertEqual(repr(filter_by_prefix(strings, prefix)), repr(expected))

    def test_case_4(self):
        strings = ['test', 'testing', 'tester']
        prefix = 'test'
        expected = ['test', 'testing', 'tester']
        self.assertEqual(repr(filter_by_prefix(strings, prefix)), repr(expected))

    def test_case_5(self):
        strings = []
        prefix = 'a'
        expected = []
        self.assertEqual(repr(filter_by_prefix(strings, prefix)), repr(expected))

    def test_case_6(self):
        strings = ['abc', 'def']
        prefix = ''
        expected = ['abc', 'def']
        self.assertEqual(repr(filter_by_prefix(strings, prefix)), repr(expected))

    def test_case_7(self):
        strings = ['a', 'b', 'c']
        prefix = 'a'
        expected = ['a']
        self.assertEqual(repr(filter_by_prefix(strings, prefix)), repr(expected))

    def test_case_8(self):
        strings = ['apple']
        prefix = 'ap'
        expected = ['apple']
        self.assertEqual(repr(filter_by_prefix(strings, prefix)), repr(expected))

    def test_case_9(self):
        strings = ['banana']
        prefix = 'ap'
        expected = []
        self.assertEqual(repr(filter_by_prefix(strings, prefix)), repr(expected))