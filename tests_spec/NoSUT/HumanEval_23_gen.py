import unittest
from sut.problem_HumanEval_23 import strlen

class Test_strlen(unittest.TestCase):
    def test_normal_alphanumeric_string(self):
        """
        A typical non-empty string with alphanumeric characters.
        Input: "abc", Expected Output: 3
        """
        self.assertEqual(strlen("abc"), 3)

    def test_normal_string_with_spaces(self):
        """
        A string containing spaces.
        Input: "hello world", Expected Output: 11
        """
        self.assertEqual(strlen("hello world"), 11)

    def test_normal_unicode_string(self):
        """
        A string containing Unicode characters.
        Input: "你好", Expected Output: 2
        """
        self.assertEqual(strlen("你好"), 2)

    def test_edge_empty_string(self):
        """
        An empty string.
        Input: "", Expected Output: 0
        """
        self.assertEqual(strlen(""), 0)

    def test_edge_single_character_string(self):
        """
        A string with a single character.
        Input: "a", Expected Output: 1
        """
        self.assertEqual(strlen("a"), 1)

    def test_edge_special_characters_string(self):
        """
        A string with special characters.
        Input: "!@#$", Expected Output: 4
        """
        self.assertEqual(strlen("!@#$"), 4)

    def test_error_input_integer(self):
        """
        Input is an integer instead of a string.
        Input: 123, Expected Exception: TypeError
        """
        with self.assertRaises(TypeError):
            strlen(123)

    def test_error_input_none(self):
        """
        Input is None instead of a string.
        Input: None, Expected Exception: TypeError
        """
        with self.assertRaises(TypeError):
            strlen(None)

    def test_error_input_list(self):
        """
        Input is a list instead of a string.
        Input: ["a", "b"], Expected Exception: TypeError
        """
        with self.assertRaises(TypeError):
            strlen(["a", "b"])