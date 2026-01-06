import unittest
from sut.problem_HumanEval_12 import longest

class Test_longest(unittest.TestCase):

    def test_normal_case_clearly_longest(self):
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')

    def test_normal_case_varying_lengths(self):
        self.assertEqual(longest(['apple', 'banana', 'cherry']), 'banana')

    def test_normal_case_tie_returns_first(self):
        self.assertEqual(longest(['hello', 'world']), 'hello')

    def test_normal_case_longest_string(self):
        self.assertEqual(longest(['short', 'medium', 'longest_string']), 'longest_string')

    def test_edge_case_empty_list(self):
        self.assertIsNone(longest([]))

    def test_edge_case_all_same_length(self):
        self.assertEqual(longest(['a', 'b', 'c']), 'a')

    def test_edge_case_single_empty_string(self):
        self.assertEqual(longest(['']), '')

    def test_edge_case_with_empty_string(self):
        self.assertEqual(longest(['', 'a', 'bb']), 'bb')

    def test_edge_case_single_element(self):
        self.assertEqual(longest(['a']), 'a')

    def test_edge_case_longest_first(self):
        self.assertEqual(longest(['longest', 'longer', 'long']), 'longest')