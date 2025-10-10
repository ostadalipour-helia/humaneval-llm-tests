import unittest
from sut.problem_HumanEval_18 import how_many_times

class TestHowManyTimes(unittest.TestCase):

    def test_empty_string_non_empty_substring(self):
        # Boundary Test: String is empty.
        # Edge Case: Empty collection for the main string.
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_substring_longer_than_string(self):
        # Boundary Test: Substring is longer than the main string.
        self.assertEqual(how_many_times('abc', 'abcd'), 0)

    def test_single_char_string_and_substring_match(self):
        # Edge Case: Single element string and substring, perfect match.
        # Boundary Test: Smallest possible matching string/substring.
        self.assertEqual(how_many_times('a', 'a'), 1)

    def test_single_char_string_and_substring_no_match(self):
        # Edge Case: Single element string and substring, no match.
        self.assertEqual(how_many_times('a', 'b'), 0)

    def test_multiple_non_overlapping_occurrences(self):
        # Typical Input: Multiple distinct occurrences.
        # Logic Mutation Test: Ensures non-overlapping counts are correct.
        self.assertEqual(how_many_times('ababab', 'ab'), 3)

    def test_multiple_overlapping_occurrences_simple(self):
        # Typical Input: Multiple overlapping occurrences.
        # Off-by-One Error Test: Crucial for `n-m+1` type logic.
        # 'aaaaa' contains 'aa' at indices 0, 1, 2, 3.
        self.assertEqual(how_many_times('aaaaa', 'aa'), 4)

    def test_string_and_substring_are_identical(self):
        # Boundary Test: String is exactly the same as the substring.
        self.assertEqual(how_many_times('test', 'test'), 1)

    def test_no_occurrences_at_all(self):
        # Typical Input: Substring not found anywhere.
        # Logic Mutation Test: Verifies the 'not found' return path.
        self.assertEqual(how_many_times('hello world', 'xyz'), 0)

    def test_long_string_single_char_substring_many_occurrences(self):
        # Extreme Input: Long string, single character substring, many occurrences.
        # Off-by-One Error Test: Ensures full iteration and correct count for simple, repetitive patterns.
        self.assertEqual(how_many_times('xxxxxxxxxxxxxxxxxxxx', 'x'), 20)

    def test_complex_string_with_multiple_overlapping_patterns(self):
        # Extreme Input: Complex string with multiple instances of a substring, some potentially overlapping within larger patterns.
        # Off-by-One Error Test: Ensures all occurrences are found in a more complex scenario.
        # 'banana' has 'ana' twice. 'banana_banana_banana' has 'ana' 6 times.
        self.assertEqual(how_many_times('banana_banana_banana', 'ana'), 6)