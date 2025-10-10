import unittest
from sut.problem_HumanEval_119 import match_parens

class TestMatchParens(unittest.TestCase):

    def test_example_one(self):
        self.assertEqual(match_parens(['()(', ')']), 'Yes')

    def test_example_two(self):
        self.assertEqual(match_parens([')', ')']), 'No')

    def test_both_empty_strings(self):
        self.assertEqual(match_parens(['', '']), 'Yes')

    def test_one_empty_string_other_balanced(self):
        self.assertEqual(match_parens(['()', '']), 'Yes')

    def test_simple_balance_first_order(self):
        self.assertEqual(match_parens(['(', ')']), 'Yes')

    def test_simple_balance_second_order(self):
        self.assertEqual(match_parens([')', '(']), 'Yes')

    def test_complex_balance_possible(self):
        self.assertEqual(match_parens(['((', '))']), 'Yes')

    def test_not_enough_closing_parens(self):
        self.assertEqual(match_parens(['((', ')']), 'No')

    def test_multiple_balanced_strings_combine(self):
        self.assertEqual(match_parens(['()()', '()']), 'Yes')

    def test_one_string_completes_other(self):
        self.assertEqual(match_parens(['(()', ')']), 'Yes')