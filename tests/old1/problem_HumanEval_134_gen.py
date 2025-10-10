import unittest
from sut.problem_HumanEval_134 import check_if_last_char_is_a_letter

class TestCheckIfLastCharIsALetter(unittest.TestCase):

    def test_empty_string(self):
        self.assertFalse(check_if_last_char_is_a_letter(""))

    def test_example_part_of_word(self):
        self.assertFalse(check_if_last_char_is_a_letter("apple pie"))

    def test_example_not_part_of_word(self):
        self.assertTrue(check_if_last_char_is_a_letter("apple pi e"))

    def test_example_ends_with_space(self):
        self.assertFalse(check_if_last_char_is_a_letter("apple pi e "))

    def test_single_lowercase_letter(self):
        self.assertTrue(check_if_last_char_is_a_letter("a"))

    def test_single_uppercase_letter(self):
        self.assertTrue(check_if_last_char_is_a_letter("Z"))

    def test_ends_with_digit(self):
        self.assertFalse(check_if_last_char_is_a_letter("word1"))

    def test_ends_with_symbol(self):
        self.assertFalse(check_if_last_char_is_a_letter("word!"))

    def test_multiple_words_last_is_part_of_word(self):
        self.assertFalse(check_if_last_char_is_a_letter("hello world"))

    def test_multiple_words_last_is_single_letter_word(self):
        self.assertTrue(check_if_last_char_is_a_letter("hello w o r l d"))

if __name__ == '__main__':
    unittest.main()