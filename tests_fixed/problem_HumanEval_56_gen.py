import unittest
from sut_llm.problem_HumanEval_56 import correct_bracketing

class TestCorrectBracketing(unittest.TestCase):

    def test_empty_string(self):
        """Test with an empty string, which should be considered correctly bracketed."""
        self.assertEqual(correct_bracketing(""), True)

    def test_minimal_correct_bracketing(self):
        """Test the simplest correct bracketing pair, covering boundary and typical input."""
        self.assertEqual(correct_bracketing("<>"), True)

    def test_minimal_incorrect_order(self):
        """Test a minimal case where brackets are in the wrong order, catching early exit logic."""
        self.assertEqual(correct_bracketing("><"), False)

    def test_single_open_bracket(self):
        """Test with a single opening bracket, an edge case for unbalanced final count."""
        self.assertEqual(correct_bracketing("<"), False)

    def test_single_close_bracket(self):
        """Test with a single closing bracket, an edge case for immediate negative balance."""
        self.assertEqual(correct_bracketing(">"), False)

    def test_nested_correct_bracketing(self):
        """Test a typical case with nested correct brackets, from the docstring."""
        self.assertEqual(correct_bracketing("<<><>>"), True)

    def test_unbalanced_start_with_close(self):
        """Test a case from docstring where it starts with a closing bracket, leading to early failure."""
        self.assertEqual(correct_bracketing("><<>"), False)

    def test_unbalanced_too_many_open(self):
        """Test an extreme input with only opening brackets, ensuring final balance check."""
        self.assertEqual(correct_bracketing("<<<"), False)

    def test_unbalanced_too_many_close(self):
        """Test an extreme input where balance goes negative due to too many closing brackets."""
        self.assertEqual(correct_bracketing("<>>"), False)

    def test_complex_correct_bracketing(self):
        """Test a more complex but correctly bracketed sequence, verifying full traversal."""
        self.assertEqual(correct_bracketing("<><<>>"), True)