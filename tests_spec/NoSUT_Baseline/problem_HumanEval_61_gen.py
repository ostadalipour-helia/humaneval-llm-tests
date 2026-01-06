import unittest
import sut.problem_HumanEval_61 as mod

class TestHybrid(unittest.TestCase):
    def test_empty_string(self):
            # Edge Case: Empty string, considered correctly bracketed.
            # Catches mutations changing initial balance or loop conditions.
            self.assertEqual(mod.correct_bracketing(""), True)

    def test_single_opening_bracket(self):
            # Boundary Case: Single opening bracket.
            # Catches off-by-one errors in balance check or loop termination.
            self.assertEqual(mod.correct_bracketing("("), False)

    def test_single_closing_bracket(self):
            # Boundary Case: Single closing bracket.
            # Catches off-by-one errors in balance check or initial negative balance.
            self.assertEqual(mod.correct_bracketing(")"), False)

    def test_minimal_incorrect_order(self):
            # Logic Mutation: Closing bracket before opening.
            # Catches errors where negative balance isn't checked or handled.
            self.assertEqual(mod.correct_bracketing(")("), False)

    def test_unbalanced_extra_opening_at_end(self):
            # Off-by-One Error: One extra opening bracket at the end.
            # Catches errors where final balance isn't checked for zero.
            self.assertEqual(mod.correct_bracketing("(()"), False)

    def test_unbalanced_extra_closing_early(self):
            # Logic Mutation: Balance goes negative early.
            # Catches errors where balance is only checked at the end, not during iteration.
            self.assertEqual(mod.correct_bracketing("())("), False)

    def test_long_complex_incorrect_bracketing_subtle_error(self):
            # Extreme Case & Off-by-One: Long string with a subtle imbalance.
            # Catches subtle bugs where a single misplaced or missing bracket is overlooked.
            self.assertEqual(mod.correct_bracketing("((()())(()()))("), False)

    def test_normal_case_simple_pair(self):
            self.assertTrue(mod.correct_bracketing("()"))

    def test_normal_case_nested_and_sequential(self):
            self.assertTrue(mod.correct_bracketing("(()())"))

    def test_normal_case_deeply_nested(self):
            self.assertTrue(mod.correct_bracketing("((()))"))

    def test_edge_case_empty_string(self):
            self.assertTrue(mod.correct_bracketing(""))

    def test_edge_case_single_opening_bracket(self):
            self.assertFalse(mod.correct_bracketing("("))

    def test_edge_case_single_closing_bracket(self):
            self.assertFalse(mod.correct_bracketing(")"))

    def test_edge_case_mismatched_order(self):
            self.assertFalse(mod.correct_bracketing(")("))

    def test_edge_case_unclosed_brackets(self):
            self.assertFalse(mod.correct_bracketing("(("))

    def test_edge_case_premature_closing(self):
            self.assertFalse(mod.correct_bracketing("())"))

    def test_edge_case_trailing_opening(self):
            self.assertFalse(mod.correct_bracketing("()("))

    def test_error_case_non_string_input_int(self):
            with self.assertRaises(TypeError):
                mod.correct_bracketing(123)

    def test_error_case_non_string_input_none(self):
            with self.assertRaises(TypeError):
                mod.correct_bracketing(None)

