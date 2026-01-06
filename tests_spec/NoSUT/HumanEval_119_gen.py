import unittest
from sut.problem_HumanEval_119 import match_parens

class Test_match_parens(unittest.TestCase):

    # Normal Cases
    def test_normal_case_simple_match(self):
        # Input: ['(', ')']
        # Reason: Concatenating as '()' results in a good string.
        self.assertEqual(match_parens(['(', ')']), 'Yes')

    def test_normal_case_complex_match(self):
        # Input: ['()(', ')']
        # Reason: Concatenating as '()()' results in a good string.
        self.assertEqual(match_parens(['()(', ')']), 'Yes')

    def test_normal_case_nested_match(self):
        # Input: ['((', '))']
        # Reason: Concatenating as '(())' results in a good string.
        self.assertEqual(match_parens(['((', '))']), 'Yes')

    # Edge Cases
    def test_edge_case_empty_strings(self):
        # Input: ['', '']
        # Reason: An empty string is considered good/balanced.
        self.assertEqual(match_parens(['', '']), 'Yes')

    def test_edge_case_one_empty_string(self):
        # Input: ['()', '']
        # Reason: Concatenating as '()' results in a good string.
        self.assertEqual(match_parens(['()', '']), 'Yes')

    def test_edge_case_no_match_total_unbalanced(self):
        # Input: ['))))))))))', '(((((((((((']
        # Reason: The total count of '(' does not equal ')'.
        self.assertEqual(match_parens(['))))))))))', '(((((((((((']), 'No')

    def test_edge_case_no_match_order_fails(self):
        # Input: [')))', '(((']
        # Reason: Neither ')))(((' nor '((()))' is good. The latter has a balance counter drop below zero immediately.
        self.assertEqual(match_parens([')))', '(((']), 'No')

    def test_edge_case_no_match_interleaved(self):
        # Input: ['()', ')(']
        # Reason: Neither '())(' nor ')()(' is good.
        self.assertEqual(match_parens(['()', ')(']), 'No')

    # Error Cases
    def test_error_not_a_list(self):
        # Input: 123
        # Reason: Violates 'The input `lst` must be a Python list'.
        with self.assertRaises(TypeError):
            match_parens(123)

    def test_error_list_too_short(self):
        # Input: []
        # Reason: Violates 'lst must contain exactly two elements'.
        # Accessing lst[0] or lst[1] would raise IndexError.
        with self.assertRaises(IndexError):
            match_parens([])

    def test_error_non_string_element(self):
        # Input: ['()', 123]
        # Reason: Violates 'Each element in `lst` must be a string'.
        with self.assertRaises(TypeError):
            match_parens(['()', 123])

    def test_error_invalid_characters(self):
        # Input: ['()', 'a(b)']
        # Reason: Violates 'Each character within these two strings must be either an open parenthesis '(' or a close parenthesis ')'.
        with self.assertRaises(ValueError):
            match_parens(['()', 'a(b)'])