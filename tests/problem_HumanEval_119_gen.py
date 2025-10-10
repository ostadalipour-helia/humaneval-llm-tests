import unittest
from sut.problem_HumanEval_119 import match_parens

class TestMatchParens(unittest.TestCase):

    def test_1_docstring_example_one_order_works(self):
        # Test case from docstring where s1+s2 is balanced, s2+s1 is not.
        # s1 = '()(', s2 = ')'
        # s1+s2 = '()()' (balanced)
        # s2+s1 = ')()(' (not balanced)
        self.assertEqual(match_parens(['()(', ')']), 'Yes')

    def test_2_docstring_example_neither_order_works(self):
        # Test case from docstring where neither s1+s2 nor s2+s1 is balanced.
        # s1 = ')', s2 = ')'
        # s1+s2 = '))' (not balanced)
        # s2+s1 = '))' (not balanced)
        self.assertEqual(match_parens([')', ')']), 'No')

    def test_3_empty_strings_edge_case(self):
        # Boundary test: both strings are empty.
        # s1 = '', s2 = ''
        # s1+s2 = '' (balanced)
        self.assertEqual(match_parens(['', '']), 'Yes')

    def test_4_one_empty_string_one_balanced_string_edge_case(self):
        # Edge case: one string is empty, the other is a simple balanced string.
        # s1 = '()', s2 = ''
        # s1+s2 = '()' (balanced)
        self.assertEqual(match_parens(['()', '']), 'Yes')

    def test_5_two_individually_balanced_strings_typical(self):
        # Typical case: both strings are individually balanced.
        # s1 = '()', s2 = '()'
        # s1+s2 = '()()' (balanced)
        self.assertEqual(match_parens(['()', '()']), 'Yes')

    def test_6_strings_balance_only_in_s1_plus_s2_order_boundary(self):
        # Logic mutation test: s1+s2 is balanced, but s2+s1 is not.
        # Also a boundary case for minimal balancing.
        # s1 = '((', s2 = '))'
        # s1+s2 = '(())' (balanced)
        # s2+s1 = '))((` (not balanced)
        self.assertEqual(match_parens(['((', '))']), 'Yes')

    def test_7_strings_balance_only_in_s2_plus_s1_order_boundary(self):
        # Logic mutation test: s2+s1 is balanced, but s1+s2 is not.
        # Also a boundary case for minimal balancing.
        # s1 = '))', s2 = '(('
        # s1+s2 = '))((` (not balanced)
        # s2+s1 = '(())' (balanced)
        self.assertEqual(match_parens(['))', '((']), 'Yes')

    def test_8_total_count_mismatch_extreme_unusual(self):
        # Extreme case: total number of open and close parentheses don't match.
        # s1 = '(', s2 = '((('
        # Total open: 4, Total close: 0. Cannot be balanced.
        self.assertEqual(match_parens(['(', '(((']), 'No')

    def test_9_correct_total_count_but_bad_order_off_by_one(self):
        # Off-by-one error test: total counts match, but prefix balance fails for both orders.
        # s1 = '()', s2 = ')('
        # s1+s2 = '())(' (balance goes negative at index 2)
        # s2+s1 = ')()(' (balance goes negative at index 0)
        self.assertEqual(match_parens(['()', ')(']), 'No')

    def test_10_long_complex_strings_extreme_unusual(self):
        # Extreme case: long and complex strings that balance in one order.
        # s1 = '((()))((', s2 = '))()()))'
        # s1+s2 = '((()))(())()()))' (balanced)
        # s2+s1 = '))()()))((()))((` (not balanced)
        self.assertEqual(match_parens(['((()))((', '))()()))']), 'Yes')