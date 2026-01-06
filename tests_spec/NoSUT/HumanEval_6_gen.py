import unittest
from sut.problem_HumanEval_6 import parse_nested_parens

class Test_parse_nested_parens(unittest.TestCase):
    def test_multiple_varying_depths(self):
        # Normal case: Multiple groups with varying nesting depths.
        input_string = "(()()) ((())) () ((())()())"
        expected_output = [2, 3, 1, 3]
        self.assertEqual(parse_nested_parens(input_string), expected_output)

    def test_single_group_depth_one(self):
        # Normal case: A single group with one level of nesting.
        input_string = "()"
        expected_output = [1]
        self.assertEqual(parse_nested_parens(input_string), expected_output)

    def test_empty_string(self):
        # Edge case: An empty input string.
        input_string = ""
        expected_output = []
        self.assertEqual(parse_nested_parens(input_string), expected_output)

    def test_only_spaces(self):
        # Edge case: An input string containing only spaces.
        input_string = "   "
        expected_output = []
        self.assertEqual(parse_nested_parens(input_string), expected_output)

    def test_deeply_nested_single_group(self):
        # Edge case: A single, deeply nested group.
        input_string = "((((()))))"
        expected_output = [5]
        self.assertEqual(parse_nested_parens(input_string), expected_output)

    def test_multiple_spaces_between_groups(self):
        # Edge case: Multiple groups separated by more than one space.
        input_string = "()  (())"
        expected_output = [1, 2]
        self.assertEqual(parse_nested_parens(input_string), expected_output)

    def test_single_complex_group(self):
        # Edge case: A single group that is not just a simple pair.
        input_string = "(()())"
        expected_output = [2]
        self.assertEqual(parse_nested_parens(input_string), expected_output)

    def test_error_non_string_input(self):
        # Error case: Input is not of type string.
        with self.assertRaises(TypeError):
            parse_nested_parens(123)

    def test_error_invalid_character_in_group(self):
        # Error case: A group contains characters other than '(' or ')'.
        with self.assertRaises(ValueError):
            parse_nested_parens("(()x())")

    def test_error_unbalanced_open_paren(self):
        # Error case: A group is not a validly balanced set of parentheses (unmatched opening parenthesis).
        with self.assertRaises(ValueError):
            parse_nested_parens("(()")

    def test_error_unbalanced_close_paren(self):
        # Error case: A group is not a validly balanced set of parentheses (unmatched closing parenthesis).
        with self.assertRaises(ValueError):
            parse_nested_parens("())")

    def test_multiple_groups_same_depth(self):
        # Normal case: Multiple groups, all with the same nesting depth.
        input_string = "() () ()"
        expected_output = [1, 1, 1]
        self.assertEqual(parse_nested_parens(input_string), expected_output)