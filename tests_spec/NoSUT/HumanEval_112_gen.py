import unittest
from sut.problem_HumanEval_112 import reverse_delete

class Test_reverse_delete(unittest.TestCase):

    def test_normal_basic_deletion(self):
        # Normal case: basic deletion, result is not a palindrome
        s = "abcde"
        c = "ae"
        expected_output = ("bcd", False)
        self.assertEqual(reverse_delete(s, c), expected_output)

    def test_normal_palindrome_result(self):
        # Normal case: deletion results in a palindrome
        s = "abcdedcba"
        c = "ab"
        expected_output = ("cdedc", True)
        self.assertEqual(reverse_delete(s, c), expected_output)

    def test_normal_hello_world_case(self):
        # Another normal case from spec
        s = "hello world"
        c = "o"
        expected_output = ("hell wrld", False)
        self.assertEqual(reverse_delete(s, c), expected_output)

    def test_edge_empty_s(self):
        # Edge case: s is an empty string
        s = ""
        c = "abc"
        expected_output = ("", True) # An empty string is considered a palindrome
        self.assertEqual(reverse_delete(s, c), expected_output)

    def test_edge_empty_c(self):
        # Edge case: c is an empty string (no characters deleted)
        s = "abc"
        c = ""
        expected_output = ("abc", False)
        self.assertEqual(reverse_delete(s, c), expected_output)

    def test_edge_s_palindrome_maintains_palindrome(self):
        # Edge case: s is a palindrome, deletion maintains palindrome property
        s = "racecar"
        c = "r"
        expected_output = ("aceca", True)
        self.assertEqual(reverse_delete(s, c), expected_output)

    def test_edge_s_palindrome_breaks_palindrome(self):
        # Edge case: s is a palindrome, but deletion breaks palindrome property
        s = "racecar"
        c = "e"
        expected_output = ("raccar", False)
        self.assertEqual(reverse_delete(s, c), expected_output)

    def test_edge_all_chars_deleted(self):
        # Edge case: All characters in s are deleted, resulting in an empty string
        s = "abc"
        c = "abc"
        expected_output = ("", True)
        self.assertEqual(reverse_delete(s, c), expected_output)

    def test_edge_single_char_s_not_deleted(self):
        # Edge case: s has one character, not in c
        s = "a"
        c = "b"
        expected_output = ("a", True)
        self.assertEqual(reverse_delete(s, c), expected_output)

    def test_edge_single_char_s_deleted(self):
        # Edge case: s has one character, which is deleted
        s = "a"
        c = "a"
        expected_output = ("", True)
        self.assertEqual(reverse_delete(s, c), expected_output)

    def test_error_s_not_string(self):
        # Error case: s is not a string
        s = 123
        c = "a"
        with self.assertRaises(TypeError):
            reverse_delete(s, c)

    def test_error_c_not_string(self):
        # Error case: c is not a string
        s = "abc"
        c = None
        with self.assertRaises(TypeError):
            reverse_delete(s, c)