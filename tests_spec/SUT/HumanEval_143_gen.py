import unittest
from sut.problem_HumanEval_143 import words_in_sentence

class Test_words_in_sentence(unittest.TestCase):

    def test_case_0(self):
        self.assertEqual(words_in_sentence("This is a test"), 'is')

    def test_case_1(self):
        self.assertEqual(words_in_sentence("lets go for swimming"), 'go for')

    def test_case_2(self):
        self.assertEqual(words_in_sentence("hello world python programming"), 'hello world programming')

    def test_case_3(self):
        self.assertEqual(words_in_sentence("a bb ccc dddd eeeee"), 'bb ccc eeeee')

    def test_case_4(self):
        self.assertEqual(words_in_sentence("apple banana cherry"), 'apple')

    def test_case_5(self):
        self.assertEqual(words_in_sentence("two"), 'two')

    def test_case_6(self):
        self.assertEqual(words_in_sentence("four"), '')

    def test_case_7(self):
        self.assertEqual(words_in_sentence("a"), '')

    def test_case_8(self):
        self.assertEqual(words_in_sentence("is"), 'is')

    def test_case_9(self):
        self.assertEqual(words_in_sentence("longwordwithnonprimelength"), '')