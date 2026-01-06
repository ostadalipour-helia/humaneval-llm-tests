import unittest
from sut.problem_HumanEval_91 import is_bored

class Test_is_bored(unittest.TestCase):
    def test_normal_no_i_sentences(self):
        # Normal case: String with no 'I' sentences and no explicit delimiters.
        self.assertEqual(is_bored("Hello world"), 0)

    def test_normal_one_i_sentence(self):
        # Normal case: Multiple sentences, one of which starts with 'I'.
        self.assertEqual(is_bored("The sky is blue. The sun is shining. I love this weather"), 1)

    def test_normal_multiple_i_sentences(self):
        # Normal case: Multiple 'I' sentences with different delimiters.
        self.assertEqual(is_bored("I am happy. Are you? I am very happy!"), 2)

    def test_edge_empty_string(self):
        # Edge case: Empty string.
        self.assertEqual(is_bored(""), 0)

    def test_edge_i_no_end_delimiter(self):
        # Edge case: String starting with 'I' but no explicit delimiter at the end.
        self.assertEqual(is_bored("I am bored"), 1)

    def test_edge_lowercase_i_ignored(self):
        # Edge case: Lowercase 'i' at the start of a sentence should not count.
        self.assertEqual(is_bored("i am bored. I am not."), 1)

    def test_edge_im_not_i(self):
        # Edge case: 'I'm' is not 'I' as a standalone word.
        self.assertEqual(is_bored("I'm bored. I am not."), 1)

    def test_edge_just_i(self):
        # Edge case: String is just 'I' (no delimiter, no other words).
        self.assertEqual(is_bored("I"), 1)

    def test_edge_just_i_with_delimiter(self):
        # Edge case: String is 'I' followed by a delimiter.
        self.assertEqual(is_bored("I."), 1)

    def test_edge_leading_trailing_spaces(self):
        # Edge case: Leading/trailing spaces and spaces around delimiters.
        self.assertEqual(is_bored("   I am bored.  "), 1)

    def test_error_none_input(self):
        # Error case: Input is None.
        with self.assertRaises(TypeError):
            is_bored(None)

    def test_error_int_input(self):
        # Error case: Input is an integer.
        with self.assertRaises(TypeError):
            is_bored(123)