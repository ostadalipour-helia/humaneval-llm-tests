import unittest
from sut.problem_HumanEval_14 import all_prefixes

class Test_all_prefixes(unittest.TestCase):

    def test_normal_case_abc(self):
        self.assertEqual(all_prefixes("abc"), ['a', 'ab', 'abc'])

    def test_normal_case_hello(self):
        self.assertEqual(all_prefixes("hello"), ['h', 'he', 'hel', 'hell', 'hello'])

    def test_edge_case_empty_string(self):
        self.assertEqual(all_prefixes(""), [])

    def test_edge_case_single_character(self):
        self.assertEqual(all_prefixes("a"), ['a'])

    def test_edge_case_numbers_and_special_chars(self):
        self.assertEqual(all_prefixes("123!"), ['1', '12', '123', '123!'])

    def test_edge_case_whitespace(self):
        self.assertEqual(all_prefixes("  "), [' ', '  '])

    def test_retest_empty_string(self):
        self.assertEqual(all_prefixes(""), [])

    def test_retest_single_character(self):
        self.assertEqual(all_prefixes("a"), ['a'])

    def test_retest_normal_case_abc(self):
        self.assertEqual(all_prefixes("abc"), ['a', 'ab', 'abc'])

    def test_retest_normal_case_hello(self):
        self.assertEqual(all_prefixes("hello"), ['h', 'he', 'hel', 'hell', 'hello'])