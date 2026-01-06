import unittest
from sut.problem_HumanEval_56 import correct_bracketing

class Test_correct_bracketing(unittest.TestCase):

    # Normal cases
    def test_normal_simple_balanced(self):
        self.assertTrue(correct_bracketing("<>"))

    def test_normal_nested_balanced(self):
        self.assertTrue(correct_bracketing("<<><>>"))

    def test_normal_deeply_nested_balanced(self):
        self.assertTrue(correct_bracketing("<<<>>>"))

    # Edge cases
    def test_edge_empty_string(self):
        self.assertTrue(correct_bracketing(""))

    def test_edge_single_open(self):
        self.assertFalse(correct_bracketing("<"))

    def test_edge_single_close(self):
        self.assertFalse(correct_bracketing(">"))

    def test_edge_unbalanced_start_close(self):
        self.assertFalse(correct_bracketing("><<>"))

    def test_edge_multiple_close_only(self):
        self.assertFalse(correct_bracketing(">>"))

    def test_edge_multiple_open_only(self):
        self.assertFalse(correct_bracketing("<<<"))

    # Error cases
    def test_error_non_string_null_input(self):
        # According to preconditions, input must be a string.
        # For `None`, a TypeError is expected for non-string input.
        with self.assertRaises(TypeError):
            correct_bracketing(None)

    def test_error_invalid_chars_abc(self):
        # According to preconditions, string must only contain '<' and '>'.
        # The spec explicitly states ValueError for this case.
        with self.assertRaises(ValueError):
            correct_bracketing("<abc>")

    def test_error_invalid_chars_curly_braces(self):
        # According to preconditions, string must only contain '<' and '>'.
        # The spec explicitly states ValueError for this case.
        with self.assertRaises(ValueError):
            correct_bracketing("<{}>")