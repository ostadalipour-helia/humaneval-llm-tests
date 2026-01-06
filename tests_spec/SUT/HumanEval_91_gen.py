import unittest
from sut.problem_HumanEval_91 import is_bored

class Test_is_bored(unittest.TestCase):

    def test_normal_cases(self):
        self.assertEqual(is_bored("Hello world"), 0)
        self.assertEqual(is_bored("The sky is blue. The sun is shining. I love this weather"), 1)
        self.assertEqual(is_bored("I am happy. Are you? I am very happy!"), 2)
        self.assertEqual(is_bored("This is a test. I am testing. It works."), 1)

    def test_empty_string(self):
        self.assertEqual(is_bored(""), 0)

    def test_single_sentence_boredom(self):
        self.assertEqual(is_bored("I am bored"), 1)

    def test_case_sensitivity(self):
        self.assertEqual(is_bored("i am bored. I am not."), 1)

    def test_word_boundary(self):
        self.assertEqual(is_bored("I'm bored. I am not."), 1)

    def test_multiple_delimiters(self):
        self.assertEqual(is_bored("I am bored... Really?"), 1)

    def test_leading_trailing_spaces(self):
        self.assertEqual(is_bored("   I am bored.  "), 0)

    def test_minimal_i_sentences(self):
        self.assertEqual(is_bored("I. I? I!"), 0)
        self.assertEqual(is_bored("Hello world. I."), 0)
        self.assertEqual(is_bored("I."), 0)

    def test_string_is_just_i(self):
        self.assertEqual(is_bored("I"), 0)

    def test_no_space_after_delimiter(self):
        self.assertEqual(is_bored("Hello.World.I.Am.Bored."), 0)