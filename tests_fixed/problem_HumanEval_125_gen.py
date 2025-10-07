import unittest
from sut_llm.problem_HumanEval_125 import split_words

class TestSplitWords(unittest.TestCase):

    def test_split_whitespace_basic(self):
        # Test case for splitting on a single whitespace
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])

    def test_split_whitespace_multiple_spaces(self):
        # Test case for splitting on multiple and mixed whitespace characters
        self.assertEqual(split_words("  Python   is  fun!  "), ["Python", "is", "fun!"])

    def test_split_whitespace_tabs_newlines(self):
        # Test case for splitting on tabs and newlines
        self.assertEqual(split_words("Line1\tLine2\nLine3"), ["Line1", "Line2", "Line3"])

    def test_split_comma_basic(self):
        # Test case for splitting on a single comma when no whitespace is present
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])

    def test_split_comma_multiple(self):
        # Test case for splitting on multiple commas
        self.assertEqual(split_words("apple,banana,orange"), ["apple", "banana", "orange"])

    def test_split_comma_with_empty_parts(self):
        # Test case for splitting on commas resulting in empty strings (e.g., "a,,b")
        self.assertEqual(split_words("a,,b"), ["a", "", "b"])

    def test_count_odd_order_basic(self):
        # Test case for counting odd-ordered lowercase letters (b=1, d=3, f=5)
        self.assertEqual(split_words("abcdef"), 3)

    def test_count_odd_order_no_odd_letters(self):
        # Test case where all lowercase letters have even order (a=0, c=2, e=4)
        self.assertEqual(split_words("acegik"), 0)

    def test_count_odd_order_mixed_case_and_symbols(self):
        # Test case with mixed case letters, numbers, and symbols; only lowercase count
        # 'p' (15), 'r' (17), 'r' (17), 'n' (13) are odd
        self.assertEqual(split_words("programming123!@#"), 4)

    def test_count_odd_order_empty_string(self):
        # Test case for an empty string, should result in 0 odd-ordered letters
        self.assertEqual(split_words(""), 0)

if __name__ == '__main__':
    unittest.main()