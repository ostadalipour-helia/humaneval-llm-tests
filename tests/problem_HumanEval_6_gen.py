import unittest
from sut.problem_HumanEval_6 import parse_nested_parens

class TestParseNestedParens(unittest.TestCase):

    def test_docstring_example(self):
        """
        Test case from the function's docstring.
        Covers: Typical input, multiple groups, varying depths.
        """
        self.assertListEqual(parse_nested_parens('(()()) ((())) () ((())()())'), [2, 3, 1, 3])

    def test_empty_string(self):
        """
        Edge case: Empty input string.
        Covers: Edge case (empty collection), off-by-one (zero groups).
        """
        self.assertListEqual(parse_nested_parens(''), [])

    def test_single_group_min_depth(self):
        """
        Boundary case: Single group with minimum possible nesting depth.
        Covers: Boundary (min depth), edge case (single element group).
        """
        self.assertListEqual(parse_nested_parens('()'), [1])

    def test_single_group_deep_nesting(self):
        """
        Boundary case: Single group with significant nesting depth.
        Covers: Boundary (max depth for a single group), extreme input.
        """
        self.assertListEqual(parse_nested_parens('((((()))))'), [5])

    def test_multiple_groups_varying_depths(self):
        """
        Typical input: Multiple groups with increasing nesting depths.
        Covers: Typical input, multiple groups, varying depths.
        """
        self.assertListEqual(parse_nested_parens('() (()) ((()))'), [1, 2, 3])

    def test_multiple_groups_same_depth(self):
        """
        Logic mutation test: Ensures each group's depth is calculated independently.
        Covers: Logic mutation (independent processing), typical input.
        """
        self.assertListEqual(parse_nested_parens('(()()) (()()) (()())'), [2, 2, 2])

    def test_complex_interleaved_nesting(self):
        """
        Extreme input: A single group with complex, interleaved nesting.
        Covers: Extreme/unusual input, complex logic.
        """
        self.assertListEqual(parse_nested_parens('((()())(()))'), [3])

    def test_long_string_many_groups(self):
        """
        Extreme input: A long string with many groups and varying depths.
        Covers: Extreme input, boundary (number of groups).
        """
        self.assertListEqual(parse_nested_parens('() (()) ((())) (((()))) ((((()))))'), [1, 2, 3, 4, 5])

    def test_group_with_max_depth_at_end(self):
        """
        Logic mutation test: Ensures max_depth is correctly updated even if the peak is late.
        Covers: Logic mutation (max depth update), boundary (order of depths).
        """
        self.assertListEqual(parse_nested_parens('((())) (()()) ()'), [3, 2, 1])

    def test_string_with_only_spaces(self):
        """
        Edge case: Input string contains only whitespace.
        Covers: Edge case (whitespace only), off-by-one (zero groups).
        """
        self.assertListEqual(parse_nested_parens('   '), [])

if __name__ == '__main__':
    unittest.main()