import unittest
from sut.problem_HumanEval_1 import separate_paren_groups

class Test_separate_paren_groups(unittest.TestCase):

    def test_case_0(self):
        paren_string = "( ) (( )) (( )( ))"
        expected = ['()', '(())', '(()())']
        self.assertEqual(separate_paren_groups(paren_string), expected)

    def test_case_1(self):
        paren_string = "((())) ()"
        expected = ['((()))', '()']
        self.assertEqual(separate_paren_groups(paren_string), expected)

    def test_case_2(self):
        paren_string = "( ( ( ) ) )"
        expected = ['((()))']
        self.assertEqual(separate_paren_groups(paren_string), expected)

    def test_case_3(self):
        paren_string = "()"
        expected = ['()']
        self.assertEqual(separate_paren_groups(paren_string), expected)

    def test_case_4(self):
        paren_string = "   (   )    ( ( ) )   "
        expected = ['()', '(())']
        self.assertEqual(separate_paren_groups(paren_string), expected)

    def test_case_5(self):
        paren_string = ""
        expected = []
        self.assertEqual(separate_paren_groups(paren_string), expected)

    def test_case_6(self):
        paren_string = "      "
        expected = []
        self.assertEqual(separate_paren_groups(paren_string), expected)

    def test_case_7(self):
        paren_string = "( ) (( )) (( )( ))"
        expected = ['()', '(())', '(()())']
        self.assertEqual(separate_paren_groups(paren_string), expected)

    def test_case_8(self):
        paren_string = "((())) ()"
        expected = ['((()))', '()']
        self.assertEqual(separate_paren_groups(paren_string), expected)

    def test_case_9(self):
        paren_string = "( ( ( ) ) )"
        expected = ['((()))']
        self.assertEqual(separate_paren_groups(paren_string), expected)