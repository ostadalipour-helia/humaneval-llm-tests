import unittest
import sut.problem_HumanEval_101 as mod

class TestHybrid(unittest.TestCase):
    def test_mixed_separators_docstring_1(self):
            # Typical input with mixed spaces and commas, as per docstring example 1.
            # Verifies correct splitting and handling of both separator types.
            s = "Hi, my name is John"
            expected = ["Hi", "my", "name", "is", "John"]
            self.assertListEqual(mod.words_string(s), expected)

    def test_only_commas_docstring_2(self):
            # Typical input with only commas as separators, as per docstring example 2.
            # Verifies correct splitting when only one type of separator is present.
            s = "One, two, three, four, five, six"
            expected = ["One", "two", "three", "four", "five", "six"]
            self.assertListEqual(mod.words_string(s), expected)

    def test_empty_string_edge_case(self):
            # Edge case: An empty input string.
            # Should result in an empty list of words.
            s = ""
            expected = []
            self.assertListEqual(mod.words_string(s), expected)

    def test_single_word_no_separators_edge_case(self):
            # Edge case: A string containing only a single word with no separators.
            # Should return a list containing that single word.
            s = "HelloWorld"
            expected = ["HelloWorld"]
            self.assertListEqual(mod.words_string(s), expected)

    def test_only_spaces_as_separators(self):
            # Logic mutation test: String with only spaces as separators.
            # Ensures that space splitting is correctly handled when no commas are present.
            s = "apple banana cherry"
            expected = ["apple", "banana", "cherry"]
            self.assertListEqual(mod.words_string(s), expected)

    def test_leading_trailing_and_mixed_separators_boundary(self):
            # Boundary test: String with leading, trailing, and mixed separators.
            # Catches issues with stripping or filtering empty strings from the split result.
            s = " ,word1, word2 , "
            expected = ["word1", "word2"]
            self.assertListEqual(mod.words_string(s), expected)

    def test_multiple_consecutive_separators_boundary(self):
            # Boundary test: String with multiple consecutive commas and spaces.
            # Catches off-by-one errors or incorrect handling of repeated delimiters.
            s = "word1,,  word2   ,word3"
            expected = ["word1", "word2", "word3"]
            self.assertListEqual(mod.words_string(s), expected)

    def test_string_with_only_separators_extreme(self):
            # Extreme input: A string composed entirely of separators.
            # Should result in an empty list, as there are no actual words.
            s = "   , ,   , "
            expected = []
            self.assertListEqual(mod.words_string(s), expected)

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
            self.assertListEqual(mod.words_string(s), expected)

    def test_long_string_many_words_mixed_separators(self):
            # Extreme input: A longer string with many words and a mix of separators.
            # Verifies performance and correctness for larger inputs.
            s = "alpha, beta,gamma delta,epsilon, zeta,eta theta,iota,kappa lambda,mu,nu,xi,omicron,pi"
            expected = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta", "iota", "kappa", "lambda", "mu", "nu", "xi", "omicron", "pi"]
            self.assertListEqual(mod.words_string(s), expected)

    def test_normal_basic_sentence(self):
            # Normal case: sentence with mixed spaces and commas
            s = "Hi, my name is John"
            expected_output = ["Hi", "my", "name", "is", "John"]
            self.assertEqual(mod.words_string(s), expected_output)

    def test_normal_comma_separated_list(self):
            # Normal case: words separated only by commas
            s = "apple,banana,cherry"
            expected_output = ["apple", "banana", "cherry"]
            self.assertEqual(mod.words_string(s), expected_output)

    def test_normal_space_separated_words(self):
            # Normal case: words separated only by spaces
            s = "hello world"
            expected_output = ["hello", "world"]
            self.assertEqual(mod.words_string(s), expected_output)

    def test_edge_empty_string(self):
            # Edge case: empty input string
            s = ""
            expected_output = []
            self.assertEqual(mod.words_string(s), expected_output)

    def test_edge_only_separators(self):
            # Edge case: string containing only spaces and commas
            s = " , ,   ,, "
            expected_output = []
            self.assertEqual(mod.words_string(s), expected_output)

    def test_edge_single_word_with_padding(self):
            # Edge case: single word with leading/trailing separators
            s = "  singleword  "
            expected_output = ["singleword"]
            self.assertEqual(mod.words_string(s), expected_output)

    def test_edge_multiple_consecutive_separators(self):
            # Edge case: multiple consecutive separators
            s = "word1,,word2   word3"
            expected_output = ["word1", "word2", "word3"]
            self.assertEqual(mod.words_string(s), expected_output)

    def test_edge_complex_leading_trailing_and_multiple_separators(self):
            # Edge case: complex mix of leading/trailing and multiple separators
            s = "  word1,  word2 ,word3  "
            expected_output = ["word1", "word2", "word3"]
            self.assertEqual(mod.words_string(s), expected_output)

    def test_error_integer_input(self):
            # Error case: input is an integer
            s = 123
            with self.assertRaises(TypeError):
                mod.words_string(s)

