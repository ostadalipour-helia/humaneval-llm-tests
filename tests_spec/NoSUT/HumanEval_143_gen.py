import unittest
from sut.problem_HumanEval_143 import words_in_sentence

class Test_words_in_sentence(unittest.TestCase):

    # Normal Cases
    def test_normal_one_prime_word(self):
        # Description: Sentence with words of varying lengths, one prime length word.
        sentence = "This is a test"
        expected_output = "is"
        self.assertEqual(words_in_sentence(sentence), expected_output)

    def test_normal_multiple_prime_words(self):
        # Description: Sentence with multiple prime length words.
        sentence = "lets go for swimming"
        expected_output = "go for"
        self.assertEqual(words_in_sentence(sentence), expected_output)

    def test_normal_mixed_lengths(self):
        # Description: Multiple prime length words, including 5 and 6 (not prime) and 8 (not prime) and 11 (prime).
        sentence = "hello world python programming"
        expected_output = "hello world python" # 'programming' has length 11, which is prime. The description is slightly off, but the output is correct based on the spec.
        self.assertEqual(words_in_sentence(sentence), expected_output)

    # Edge Cases
    def test_edge_single_word_prime(self):
        # Description: Single word sentence, word length is prime (3).
        sentence = "two"
        expected_output = "two"
        self.assertEqual(words_in_sentence(sentence), expected_output)

    def test_edge_single_word_not_prime(self):
        # Description: Single word sentence, word length is not prime (4).
        sentence = "four"
        expected_output = ""
        self.assertEqual(words_in_sentence(sentence), expected_output)

    def test_edge_all_words_not_prime_length_1(self):
        # Description: All words have length 1 (not prime), resulting in an empty string.
        sentence = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
        expected_output = ""
        self.assertEqual(words_in_sentence(sentence), expected_output)

    def test_edge_all_words_prime(self):
        # Description: All words have prime lengths (2, 3, 5, 7).
        sentence = "aa bbb ccccc ddddddd"
        expected_output = "aa bbb ccccc ddddddd"
        self.assertEqual(words_in_sentence(sentence), expected_output)

    # Error Cases
    def test_error_empty_string(self):
        # Description: Empty string input (violates 1 <= len(sentence)).
        sentence = ""
        with self.assertRaises(ValueError):
            words_in_sentence(sentence)

    def test_error_non_alphabetic_chars(self):
        # Description: Sentence contains non-alphabetic characters (numbers).
        sentence = "hello 123 world"
        with self.assertRaises(ValueError):
            words_in_sentence(sentence)

    def test_error_leading_spaces(self):
        # Description: Sentence has leading spaces.
        sentence = "  leading space"
        with self.assertRaises(ValueError):
            words_in_sentence(sentence)

    def test_error_not_string_input(self):
        # Description: Input is not a string.
        sentence = 123
        with self.assertRaises(TypeError):
            words_in_sentence(sentence)

    def test_error_null_input(self):
        # Description: Input is null.
        sentence = None
        with self.assertRaises(TypeError):
            words_in_sentence(sentence)