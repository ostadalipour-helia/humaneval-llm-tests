import unittest
from sut_llm.problem_HumanEval_16 import count_distinct_characters

class TestCountDistinctCharacters(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_distinct_characters(""), 0)

    def test_all_same_lowercase(self):
        self.assertEqual(count_distinct_characters("aaaaa"), 1)

    def test_all_same_uppercase(self):
        self.assertEqual(count_distinct_characters("AAAAA"), 1)

    def test_all_distinct_lowercase(self):
        self.assertEqual(count_distinct_characters("abcdef"), 6)

    def test_all_distinct_uppercase(self):
        self.assertEqual(count_distinct_characters("ABCDEF"), 6)

    def test_mixed_case_duplicates_example1(self):
        self.assertEqual(count_distinct_characters("xyzXYZ"), 3)

    def test_mixed_case_duplicates_example2(self):
        self.assertEqual(count_distinct_characters("Jerry"), 4)

    def test_single_character(self):
        self.assertEqual(count_distinct_characters("z"), 1)

    def test_string_with_numbers_and_symbols(self):
        self.assertEqual(count_distinct_characters("123!@#abcABC"), 9)

    def test_string_with_spaces_and_mixed_case(self):
        self.assertEqual(count_distinct_characters("Hello World"), 8)