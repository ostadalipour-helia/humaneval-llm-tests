import unittest
from sut.problem_HumanEval_6 import parse_nested_parens

class TestParseNestedParens(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(parse_nested_parens('(()()) ((())) () ((())()())'), [2, 3, 1, 3])

    def test_single_group_level_1(self):
        self.assertEqual(parse_nested_parens('()'), [1])

    def test_single_group_level_2(self):
        self.assertEqual(parse_nested_parens('(())'), [2])

    def test_single_group_level_3(self):
        self.assertEqual(parse_nested_parens('((()))'), [3])

    def test_single_group_complex_level_2(self):
        self.assertEqual(parse_nested_parens('(()())'), [2])

    def test_single_group_complex_level_3(self):
        self.assertEqual(parse_nested_parens('((()()))'), [3])

    def test_multiple_groups_simple(self):
        self.assertEqual(parse_nested_parens('() () ()'), [1, 1, 1])

    def test_multiple_groups_mixed_levels(self):
        self.assertEqual(parse_nested_parens('(()) () ((()))'), [2, 1, 3])

    def test_multiple_groups_complex_mixed(self):
        self.assertEqual(parse_nested_parens('(()()) ((()())) ()'), [2, 3, 1])

    def test_single_group_deep_nesting(self):
        self.assertEqual(parse_nested_parens('((((()))))'), [4])