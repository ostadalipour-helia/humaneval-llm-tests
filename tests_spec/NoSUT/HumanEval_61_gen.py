import unittest
from sut.problem_HumanEval_61 import correct_bracketing

class Test_correct_bracketing(unittest.TestCase):

    def test_normal_case_simple_pair(self):
        self.assertTrue(correct_bracketing("()"))

    def test_normal_case_nested_and_sequential(self):
        self.assertTrue(correct_bracketing("(()())"))

    def test_normal_case_deeply_nested(self):
        self.assertTrue(correct_bracketing("((()))"))

    def test_edge_case_empty_string(self):
        self.assertTrue(correct_bracketing(""))

    def test_edge_case_single_opening_bracket(self):
        self.assertFalse(correct_bracketing("("))

    def test_edge_case_single_closing_bracket(self):
        self.assertFalse(correct_bracketing(")"))

    def test_edge_case_mismatched_order(self):
        self.assertFalse(correct_bracketing(")("))

    def test_edge_case_unclosed_brackets(self):
        self.assertFalse(correct_bracketing("(("))

    def test_edge_case_premature_closing(self):
        self.assertFalse(correct_bracketing("())"))

    def test_edge_case_trailing_opening(self):
        self.assertFalse(correct_bracketing("()("))

    def test_error_case_non_string_input_int(self):
        with self.assertRaises(TypeError):
            correct_bracketing(123)

    def test_error_case_non_string_input_list(self):
        with self.assertRaises(TypeError):
            correct_bracketing(['(', ')'])

    def test_error_case_non_string_input_none(self):
        with self.assertRaises(TypeError):
            correct_bracketing(None)