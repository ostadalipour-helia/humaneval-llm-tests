import unittest
from sut.problem_HumanEval_140 import fix_spaces

class TestFixSpaces(unittest.TestCase):

    def test_no_spaces(self):
        # Test case: String with no spaces.
        # Expected: Should remain unchanged.
        self.assertEqual(fix_spaces("HelloWorld"), "HelloWorld")

    def test_single_space(self):
        # Test case: String with a single space.
        # Expected: Single space replaced by underscore. (Boundary: 1 space)
        self.assertEqual(fix_spaces("Example 1"), "Example_1")

    def test_two_consecutive_spaces(self):
        # Test case: String with exactly two consecutive spaces.
        # Expected: Each space replaced by an underscore. (Boundary: 2 spaces)
        # Crucial for catching off-by-one errors like changing '>' to '>='
        self.assertEqual(fix_spaces("Two  Spaces"), "Two__Spaces")

    def test_three_consecutive_spaces(self):
        # Test case: String with exactly three consecutive spaces.
        # Expected: All three spaces replaced by a single hyphen. (Boundary: 3 spaces)
        # Crucial for catching off-by-one errors like changing '>' to '>='
        self.assertEqual(fix_spaces("Three   Spaces"), "Three-Spaces")

    def test_mixed_space_patterns(self):
        # Test case: String with a mix of single, two, and three consecutive spaces.
        # Expected: Correct replacement for each pattern. (Logic Mutation)
        self.assertEqual(fix_spaces("A B  C   D"), "A_B__C-D")

    def test_string_starts_and_ends_with_spaces(self):
        # Test case: String starting and ending with different space patterns.
        # Expected: Correct replacement at boundaries. (Edge Case)
        self.assertEqual(fix_spaces("  Example   3 "), "__Example-3_")

    def test_empty_string(self):
        # Test case: An empty input string.
        # Expected: Should return an empty string. (Edge Case)
        self.assertEqual(fix_spaces(""), "")

    def test_string_with_only_many_consecutive_spaces(self):
        # Test case: String consisting only of more than 2 consecutive spaces.
        # Expected: Replaced by a single hyphen. (Extreme Input)
        self.assertEqual(fix_spaces("     "), "-") # 5 spaces

    def test_string_with_only_two_consecutive_spaces(self):
        # Test case: String consisting only of exactly two consecutive spaces.
        # Expected: Replaced by two underscores. (Extreme Input / Edge Case)
        self.assertEqual(fix_spaces("  "), "__")

    def test_long_string_complex_patterns(self):
        # Test case: A longer string with various complex space patterns.
        # Expected: All patterns correctly handled. (Logic Mutation / Extreme Input)
        self.assertEqual(fix_spaces("  Start   Middle  End    Final"), "__Start-Middle__End-Final")