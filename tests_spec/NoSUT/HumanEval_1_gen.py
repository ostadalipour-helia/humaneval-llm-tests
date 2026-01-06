import unittest
from sut.problem_HumanEval_1 import separate_paren_groups

class Test_separate_paren_groups(unittest.TestCase):
    def test_multiple_groups_varying_nesting_and_spaces(self):
        # Normal case: Multiple groups with varying levels of nesting and spaces.
        paren_string = "( ) (( )) (( )( ))"
        expected_output = ["()", "(())", "(()())"]
        self.assertEqual(separate_paren_groups(paren_string), expected_output)

    def test_two_distinct_groups_deep_and_simple(self):
        # Normal case: Two distinct groups, one deeply nested, one simple.
        paren_string = "((())) ()"
        expected_output = ["((()))", "()"]
        self.assertEqual(separate_paren_groups(paren_string), expected_output)

    def test_single_group_many_internal_spaces(self):
        # Normal case: A single group with many internal spaces.
        paren_string = "( ( ( ) ) )"
        expected_output = ["((()))"]
        self.assertEqual(separate_paren_groups(paren_string), expected_output)

    def test_single_simple_group_no_spaces(self):
        # Edge case: Single, simple group with no spaces.
        paren_string = "()"
        expected_output = ["()"]
        self.assertEqual(separate_paren_groups(paren_string), expected_output)

    def test_multiple_groups_with_leading_trailing_inter_spaces(self):
        # Edge case: Multiple groups with leading, trailing, and inter-group spaces.
        paren_string = "   (   )    ( ( ) )   "
        expected_output = ["()", "(())"]
        self.assertEqual(separate_paren_groups(paren_string), expected_output)

    def test_empty_input_string(self):
        # Edge case: Empty input string should return an empty list.
        paren_string = ""
        expected_output = []
        self.assertEqual(separate_paren_groups(paren_string), expected_output)

    def test_input_only_spaces(self):
        # Edge case: Input string containing only spaces should return an empty list.
        paren_string = "      "
        expected_output = []
        self.assertEqual(separate_paren_groups(paren_string), expected_output)

    def test_error_unbalanced_top_level_group(self):
        # Error case: Input contains an unbalanced parenthesis group.
        # Behavior: Undefined behavior or raise an error (e.g., ValueError).
        with self.assertRaises(ValueError):
            separate_paren_groups("(( )) (")

    def test_error_unexpected_characters(self):
        # Error case: Input contains characters other than '(', ')', and spaces.
        # Behavior: Undefined behavior or raise an error (e.g., ValueError).
        with self.assertRaises(ValueError):
            separate_paren_groups("( [ ] )")

    def test_error_input_not_string(self):
        # Error case: Input is not a string (e.g., None).
        # Behavior: Raise a TypeError.
        with self.assertRaises(TypeError):
            separate_paren_groups(None)

    def test_error_unmatched_opening_parenthesis(self):
        # Error case: Input starts a group but does not close it.
        # Behavior: Undefined behavior or raise an error (e.g., ValueError).
        with self.assertRaises(ValueError):
            separate_paren_groups("((")

    def test_error_closing_before_opening(self):
        # Error case: Input contains a closing parenthesis before an opening one, violating balance.
        # Behavior: Undefined behavior or raise an error (e.g., ValueError).
        with self.assertRaises(ValueError):
            separate_paren_groups(")(")