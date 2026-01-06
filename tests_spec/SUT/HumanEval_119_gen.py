import unittest
from sut.problem_HumanEval_119 import match_parens

class Test_match_parens(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(match_parens(['()(', ')']), 'No')

    def test_case_1(self):
        self.assertEqual(match_parens(['(', ')']), 'No')

    def test_case_2(self):
        self.assertEqual(match_parens(['((', '))']), 'No')

    def test_case_3(self):
        self.assertEqual(match_parens(['()', '()']), 'No')

    def test_case_4(self):
        self.assertEqual(match_parens(['', '']), 'No')

    def test_case_5(self):
        self.assertEqual(match_parens(['()', '']), 'No')

    def test_case_6(self):
        self.assertEqual(match_parens(['', '()']), 'No')

    def test_case_7(self):
        self.assertEqual(match_parens([')))', '(((']), 'No')

    def test_case_8(self):
        self.assertEqual(match_parens(['()', ')(']), 'No')

    def test_case_9(self):
        self.assertEqual(match_parens([')))((', '()']), 'No')