import unittest
from sut.problem_HumanEval_91 import is_bored

class TestIsBored(unittest.TestCase):

    def test_docstring_example_no_boredom(self):
        # Test case from docstring: no boredoms
        self.assertEqual(is_bored("Hello world"), 0)

    def test_docstring_example_one_boredom(self):
        # Test case from docstring: one boredom
        self.assertEqual(is_bored("The sky is blue. The sun is shining. I love this weather"), 1)

    def test_empty_string(self):
        # Edge case: empty string
        self.assertEqual(is_bored(""), 0)

    def test_single_bored_sentence(self):
        # Edge case: single sentence, which is a boredom
        # Boundary: sentence starts with "I", ends with a delimiter
        self.assertEqual(is_bored("I am happy."), 1)

    def test_multiple_bored_sentences_all_types_of_delimiters(self):
        # Multiple boredoms with different delimiters
        # Boundary: tests all delimiter types (., !, ?)
        self.assertEqual(is_bored("I am here. I am there! I am everywhere?"), 3)

    def test_no_boredom_despite_i_presence(self):
        # Logic mutation: "I" is present but not as the start of a sentence or not as a word
        # Off-by-one: ensures "Is" or "I'm" are not counted as "I"
        self.assertEqual(is_bored("Is it true? I'm not sure. Important question."), 0)

    def test_leading_trailing_spaces_and_no_final_delimiter(self):
        # Boundary: leading/trailing spaces, and string does not end with a delimiter
        # Logic: ensures spaces are handled correctly around "I"
        self.assertEqual(is_bored("  I am here. You are there. I am everywhere  "), 2)

    def test_case_sensitivity_and_non_word_i(self):
        # Logic mutation: tests case sensitivity ('i' vs 'I') and "Is" vs "I"
        # Boundary: 'i' at the start of a sentence
        self.assertEqual(is_bored("i am small. I am big. Is it good?"), 1)

    def test_string_with_only_delimiters_and_spaces(self):
        # Edge case: string contains only delimiters and spaces, no actual words
        self.assertEqual(is_bored(". ! ? . . .   "), 0)

    def test_many_boredoms_consecutive_delimiters(self):
        # Extreme input: many boredoms, with consecutive delimiters
        # Boundary: "I" immediately after a delimiter, multiple delimiters in a row
        self.assertEqual(is_bored("I. I! I? I. I. I! I? I. I. I."), 10)