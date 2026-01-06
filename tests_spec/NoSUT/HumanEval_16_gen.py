import unittest
from sut.problem_HumanEval_16 import count_distinct_characters

class Test_count_distinct_characters(unittest.TestCase):
    def test_normal_mixed_case_distinct(self):
        """
        String with mixed case characters that are distinct when case is ignored.
        Input: "xyzXYZ", Expected Output: 3
        """
        self.assertEqual(count_distinct_characters("xyzXYZ"), 3)

    def test_normal_repeated_mixed_case(self):
        """
        String with some repeated characters and mixed case.
        Input: "Jerry", Expected Output: 4
        """
        self.assertEqual(count_distinct_characters("Jerry"), 4)

    def test_normal_sentence_with_space(self):
        """
        String with spaces and common words, testing case-insensitivity and character set.
        Input: "Hello World", Expected Output: 8
        """
        self.assertEqual(count_distinct_characters("Hello World"), 8)

    def test_edge_empty_string(self):
        """
        Empty string should have zero distinct characters.
        Input: "", Expected Output: 0
        """
        self.assertEqual(count_distinct_characters(""), 0)

    def test_edge_all_same_case_insensitive(self):
        """
        String with all characters being the same, regardless of case.
        Input: "aaaaaA", Expected Output: 1
        """
        self.assertEqual(count_distinct_characters("aaaaaA"), 1)

    def test_edge_single_character(self):
        """
        String with a single character.
        Input: "a", Expected Output: 1
        """
        self.assertEqual(count_distinct_characters("a"), 1)

    def test_edge_non_alphabetic_characters(self):
        """
        String with only non-alphabetic characters.
        Input: "123!@#", Expected Output: 6
        """
        self.assertEqual(count_distinct_characters("123!@#"), 6)

    def test_edge_pairs_different_case(self):
        """
        String with pairs of same characters in different cases.
        Input: "AaBbCc", Expected Output: 3
        """
        self.assertEqual(count_distinct_characters("AaBbCc"), 3)

    def test_error_integer_input(self):
        """
        Input is an integer instead of a string.
        Input: 123, Expected Exception: TypeError
        """
        with self.assertRaises(TypeError):
            count_distinct_characters(123)

    def test_error_none_input(self):
        """
        Input is None instead of a string.
        Input: None, Expected Exception: TypeError
        """
        with self.assertRaises(TypeError):
            count_distinct_characters(None)

    def test_error_list_input(self):
        """
        Input is a list instead of a string.
        Input: ["a", "b", "c"], Expected Exception: TypeError
        """
        with self.assertRaises(TypeError):
            count_distinct_characters(["a", "b", "c"])