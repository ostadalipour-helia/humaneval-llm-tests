import unittest
import sut.problem_HumanEval_119 as mod

class TestHybrid(unittest.TestCase):
    def test_1_docstring_example_one_order_works(self):
            # Test case from docstring where s1+s2 is balanced, s2+s1 is not.
            # s1 = '()(', s2 = ')'
            # s1+s2 = '()()' (balanced)
            # s2+s1 = ')()(' (not balanced)
            self.assertEqual(mod.match_parens(['()(', ')']), 'Yes')

    def test_2_docstring_example_neither_order_works(self):
            # Test case from docstring where neither s1+s2 nor s2+s1 is balanced.
            # s1 = ')', s2 = ')'
            # s1+s2 = '))' (not balanced)
            # s2+s1 = '))' (not balanced)
            self.assertEqual(mod.match_parens([')', ')']), 'No')

    def test_3_empty_strings_edge_case(self):
            # Boundary test: both strings are empty.
            # s1 = '', s2 = ''
            # s1+s2 = '' (balanced)
            self.assertEqual(mod.match_parens(['', '']), 'Yes')

    def test_4_one_empty_string_one_balanced_string_edge_case(self):
            # Edge case: one string is empty, the other is a simple balanced string.
            # s1 = '()', s2 = ''
            # s1+s2 = '()' (balanced)
            self.assertEqual(mod.match_parens(['()', '']), 'Yes')

    def test_5_two_individually_balanced_strings_typical(self):
            # Typical case: both strings are individually balanced.
            # s1 = '()', s2 = '()'
            # s1+s2 = '()()' (balanced)
            self.assertEqual(mod.match_parens(['()', '()']), 'Yes')

    def test_6_strings_balance_only_in_s1_plus_s2_order_boundary(self):
            # Logic mutation test: s1+s2 is balanced, but s2+s1 is not.
            # Also a boundary case for minimal balancing.
            # s1 = '((', s2 = '))'
            # s1+s2 = '(())' (balanced)
            # s2+s1 = '))((` (not balanced)
            self.assertEqual(mod.match_parens(['((', '))']), 'Yes')

    def test_7_strings_balance_only_in_s2_plus_s1_order_boundary(self):
            # Logic mutation test: s2+s1 is balanced, but s1+s2 is not.
            # Also a boundary case for minimal balancing.
            # s1 = '))', s2 = '(('
            # s1+s2 = '))((` (not balanced)
            # s2+s1 = '(())' (balanced)
            self.assertEqual(mod.match_parens(['))', '((']), 'Yes')

    def test_8_total_count_mismatch_extreme_unusual(self):
            # Extreme case: total number of open and close parentheses don't match.
            # s1 = '(', s2 = '((('
            # Total open: 4, Total close: 0. Cannot be balanced.
            self.assertEqual(mod.match_parens(['(', '(((']), 'No')

    def test_9_correct_total_count_but_bad_order_off_by_one(self):
            # Off-by-one error test: total counts match, but prefix balance fails for both orders.
            # s1 = '()', s2 = ')('
            # s1+s2 = '())(' (balance goes negative at index 2)
            # s2+s1 = ')()(' (balance goes negative at index 0)
            self.assertEqual(mod.match_parens(['()', ')(']), 'No')

    def test_normal_case_simple_match(self):
            # Input: ['(', ')']
            # Reason: Concatenating as '()' results in a good string.
            self.assertEqual(mod.match_parens(['(', ')']), 'Yes')

    def test_normal_case_complex_match(self):
            # Input: ['()(', ')']
            # Reason: Concatenating as '()()' results in a good string.
            self.assertEqual(mod.match_parens(['()(', ')']), 'Yes')

    def test_normal_case_nested_match(self):
            # Input: ['((', '))']
            # Reason: Concatenating as '(())' results in a good string.
            self.assertEqual(mod.match_parens(['((', '))']), 'Yes')
    
        # Edge Cases

    def test_edge_case_empty_strings(self):
            # Input: ['', '']
            # Reason: An empty string is considered good/balanced.
            self.assertEqual(mod.match_parens(['', '']), 'Yes')

    def test_edge_case_one_empty_string(self):
            # Input: ['()', '']
            # Reason: Concatenating as '()' results in a good string.
            self.assertEqual(mod.match_parens(['()', '']), 'Yes')

    def test_edge_case_no_match_total_unbalanced(self):
            # Input: ['))))))))))', '(((((((((((']
            # Reason: The total count of '(' does not equal ')'.
            self.assertEqual(mod.match_parens(['))))))))))', '(((((((((((']), 'No')

    def test_edge_case_no_match_interleaved(self):
            # Input: ['()', ')(']
            # Reason: Neither '())(' nor ')()(' is good.
            self.assertEqual(mod.match_parens(['()', ')(']), 'No')
    
        # Error Cases

    def test_error_not_a_list(self):
            # Input: 123
            # Reason: Violates 'The input `lst` must be a Python list'.
            with self.assertRaises(TypeError):
                mod.match_parens(123)

    def test_error_list_too_short(self):
            # Input: []
            # Reason: Violates 'lst must contain exactly two elements'.
            # Accessing lst[0] or lst[1] would raise IndexError.
            with self.assertRaises(IndexError):
                mod.match_parens([])

    def test_error_non_string_element(self):
            # Input: ['()', 123]
            # Reason: Violates 'Each element in `lst` must be a string'.
            with self.assertRaises(TypeError):
                mod.match_parens(['()', 123])

