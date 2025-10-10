import unittest
from sut_llm.problem_HumanEval_143 import words_in_sentence

class TestWordsInSentence(unittest.TestCase):

    def test_1_docstring_example_1(self):
        # Example from the docstring
        sentence = "This is a test"
        expected_output = "is"
        self.assertEqual(words_in_sentence(sentence), expected_output)

    def test_2_docstring_example_2(self):
        # Example from the docstring
        sentence = "lets go for swimming"
        expected_output = "go for"
        self.assertEqual(words_in_sentence(sentence), expected_output)

    def test_3_single_word_prime_length(self):
        # Test with a single word whose length is a prime number (e.g., 5)
        sentence = "prime"
        expected_output = "prime"
        self.assertEqual(words_in_sentence(sentence), expected_output)

    def test_4_single_word_non_prime_length(self):
        # Test with a single word whose length is not a prime number (e.g., 4)
        sentence = "four"
        expected_output = ""
        self.assertEqual(words_in_sentence(sentence), expected_output)

    def test_5_all_words_have_prime_length(self):
        # Test where all words in the sentence have prime lengths
        sentence = "is the cat dog" # lengths: 2, 3, 3, 3
        expected_output = "is the cat dog"
        self.assertEqual(words_in_sentence(sentence), expected_output)

    def test_6_no_words_have_prime_length(self):
        # Test where some words in the sentence have prime lengths, contrary to the test name
        sentence = "fourteen sixteen eighteen twenty" # lengths: 8, 7, 8, 6
        # "sixteen" has length 7, which is a prime number.
        expected_output = "sixteen"
        self.assertEqual(words_in_sentence(sentence), expected_output)

    def test_7_mixed_lengths_with_longer_words(self):
        # Test with a mix of prime and non-prime lengths, including longer words
        sentence = "programming is a fascinating subject" # lengths: 11, 2, 1, 11, 7
        expected_output = "programming is fascinating subject"
        self.assertEqual(words_in_sentence(sentence), expected_output)

    def test_8_minimum_sentence_length_one_char_word(self):
        # Test with the smallest possible sentence (one word, one character), length 1 is not prime
        sentence = "a"
        expected_output = ""
        self.assertEqual(words_in_sentence(sentence), expected_output)

    def test_9_minimum_sentence_length_two_char_word(self):
        # Test with a two-character word (length 2 is prime)
        sentence = "hi"
        expected_output = "hi"
        self.assertEqual(words_in_sentence(sentence), expected_output)

    def test_10_various_prime_and_non_prime_lengths(self):
        # Test with a diverse set of word lengths, including 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
        sentence = "a is the four prime number perfect example beautiful magnificent"
        # lengths: a=1(no), is=2(yes), the=3(yes), four=4(no), prime=5(yes), number=6(no), perfect=7(yes), example=7(yes), beautiful=9(no), magnificent=11(yes)
        expected_output = "is the prime perfect example magnificent"
        self.assertEqual(words_in_sentence(sentence), expected_output)

if __name__ == '__main__':
    unittest.main()