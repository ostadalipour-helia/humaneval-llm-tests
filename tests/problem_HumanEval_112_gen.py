import unittest
from sut.problem_HumanEval_112 import reverse_delete

class TestReverseDelete(unittest.TestCase):

    def test_example_1_typical_non_palindrome(self):
        # Docstring example: typical input, deletion, non-palindrome result.
        # Covers: typical input, deletion logic, non-palindrome check.
        s = "abcde"
        c = "ae"
        expected_output = ('bcd', False)
        self.assertEqual(reverse_delete(s, c), expected_output)

    def test_example_2_single_char_deletion(self):
        # Docstring example: typical input, single character deletion, non-palindrome result.
        # Covers: single character in 'c', deletion logic, non-palindrome check.
        s = "abcdef"
        c = "b"
        expected_output = ('acdef', False)
        self.assertEqual(reverse_delete(s, c), expected_output)

    def test_example_3_typical_palindrome(self):
        # Docstring example: typical input, multiple char deletion, palindrome result.
        # Covers: multiple characters in 'c', deletion logic, palindrome check.
        s = "abcdedcba"
        c = "ab"
        expected_output = ('cdedc', True)
        self.assertEqual(reverse_delete(s, c), expected_output)

    def test_empty_s_string(self):
        # Edge case: 's' is an empty string. An empty string is a palindrome.
        # Covers: empty input string 's', boundary condition.
        s = ""
        c = "abc"
        expected_output = ('', True)
        self.assertEqual(reverse_delete(s, c), expected_output)

    def test_empty_c_string(self):
        # Edge case: 'c' is an empty string. No characters should be deleted.
        # 's' is a palindrome.
        # Covers: empty deletion set 'c', boundary condition, existing palindrome.
        s = "racecar"
        c = ""
        expected_output = ('racecar', True)
        self.assertEqual(reverse_delete(s, c), expected_output)

    def test_all_chars_deleted_resulting_empty(self):
        # Boundary case: all characters in 's' are present in 'c', resulting in an empty string.
        # An empty string is a palindrome.
        # Covers: all deletions, resulting empty string, boundary.
        s = "aaaaa"
        c = "a"
        expected_output = ('', True)
        self.assertEqual(reverse_delete(s, c), expected_output)

    def test_single_char_s_deleted(self):
        # Edge/Boundary case: 's' has one character, which is deleted.
        # Resulting string is empty, which is a palindrome.
        # Covers: single character 's', complete deletion, off-by-one.
        s = "x"
        c = "x"
        expected_output = ('', True)
        self.assertEqual(reverse_delete(s, c), expected_output)

    def test_single_char_s_not_deleted(self):
        # Edge/Boundary case: 's' has one character, which is not deleted.
        # Resulting string is single character, which is a palindrome.
        # Covers: single character 's', no deletion, off-by-one.
        s = "y"
        c = "z"
        expected_output = ('y', True)
        self.assertEqual(reverse_delete(s, c), expected_output)

    def test_palindrome_s_remains_palindrome_after_deletion(self):
        # Logic mutation test: 's' is a palindrome, 'c' deletes characters, result is still a palindrome.
        # Covers: palindrome logic, deletion affecting boundaries of palindrome.
        s = "madam"
        c = "m"
        expected_output = ('ada', True)
        self.assertEqual(reverse_delete(s, c), expected_output)

    def test_non_palindrome_s_becomes_palindrome_after_deletion(self):
        # Logic mutation test: 's' is not a palindrome, 'c' deletes characters, result becomes a palindrome.
        # Covers: deletion logic transforming a non-palindrome into a palindrome.
        s = "racecarx"
        c = "x"
        expected_output = ('racecar', True)
        self.assertEqual(reverse_delete(s, c), expected_output)