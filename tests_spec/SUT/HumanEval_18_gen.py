import unittest
from sut.problem_HumanEval_18 import how_many_times

class Test_how_many_times(unittest.TestCase):

    def test_multiple_non_overlapping(self):
        self.assertEqual(how_many_times("abcabc", "abc"), 2)

    def test_multiple_overlapping(self):
        self.assertEqual(how_many_times("aaaaa", "aa"), 4)
        self.assertEqual(how_many_times("banana", "ana"), 2)

    def test_single_character_substring(self):
        self.assertEqual(how_many_times("hello world", "o"), 2)

    def test_string_composed_of_substring(self):
        self.assertEqual(how_many_times("aaa", "a"), 3)
        self.assertEqual(how_many_times("aaaa", "aa"), 3)

    def test_empty_string(self):
        self.assertEqual(how_many_times("", "a"), 0)

    def test_substring_longer_than_string(self):
        self.assertEqual(how_many_times("abc", "abcd"), 0)

    def test_substring_not_found(self):
        self.assertEqual(how_many_times("abc", "d"), 0)

    def test_identical_string_and_substring(self):
        self.assertEqual(how_many_times("abc", "abc"), 1)

    def test_empty_substring(self):
        self.assertEqual(how_many_times("test", ""), 5)

    def test_both_strings_empty(self):
        self.assertEqual(how_many_times("", ""), 1)