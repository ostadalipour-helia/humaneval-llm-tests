import unittest
from sut.problem_HumanEval_18 import how_many_times

class Test_how_many_times(unittest.TestCase):

    def test_multiple_non_overlapping_occurrences(self):
        # Normal case: Multiple non-overlapping occurrences.
        self.assertEqual(how_many_times("abcabc", "abc"), 2)

    def test_multiple_overlapping_occurrences(self):
        # Normal case: Multiple overlapping occurrences.
        self.assertEqual(how_many_times("aaaaa", "aa"), 4)

    def test_standard_single_char_substring(self):
        # Normal case: Standard case with single character substring.
        self.assertEqual(how_many_times("hello world", "o"), 2)

    def test_empty_original_string(self):
        # Edge case: Empty original string, non-empty substring.
        self.assertEqual(how_many_times("", "a"), 0)

    def test_substring_longer_than_string(self):
        # Edge case: Substring is longer than the original string.
        self.assertEqual(how_many_times("abc", "abcd"), 0)

    def test_substring_not_found(self):
        # Edge case: Substring not found in the original string.
        self.assertEqual(how_many_times("abc", "d"), 0)

    def test_string_and_substring_identical(self):
        # Edge case: Original string and substring are identical.
        self.assertEqual(how_many_times("abc", "abc"), 1)

    def test_empty_substring_non_empty_string(self):
        # Edge case: Substring is empty, non-empty original string (len(string) + 1).
        self.assertEqual(how_many_times("test", ""), 5)

    def test_both_empty_strings(self):
        # Edge case: Both original string and substring are empty (len(string) + 1).
        self.assertEqual(how_many_times("", ""), 1)

    def test_string_not_str_type_error(self):
        # Error case: Input 'string' is not a string.
        with self.assertRaises(TypeError):
            how_many_times(123, "a")

    def test_substring_not_str_type_error(self):
        # Error case: Input 'substring' is not a string.
        with self.assertRaises(TypeError):
            how_many_times("abc", None)