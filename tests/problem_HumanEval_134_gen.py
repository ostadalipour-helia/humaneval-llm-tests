import unittest
from sut.problem_HumanEval_134 import check_if_last_char_is_a_letter

class TestCheckIfLastCharIsALetter(unittest.TestCase):

    def test_empty_string(self):
        # Edge case: empty string
        # Expected: False (no last character)
        self.assertEqual(check_if_last_char_is_a_letter(""), False)

    def test_single_letter_string(self):
        # Boundary case: string with a single alphabetical character
        # Expected: True (is a letter, not part of a word as no preceding char)
        self.assertEqual(check_if_last_char_is_a_letter("a"), True)

    def test_single_non_letter_string(self):
        # Edge case: string with a single non-alphabetical character (space)
        # Expected: False (not a letter)
        self.assertEqual(check_if_last_char_is_a_letter(" "), False)

    def test_last_char_is_letter_part_of_word(self):
        # Typical case: last char is a letter, but part of a multi-letter word
        # Example from docstring: "apple pie"
        # Expected: False (last char 'e' is alpha, but preceded by 'i')
        self.assertEqual(check_if_last_char_is_a_letter("apple pie"), False)

    def test_last_char_is_letter_not_part_of_word(self):
        # Typical case: last char is a letter, not part of a word (preceded by space)
        # Example from docstring: "apple pi e"
        # Expected: True (last char 'e' is alpha, preceded by ' ')
        self.assertEqual(check_if_last_char_is_a_letter("apple pi e"), True)

    def test_last_char_is_space(self):
        # Edge case: string ends with a space
        # Example from docstring: "apple pi e "
        # Expected: False (last char ' ' is not alpha)
        self.assertEqual(check_if_last_char_is_a_letter("apple pi e "), False)

    def test_last_char_is_digit(self):
        # Edge case: string ends with a digit
        # Expected: False (last char '1' is not alpha)
        self.assertEqual(check_if_last_char_is_a_letter("word1"), False)

    def test_boundary_two_chars_space_then_letter(self):
        # Boundary case: two characters, first is space, second is letter
        # Expected: True (last char 'a' is alpha, preceded by ' ')
        self.assertEqual(check_if_last_char_is_a_letter(" a"), True)

    def test_boundary_two_chars_letter_then_letter(self):
        # Boundary case: two characters, both letters
        # Expected: False (last char 'b' is alpha, but preceded by 'a')
        self.assertEqual(check_if_last_char_is_a_letter("ab"), False)

    def test_extreme_long_string_with_multiple_spaces_before_last_char(self):
        # Extreme case: long string with multiple spaces before the last letter
        # Expected: True (last char 'a' is alpha, preceded by ' ')
        self.assertEqual(check_if_last_char_is_a_letter("this is a very long string with   a"), True)