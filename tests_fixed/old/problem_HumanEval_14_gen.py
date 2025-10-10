import unittest
from sut_llm.problem_HumanEval_14 import all_prefixes


class TestAllPrefixes(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(all_prefixes(""), [])

    def test_single_character_string(self):
        self.assertEqual(all_prefixes("a"), ["a"])

    def test_two_character_string(self):
        self.assertEqual(all_prefixes("ab"), ["a", "ab"])

    def test_three_character_string_from_docstring(self):
        self.assertEqual(all_prefixes("abc"), ["a", "ab", "abc"])

    def test_string_with_spaces(self):
        self.assertEqual(all_prefixes("hello world"), ["h", "he", "hel", "hell", "hello", "hello ", "hello w", "hello wo", "hello wor", "hello worl", "hello world"])

    def test_string_with_numbers(self):
        self.assertEqual(all_prefixes("123"), ["1", "12", "123"])

    def test_string_with_special_characters(self):
        self.assertEqual(all_prefixes("!@#"), ["!", "!@", "!@#"])

    def test_longer_string(self):
        self.assertEqual(all_prefixes("python"), ["p", "py", "pyt", "pyth", "pytho", "python"])

    def test_string_with_repeated_characters(self):
        self.assertEqual(all_prefixes("aaa"), ["a", "aa", "aaa"])

    def test_medium_length_string(self):
        self.assertEqual(all_prefixes("test"), ["t", "te", "tes", "test"])


if __name__ == '__main__':
    unittest.main()