import unittest
import sut.problem_HumanEval_91 as mod

class TestHybrid(unittest.TestCase):
    def test_docstring_example_no_boredom(self):
            # Test case from docstring: no boredoms
            self.assertEqual(mod.is_bored("Hello world"), 0)

    def test_docstring_example_one_boredom(self):
            # Test case from docstring: one boredom
            self.assertEqual(mod.is_bored("The sky is blue. The sun is shining. I love this weather"), 1)

    def test_empty_string(self):
            # Edge case: empty string
            self.assertEqual(mod.is_bored(""), 0)

    def test_single_bored_sentence(self):
            # Edge case: single sentence, which is a boredom
            # Boundary: sentence starts with "I", ends with a delimiter
            self.assertEqual(mod.is_bored("I am happy."), 1)

    def test_multiple_bored_sentences_all_types_of_delimiters(self):
            # Multiple boredoms with different delimiters
            # Boundary: tests all delimiter types (., !, ?)
            self.assertEqual(mod.is_bored("I am here. I am there! I am everywhere?"), 3)

    def test_no_boredom_despite_i_presence(self):
            # Logic mutation: "I" is present but not as the start of a sentence or not as a word
            # Off-by-one: ensures "Is" or "I'm" are not counted as "I"
            self.assertEqual(mod.is_bored("Is it true? I'm not sure. Important question."), 0)

    def test_case_sensitivity_and_non_word_i(self):
            # Logic mutation: tests case sensitivity ('i' vs 'I') and "Is" vs "I"
            # Boundary: 'i' at the start of a sentence
            self.assertEqual(mod.is_bored("i am small. I am big. Is it good?"), 1)

    def test_string_with_only_delimiters_and_spaces(self):
            # Edge case: string contains only delimiters and spaces, no actual words
            self.assertEqual(mod.is_bored(". ! ? . . .   "), 0)

    def test_normal_no_i_sentences(self):
            # Normal case: String with no 'I' sentences and no explicit delimiters.
            self.assertEqual(mod.is_bored("Hello world"), 0)

    def test_normal_one_i_sentence(self):
            # Normal case: Multiple sentences, one of which starts with 'I'.
            self.assertEqual(mod.is_bored("The sky is blue. The sun is shining. I love this weather"), 1)

    def test_normal_multiple_i_sentences(self):
            # Normal case: Multiple 'I' sentences with different delimiters.
            self.assertEqual(mod.is_bored("I am happy. Are you? I am very happy!"), 2)

    def test_edge_empty_string(self):
            # Edge case: Empty string.
            self.assertEqual(mod.is_bored(""), 0)

    def test_edge_i_no_end_delimiter(self):
            # Edge case: String starting with 'I' but no explicit delimiter at the end.
            self.assertEqual(mod.is_bored("I am bored"), 1)

    def test_edge_lowercase_i_ignored(self):
            # Edge case: Lowercase 'i' at the start of a sentence should not count.
            self.assertEqual(mod.is_bored("i am bored. I am not."), 1)

    def test_edge_im_not_i(self):
            # Edge case: 'I'm' is not 'I' as a standalone word.
            self.assertEqual(mod.is_bored("I'm bored. I am not."), 1)

    def test_error_none_input(self):
            # Error case: Input is None.
            with self.assertRaises(TypeError):
                mod.is_bored(None)

    def test_error_int_input(self):
            # Error case: Input is an integer.
            with self.assertRaises(TypeError):
                mod.is_bored(123)

