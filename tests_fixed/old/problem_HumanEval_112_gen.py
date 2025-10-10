import unittest
from sut_llm.problem_HumanEval_112 import reverse_delete

class TestReverseDelete(unittest.TestCase):

    def test_example_1(self):
        # Docstring example: s = "abcde", c = "ae" -> ('bcd', False)
        self.assertEqual(reverse_delete("abcde", "ae"), ('bcd', False))

    def test_example_2(self):
        # Docstring example: s = "abcdef", c = "b" -> ('acdef', False)
        self.assertEqual(reverse_delete("abcdef", "b"), ('acdef', False))

    def test_example_3(self):
        # Docstring example: s = "abcdedcba", c = "ab" -> ('cdedc', True)
        self.assertEqual(reverse_delete("abcdedcba", "ab"), ('cdedc', True))

    def test_empty_s(self):
        # Test with an empty string s
        self.assertEqual(reverse_delete("", "abc"), ('', True))

    def test_empty_c(self):
        # Test with an empty string c, no characters should be deleted
        self.assertEqual(reverse_delete("madam", ""), ('madam', True))

    def test_all_chars_deleted(self):
        # Test where all characters in s are deleted, resulting in an empty string
        self.assertEqual(reverse_delete("aaaaa", "a"), ('', True))

    def test_result_is_odd_palindrome(self):
        # Test where deletion results in an odd-length palindrome
        self.assertEqual(reverse_delete("racecar", "r"), ('aceca', True))

    def test_result_is_even_palindrome(self):
        # Test where deletion results in an even-length palindrome
        self.assertEqual(reverse_delete("noon", "n"), ('oo', True))

    def test_result_is_not_palindrome(self):
        # Test where deletion results in a non-palindrome string
        self.assertEqual(reverse_delete("programming", "g"), ('prorammin', False))

    def test_c_has_chars_not_in_s(self):
        # Test where c contains characters not present in s, and s is not a palindrome
        # The character 'y' from "python" is present in "xyz", so it should be deleted.
        self.assertEqual(reverse_delete("python", "xyz"), ('pthon', False))

if __name__ == '__main__':
    unittest.main()