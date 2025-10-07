import unittest
from sut_llm.problem_HumanEval_56 import correct_bracketing

class TestCorrectBracketing(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(correct_bracketing(""))

    def test_basic_balanced(self):
        self.assertTrue(correct_bracketing("<>"))

    def test_basic_unbalanced_open(self):
        self.assertFalse(correct_bracketing("<"))

    def test_basic_unbalanced_close(self):
        self.assertFalse(correct_bracketing(">"))

    def test_nested_balanced(self):
        self.assertTrue(correct_bracketing("<<>>"))

    def test_nested_unbalanced_too_many_open(self):
        self.assertFalse(correct_bracketing("<<>"))

    def test_nested_unbalanced_too_many_close(self):
        self.assertFalse(correct_bracketing("<>>>"))

    def test_mixed_balanced_docstring_example(self):
        self.assertTrue(correct_bracketing("<<><>>"))

    def test_mixed_unbalanced_starts_with_close_docstring_example(self):
        self.assertFalse(correct_bracketing("><<>"))

    def test_longer_complex_balanced(self):
        self.assertTrue(correct_bracketing("<><<>>"))