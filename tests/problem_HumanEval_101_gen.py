import unittest
from sut.problem_HumanEval_101 import words_string

class TestWordsString(unittest.TestCase):

    def test_mixed_separators_docstring_1(self):
        # Typical input with mixed spaces and commas, as per docstring example 1.
        # Verifies correct splitting and handling of both separator types.
        s = "Hi, my name is John"
        expected = ["Hi", "my", "name", "is", "John"]
        self.assertListEqual(words_string(s), expected)

    def test_only_commas_docstring_2(self):
        # Typical input with only commas as separators, as per docstring example 2.
        # Verifies correct splitting when only one type of separator is present.
        s = "One, two, three, four, five, six"
        expected = ["One", "two", "three", "four", "five", "six"]
        self.assertListEqual(words_string(s), expected)

    def test_empty_string_edge_case(self):
        # Edge case: An empty input string.
        # Should result in an empty list of words.
        s = ""
        expected = []
        self.assertListEqual(words_string(s), expected)

    def test_single_word_no_separators_edge_case(self):
        # Edge case: A string containing only a single word with no separators.
        # Should return a list containing that single word.
        s = "HelloWorld"
        expected = ["HelloWorld"]
        self.assertListEqual(words_string(s), expected)

    def test_only_spaces_as_separators(self):
        # Logic mutation test: String with only spaces as separators.
        # Ensures that space splitting is correctly handled when no commas are present.
        s = "apple banana cherry"
        expected = ["apple", "banana", "cherry"]
        self.assertListEqual(words_string(s), expected)

    def test_leading_trailing_and_mixed_separators_boundary(self):
        # Boundary test: String with leading, trailing, and mixed separators.
        # Catches issues with stripping or filtering empty strings from the split result.
        s = " ,word1, word2 , "
        expected = ["word1", "word2"]
        self.assertListEqual(words_string(s), expected)

    def test_multiple_consecutive_separators_boundary(self):
        # Boundary test: String with multiple consecutive commas and spaces.
        # Catches off-by-one errors or incorrect handling of repeated delimiters.
        s = "word1,,  word2   ,word3"
        expected = ["word1", "word2", "word3"]
        self.assertListEqual(words_string(s), expected)

    def test_string_with_only_separators_extreme(self):
        # Extreme input: A string composed entirely of separators.
        # Should result in an empty list, as there are no actual words.
        s = "   , ,   , "
        expected = []
        self.assertListEqual(words_string(s), expected)

    def test_words_with_internal_commas_or_spaces(self):
        # Unusual input: Words themselves contain commas or spaces, but are not delimiters.
        # This tests if the splitting logic correctly identifies actual word boundaries.
        # (Assuming "word,part" is one word if no space/comma separates it from another word)
        # Based on the docstring examples, "Hi, my name is John" -> ["Hi", "my", "name", "is", "John"]
        # implies that a comma *is* a separator. So "word,part" would be ["word", "part"].
        # Let's re-evaluate this test based on the docstring.
        # The docstring implies that commas and spaces are *always* separators.
        # So, "word,part" would split into "word" and "part".
        # Let's test a case where a word might contain a character that *looks* like a separator but isn't.
        # For example, a hyphenated word or a word with an apostrophe.
        s = "don't-forget,this"
        expected = ["don't-forget", "this"]
        self.assertListEqual(words_string(s), expected)

    def test_long_string_many_words_mixed_separators(self):
        # Extreme input: A longer string with many words and a mix of separators.
        # Verifies performance and correctness for larger inputs.
        s = "alpha, beta,gamma delta,epsilon, zeta,eta theta,iota,kappa lambda,mu,nu,xi,omicron,pi"
        expected = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta", "iota", "kappa", "lambda", "mu", "nu", "xi", "omicron", "pi"]
        self.assertListEqual(words_string(s), expected)