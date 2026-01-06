import unittest
from sut.problem_HumanEval_140 import fix_spaces

class Test_fix_spaces(unittest.TestCase):

    def test_no_spaces(self):
        self.assertEqual(fix_spaces("Example"), 'Example')

    def test_single_space(self):
        self.assertEqual(fix_spaces("Example 1"), 'Example_1')

    def test_leading_single_space(self):
        self.assertEqual(fix_spaces(" Example 2"), '_Example_2')

    def test_three_consecutive_spaces(self):
        self.assertEqual(fix_spaces("Example   3"), 'Example-3')

    def test_mixed_spaces(self):
        self.assertEqual(fix_spaces("  Test   String "), '__Test-String_')

    def test_empty_string(self):
        self.assertEqual(fix_spaces(""), '')

    def test_only_single_space(self):
        self.assertEqual(fix_spaces(" "), '_')

    def test_only_two_spaces(self):
        self.assertEqual(fix_spaces("  "), '_')

    def test_only_three_spaces(self):
        self.assertEqual(fix_spaces("   "), '-')

    def test_various_space_lengths(self):
        self.assertEqual(fix_spaces("A  B   C    D     E"), 'A__B-C-D-E')