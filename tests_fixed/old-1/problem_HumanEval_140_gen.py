import unittest
from sut_llm.problem_HumanEval_140 import fix_spaces

class TestFixSpaces(unittest.TestCase):

    def test_no_spaces(self):
        self.assertEqual(fix_spaces("Example"), "Example")

    def test_single_space(self):
        self.assertEqual(fix_spaces("Example 1"), "Example_1")

    def test_leading_single_space(self):
        self.assertEqual(fix_spaces(" Example 2"), "_Example_2")

    def test_trailing_single_space(self):
        self.assertEqual(fix_spaces("Example 4 "), "Example_4_")

    def test_multiple_single_spaces(self):
        self.assertEqual(fix_spaces("Hello world again"), "Hello_world_again")

    def test_exactly_two_consecutive_spaces(self):
        # "more than 2 consecutive spaces" implies 2 spaces become two underscores
        self.assertEqual(fix_spaces("Two  spaces"), "Two__spaces")

    def test_three_consecutive_spaces(self):
        self.assertEqual(fix_spaces("Three   spaces"), "Three-spaces")

    def test_four_consecutive_spaces(self):
        self.assertEqual(fix_spaces("Four    spaces"), "Four-spaces")

    def test_mixed_single_and_consecutive_spaces(self):
        self.assertEqual(fix_spaces("Mix 1   2  3"), "Mix_1-2__3")

    def test_only_consecutive_spaces_more_than_two(self):
        self.assertEqual(fix_spaces("     "), "-") # Five spaces

if __name__ == '__main__':
    unittest.main()