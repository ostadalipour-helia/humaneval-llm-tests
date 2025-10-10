import unittest
from sut.problem_HumanEval_91 import is_bored

class TestIsBored(unittest.TestCase):

    def test_example_no_boredom(self):
        self.assertEqual(is_bored("Hello world"), 0)

    def test_example_one_boredom(self):
        self.assertEqual(is_bored("The sky is blue. The sun is shining. I love this weather"), 1)

    def test_multiple_boredoms_mixed_delimiters(self):
        self.assertEqual(is_bored("I am happy. Are you? I like pizza! What about you? I am hungry."), 3)

    def test_no_boredoms_multiple_sentences(self):
        self.assertEqual(is_bored("This is a test. Another sentence here. And one more."), 0)

    def test_boredom_with_question_mark(self):
        self.assertEqual(is_bored("Are you there? I am here. What's up?"), 1)

    def test_boredom_with_exclamation_mark(self):
        self.assertEqual(is_bored("Wow! This is great! I feel amazing!"), 1)

    def test_empty_string(self):
        self.assertEqual(is_bored(""), 0)

    def test_only_i_as_sentence(self):
        self.assertEqual(is_bored("I. You. I? He! I!"), 3)

    def test_i_as_part_of_word_not_boredom(self):
        self.assertEqual(is_bored("This is an island. Interesting. I am here."), 1)

    def test_leading_trailing_spaces_and_case_sensitivity(self):
        self.assertEqual(is_bored("  I am good.  you are bad. i am okay. I am great! "), 2)

if __name__ == '__main__':
    unittest.main()