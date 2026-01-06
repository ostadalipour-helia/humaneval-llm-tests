import unittest
from sut.problem_HumanEval_158 import find_max

class Test_find_max(unittest.TestCase):
    def test_normal_case_basic_unique_chars(self):
        words = ["name", "of", "string"]
        expected_output = "string"
        self.assertEqual(find_max(words), expected_output)

    def test_normal_case_different_unique_chars(self):
        words = ["name", "enam", "game"]
        expected_output = "enam"
        self.assertEqual(find_max(words), expected_output)

    def test_edge_case_empty_list(self):
        words = []
        expected_output = ""
        self.assertEqual(find_max(words), expected_output)

    def test_edge_case_single_word(self):
        words = ["hello"]
        expected_output = "hello"
        self.assertEqual(find_max(words), expected_output)

    def test_edge_case_all_same_unique_count_lexicographical_first(self):
        words = ["aaaaaaa", "bb" ,"cc"]
        expected_output = "aaaaaaa"
        self.assertEqual(find_max(words), expected_output)

    def test_edge_case_multiple_same_unique_count_lexicographical_first(self):
        words = ["abc", "bca", "cab"]
        expected_output = "abc"
        self.assertEqual(find_max(words), expected_output)

    def test_edge_case_complex_unique_chars(self):
        words = ["apple", "banana", "apricot"]
        expected_output = "apricot"
        self.assertEqual(find_max(words), expected_output)

    def test_edge_case_case_sensitivity_lexicographical(self):
        words = ["Aa", "aA"]
        expected_output = "Aa"
        self.assertEqual(find_max(words), expected_output)

    def test_error_input_not_list(self):
        words = "not_a_list"
        with self.assertRaises(TypeError):
            find_max(words)

    def test_error_list_contains_non_strings(self):
        words = ["hello", 123, "world"]
        with self.assertRaises(TypeError):
            find_max(words)