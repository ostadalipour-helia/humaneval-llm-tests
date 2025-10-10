import unittest
from sut_llm.problem_HumanEval_143 import words_in_sentence

class TestWordsInSentence(unittest.TestCase):

    def test_example_1(self):
        # Docstring example 1: "This is a test" -> "is"
        sentence = "This is a test"
        expected_output = "is"
        self.assertEqual(words_in_sentence(sentence), expected_output)

    def test_example_2(self):
        # Docstring example 2: "lets go for swimming" -> "go for"
        sentence = "lets go for swimming"
        expected_output = "go for"
        self.assertEqual(words_in_sentence(sentence), expected_output)

    def test_no_prime_length_words(self):
        # All words have non-prime lengths
        sentence = "a four letter word" # lengths: 1, 4, 6, 4
        expected_output = ""
        self.assertEqual(words_in_sentence(sentence), expected_output)

    def test_all_words_prime_length(self):
        # All words in the sentence have prime lengths
        sentence = "is an of at" # lengths: 2, 2, 2, 2
        expected_output = "is an of at"
        self.assertEqual(words_in_sentence(sentence), expected_output)

    def test_single_word_prime_length(self):
        # Sentence with a single word of prime length
        sentence = "hello" # length: 5
        expected_output = "hello"
        self.assertEqual(words_in_sentence(sentence), expected_output)

    def test_single_word_non_prime_length(self):
        # Sentence with a single word of non-prime length
        sentence = "python" # length: 6
        expected_output = ""
        self.assertEqual(words_in_sentence(sentence), expected_output)

    def test_mixed_lengths_starts_non_prime(self):
        # Mixed prime and non-prime lengths, starting with a non-prime word
        sentence = "a quick brown fox" # lengths: 1, 5, 5, 3
        expected_output = "quick brown fox"
        self.assertEqual(words_in_sentence(sentence), expected_output)

    def test_mixed_lengths_ends_non_prime(self):
        # Mixed prime and non-prime lengths, ending with a non-prime word
        sentence = "quick brown fox a" # lengths: 5, 5, 3, 1
        expected_output = "quick brown fox"
        self.assertEqual(words_in_sentence(sentence), expected_output)

    def test_longer_sentence_mixed_lengths(self):
        # A longer sentence with various prime and non-prime word lengths
        sentence = "the quick brown fox jumps over the lazy dog and a cat"
        # lengths: 3, 5, 5, 3, 5, 4, 3, 4, 3, 3, 1, 3
        # primes:  Y, Y, Y, Y, Y, N, Y, N, Y, Y, N, Y
        expected_output = "the quick brown fox jumps the dog and cat"
        self.assertEqual(words_in_sentence(sentence), expected_output)

    def test_short_words_mixed_prime_non_prime(self):
        # Edge case with very short words, some prime, some not
        sentence = "a bb ccc dddd eeeee ffffff ggggggg"
        # lengths: 1, 2, 3, 4, 5, 6, 7
        # primes:  N, Y, Y, N, Y, N, Y
        expected_output = "bb ccc eeeee ggggggg"
        self.assertEqual(words_in_sentence(sentence), expected_output)

    def test_prime_check_even_and_odd_lengths(self):
        # This test aims to cover:
        # - Line 35: `if n % 2 == 0:` (by passing an even number > 2, e.g., 6)
        # - Line 36: `return False` (by passing an even number > 2, e.g., 6)
        # - Line 37: `i = 3` (by passing an odd number > 2, e.g., 5)
        sentence = "apple banana orange grape"
        # "apple" has length 5 (prime) -> is_prime(5) will execute line 37
        # "banana" has length 6 (not prime) -> is_prime(6) will execute lines 35 and 36
        # "orange" has length 6 (not prime) -> is_prime(6) will execute lines 35 and 36
        # "grape" has length 5 (prime) -> is_prime(5) will execute line 37
        result = words_in_sentence(sentence)
        self.assertEqual(result, "apple grape")

if __name__ == '__main__':
    unittest.main()