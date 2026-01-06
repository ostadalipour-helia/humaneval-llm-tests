import unittest
from sut.problem_HumanEval_16 import count_distinct_characters

class Test_count_distinct_characters(unittest.TestCase):

    def test_normal_mixed_case_distinct(self):
        self.assertEqual(count_distinct_characters("xyzXYZ"), 3)

    def test_normal_repeated_and_mixed_case(self):
        self.assertEqual(count_distinct_characters("Jerry"), 4)

    def test_normal_with_spaces(self):
        self.assertEqual(count_distinct_characters("Hello World"), 8)

    def test_edge_empty_string(self):
        self.assertEqual(count_distinct_characters(""), 0)

    def test_edge_all_same_character_case_insensitive(self):
        self.assertEqual(count_distinct_characters("aaaaaA"), 1)

    def test_edge_single_character(self):
        self.assertEqual(count_distinct_characters("a"), 1)

    def test_edge_non_alphabetic(self):
        self.assertEqual(count_distinct_characters("123!@#"), 6)

    def test_edge_case_pairs(self):
        self.assertEqual(count_distinct_characters("AaBbCc"), 3)

    # Additional test cases to meet the 10-test requirement, re-using provided inputs
    def test_retest_normal_mixed_case_distinct(self):
        self.assertEqual(count_distinct_characters("xyzXYZ"), 3)

    def test_retest_normal_repeated_and_mixed_case(self):
        self.assertEqual(count_distinct_characters("Jerry"), 4)