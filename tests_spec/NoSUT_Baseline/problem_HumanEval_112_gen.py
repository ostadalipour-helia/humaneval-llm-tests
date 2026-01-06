import unittest
import sut.problem_HumanEval_112 as mod

class TestHybrid(unittest.TestCase):
    def test_example_1_typical_non_palindrome(self):
            # Docstring example: typical input, deletion, non-palindrome result.
            # Covers: typical input, deletion logic, non-palindrome check.
            s = "abcde"
            c = "ae"
            expected_output = ('bcd', False)
            self.assertEqual(mod.reverse_delete(s, c), expected_output)

    def test_example_2_single_char_deletion(self):
            # Docstring example: typical input, single character deletion, non-palindrome result.
            # Covers: single character in 'c', deletion logic, non-palindrome check.
            s = "abcdef"
            c = "b"
            expected_output = ('acdef', False)
            self.assertEqual(mod.reverse_delete(s, c), expected_output)

    def test_example_3_typical_palindrome(self):
            # Docstring example: typical input, multiple char deletion, palindrome result.
            # Covers: multiple characters in 'c', deletion logic, palindrome check.
            s = "abcdedcba"
            c = "ab"
            expected_output = ('cdedc', True)
            self.assertEqual(mod.reverse_delete(s, c), expected_output)

    def test_empty_s_string(self):
            # Edge case: 's' is an empty string. An empty string is a palindrome.
            # Covers: empty input string 's', boundary condition.
            s = ""
            c = "abc"
            expected_output = ('', True)
            self.assertEqual(mod.reverse_delete(s, c), expected_output)

    def test_empty_c_string(self):
            # Edge case: 'c' is an empty string. No characters should be deleted.
            # 's' is a palindrome.
            # Covers: empty deletion set 'c', boundary condition, existing palindrome.
            s = "racecar"
            c = ""
            expected_output = ('racecar', True)
            self.assertEqual(mod.reverse_delete(s, c), expected_output)

    def test_all_chars_deleted_resulting_empty(self):
            # Boundary case: all characters in 's' are present in 'c', resulting in an empty string.
            # An empty string is a palindrome.
            # Covers: all deletions, resulting empty string, boundary.
            s = "aaaaa"
            c = "a"
            expected_output = ('', True)
            self.assertEqual(mod.reverse_delete(s, c), expected_output)

    def test_single_char_s_deleted(self):
            # Edge/Boundary case: 's' has one character, which is deleted.
            # Resulting string is empty, which is a palindrome.
            # Covers: single character 's', complete deletion, off-by-one.
            s = "x"
            c = "x"
            expected_output = ('', True)
            self.assertEqual(mod.reverse_delete(s, c), expected_output)

    def test_single_char_s_not_deleted(self):
            # Edge/Boundary case: 's' has one character, which is not deleted.
            # Resulting string is single character, which is a palindrome.
            # Covers: single character 's', no deletion, off-by-one.
            s = "y"
            c = "z"
            expected_output = ('y', True)
            self.assertEqual(mod.reverse_delete(s, c), expected_output)

    def test_palindrome_s_remains_palindrome_after_deletion(self):
            # Logic mutation test: 's' is a palindrome, 'c' deletes characters, result is still a palindrome.
            # Covers: palindrome logic, deletion affecting boundaries of palindrome.
            s = "madam"
            c = "m"
            expected_output = ('ada', True)
            self.assertEqual(mod.reverse_delete(s, c), expected_output)

    def test_non_palindrome_s_becomes_palindrome_after_deletion(self):
            # Logic mutation test: 's' is not a palindrome, 'c' deletes characters, result becomes a palindrome.
            # Covers: deletion logic transforming a non-palindrome into a palindrome.
            s = "racecarx"
            c = "x"
            expected_output = ('racecar', True)
            self.assertEqual(mod.reverse_delete(s, c), expected_output)

    def test_normal_basic_deletion(self):
            # Normal case: basic deletion, result is not a palindrome
            s = "abcde"
            c = "ae"
            expected_output = ("bcd", False)
            self.assertEqual(mod.reverse_delete(s, c), expected_output)

    def test_normal_palindrome_result(self):
            # Normal case: deletion results in a palindrome
            s = "abcdedcba"
            c = "ab"
            expected_output = ("cdedc", True)
            self.assertEqual(mod.reverse_delete(s, c), expected_output)

    def test_normal_hello_world_case(self):
            # Another normal case from spec
            s = "hello world"
            c = "o"
            expected_output = ("hell wrld", False)
            self.assertEqual(mod.reverse_delete(s, c), expected_output)

    def test_edge_empty_s(self):
            # Edge case: s is an empty string
            s = ""
            c = "abc"
            expected_output = ("", True) # An empty string is considered a palindrome
            self.assertEqual(mod.reverse_delete(s, c), expected_output)

    def test_edge_empty_c(self):
            # Edge case: c is an empty string (no characters deleted)
            s = "abc"
            c = ""
            expected_output = ("abc", False)
            self.assertEqual(mod.reverse_delete(s, c), expected_output)

    def test_edge_s_palindrome_maintains_palindrome(self):
            # Edge case: s is a palindrome, deletion maintains palindrome property
            s = "racecar"
            c = "r"
            expected_output = ("aceca", True)
            self.assertEqual(mod.reverse_delete(s, c), expected_output)

    def test_edge_s_palindrome_breaks_palindrome(self):
            # Edge case: s is a palindrome, but deletion breaks palindrome property
            s = "racecar"
            c = "e"
            expected_output = ("raccar", False)
            self.assertEqual(mod.reverse_delete(s, c), expected_output)

    def test_edge_all_chars_deleted(self):
            # Edge case: All characters in s are deleted, resulting in an empty string
            s = "abc"
            c = "abc"
            expected_output = ("", True)
            self.assertEqual(mod.reverse_delete(s, c), expected_output)

    def test_edge_single_char_s_not_deleted(self):
            # Edge case: s has one character, not in c
            s = "a"
            c = "b"
            expected_output = ("a", True)
            self.assertEqual(mod.reverse_delete(s, c), expected_output)

    def test_edge_single_char_s_deleted(self):
            # Edge case: s has one character, which is deleted
            s = "a"
            c = "a"
            expected_output = ("", True)
            self.assertEqual(mod.reverse_delete(s, c), expected_output)

    def test_error_s_not_string(self):
            # Error case: s is not a string
            s = 123
            c = "a"
            with self.assertRaises(TypeError):
                mod.reverse_delete(s, c)

    def test_error_c_not_string(self):
            # Error case: c is not a string
            s = "abc"
            c = None
            with self.assertRaises(TypeError):
                mod.reverse_delete(s, c)

