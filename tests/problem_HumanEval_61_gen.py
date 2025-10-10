import unittest
from sut.problem_HumanEval_61 import correct_bracketing

class TestCorrectBracketing(unittest.TestCase):

    def test_empty_string(self):
        # Edge Case: Empty string, considered correctly bracketed.
        # Catches mutations changing initial balance or loop conditions.
        self.assertEqual(correct_bracketing(""), True)

    def test_single_opening_bracket(self):
        # Boundary Case: Single opening bracket.
        # Catches off-by-one errors in balance check or loop termination.
        self.assertEqual(correct_bracketing("("), False)

    def test_single_closing_bracket(self):
        # Boundary Case: Single closing bracket.
        # Catches off-by-one errors in balance check or initial negative balance.
        self.assertEqual(correct_bracketing(")"), False)

    def test_minimal_correct_bracketing(self):
        # Typical Case: Simplest correct pair.
        # Verifies basic functionality and balance increment/decrement.
        self.assertEqual(correct_bracketing("()"), True)

    def test_minimal_incorrect_order(self):
        # Logic Mutation: Closing bracket before opening.
        # Catches errors where negative balance isn't checked or handled.
        self.assertEqual(correct_bracketing(")("), False)

    def test_nested_correct_bracketing(self):
        # Typical Case: Nested and sequential correct brackets.
        # Verifies correct handling of multiple levels of nesting.
        self.assertEqual(correct_bracketing("(()())"), True)

    def test_unbalanced_extra_opening_at_end(self):
        # Off-by-One Error: One extra opening bracket at the end.
        # Catches errors where final balance isn't checked for zero.
        self.assertEqual(correct_bracketing("(()"), False)

    def test_unbalanced_extra_closing_early(self):
        # Logic Mutation: Balance goes negative early.
        # Catches errors where balance is only checked at the end, not during iteration.
        self.assertEqual(correct_bracketing("())("), False)

    def test_long_complex_correct_bracketing(self):
        # Extreme Case: Long string with multiple nested and sequential correct brackets.
        # Verifies robustness for longer inputs and complex structures.
        self.assertEqual(correct_bracketing("((()())(()()))"), True)

    def test_long_complex_incorrect_bracketing_subtle_error(self):
        # Extreme Case & Off-by-One: Long string with a subtle imbalance.
        # Catches subtle bugs where a single misplaced or missing bracket is overlooked.
        self.assertEqual(correct_bracketing("((()())(()()))("), False)