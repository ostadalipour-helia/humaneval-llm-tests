import unittest
from sut.problem_HumanEval_125 import split_words

class Test_split_words(unittest.TestCase):

    def test_normal_whitespace_split(self):
        # Normal case: input with whitespace, should split by whitespace
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])

    def test_normal_comma_split(self):
        # Normal case: input with commas, no whitespace, should split by comma
        self.assertEqual(split_words("one,two,three"), ["one", "two", "three"])

    def test_normal_integer_count(self):
        # Normal case: input with no whitespace or commas, should count odd-indexed lowercase letters
        self.assertEqual(split_words("abcdef"), 3) # b(1), d(3), f(5)

    def test_edge_empty_string_count(self):
        # Edge case: empty string, no whitespace or commas, count should be 0
        self.assertEqual(split_words(""), 0)

    def test_edge_only_whitespace(self):
        # Edge case: string with only whitespace, should split into an empty list
        self.assertEqual(split_words("   "), [])

    def test_edge_only_commas(self):
        # Edge case: string with only commas, should split into empty strings
        self.assertEqual(split_words(",,,"), ["", "", "", ""])

    def test_edge_whitespace_leading_trailing_multiple(self):
        # Edge case: whitespace split with leading/trailing/multiple spaces
        self.assertEqual(split_words("  hello  world  "), ["hello", "world"])

    def test_edge_comma_empty_parts(self):
        # Edge case: comma split with empty parts due to multiple commas
        self.assertEqual(split_words("hello,,world"), ["hello", "", "world"])

    def test_edge_single_odd_char_count(self):
        # Edge case: single character, odd alphabetical order
        self.assertEqual(split_words("b"), 1) # b is 1st (odd)

    def test_edge_integer_count_xyz(self):
        # Edge case: integer count with mixed odd/even alphabetical order
        self.assertEqual(split_words("xyz"), 2) # x(23), z(25) are odd

    def test_error_none_input(self):
        # Error case: input is None, should raise TypeError
        with self.assertRaises(TypeError):
            split_words(None)

    def test_error_int_input(self):
        # Error case: input is an integer, should raise TypeError
        with self.assertRaises(TypeError):
            split_words(123)