import unittest
import sut.problem_HumanEval_56 as mod

class TestHybrid(unittest.TestCase):
    def test_empty_string(self):
            """Test with an empty string, which should be considered correctly bracketed."""
            self.assertEqual(mod.correct_bracketing(""), True)

    def test_minimal_incorrect_order(self):
            """Test a minimal case where brackets are in the wrong order, catching early exit logic."""
            self.assertEqual(mod.correct_bracketing("><"), False)

    def test_single_open_bracket(self):
            """Test with a single opening bracket, an edge case for unbalanced final count."""
            self.assertEqual(mod.correct_bracketing("<"), False)

    def test_single_close_bracket(self):
            """Test with a single closing bracket, an edge case for immediate negative balance."""
            self.assertEqual(mod.correct_bracketing(">"), False)

    def test_unbalanced_start_with_close(self):
            """Test a case from docstring where it starts with a closing bracket, leading to early failure."""
            self.assertEqual(mod.correct_bracketing("><<>"), False)

    def test_unbalanced_too_many_open(self):
            """Test an extreme input with only opening brackets, ensuring final balance check."""
            self.assertEqual(mod.correct_bracketing("<<<"), False)

    def test_unbalanced_too_many_close(self):
            """Test an extreme input where balance goes negative due to too many closing brackets."""
            self.assertEqual(mod.correct_bracketing("<>>"), False)

    def test_normal_simple_balanced(self):
            self.assertTrue(mod.correct_bracketing("<>"))

    def test_normal_nested_balanced(self):
            self.assertTrue(mod.correct_bracketing("<<><>>"))

    def test_normal_deeply_nested_balanced(self):
            self.assertTrue(mod.correct_bracketing("<<<>>>"))
    
        # Edge cases

    def test_edge_empty_string(self):
            self.assertTrue(mod.correct_bracketing(""))

    def test_edge_single_open(self):
            self.assertFalse(mod.correct_bracketing("<"))

    def test_edge_single_close(self):
            self.assertFalse(mod.correct_bracketing(">"))

    def test_edge_unbalanced_start_close(self):
            self.assertFalse(mod.correct_bracketing("><<>"))

    def test_edge_multiple_close_only(self):
            self.assertFalse(mod.correct_bracketing(">>"))

    def test_edge_multiple_open_only(self):
            self.assertFalse(mod.correct_bracketing("<<<"))
    
        # Error cases

    def test_error_non_string_null_input(self):
            # According to preconditions, input must be a string.
            # For `None`, a TypeError is expected for non-string input.
            with self.assertRaises(TypeError):
                mod.correct_bracketing(None)

