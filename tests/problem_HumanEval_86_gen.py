import unittest
from sut.problem_HumanEval_86 import anti_shuffle

class TestAntiShuffle(unittest.TestCase):

    def test_single_word_already_sorted(self):
        self.assertEqual(anti_shuffle('Hi'), 'Hi')

    def test_single_word_needs_sorting(self):
        self.assertEqual(anti_shuffle('hello'), 'ehllo')

    def test_multiple_words_mixed_case_punctuation(self):
        self.assertEqual(anti_shuffle('Hello World!!!'), 'Hello !!!Wdlor')

    def test_empty_string(self):
        self.assertEqual(anti_shuffle(''), '')

    def test_string_with_only_spaces(self):
        self.assertEqual(anti_shuffle('   '), '   ')

    def test_single_character_word(self):
        self.assertEqual(anti_shuffle('a'), 'a')

    def test_multiple_words_all_lowercase(self):
        self.assertEqual(anti_shuffle('python is fun'), 'hnoopt is fnu')

    def test_words_with_numbers_and_symbols(self):
        self.assertEqual(anti_shuffle('123abc DEF!@#'), '123abc !@#DEF')

    def test_words_with_leading_trailing_spaces(self):
        self.assertEqual(anti_shuffle('  test  me  '), '  estt  em  ')

    def test_complex_sentence_with_various_punctuation(self):
        self.assertEqual(anti_shuffle('This is a Test. How are you?'), 'Hist is a .Estt How aer ?ouy')

if __name__ == '__main__':
    unittest.main()