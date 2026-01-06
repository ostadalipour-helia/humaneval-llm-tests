import unittest
from sut.problem_HumanEval_61 import correct_bracketing

class Test_correct_bracketing(unittest.TestCase):

    def test_simple_correct_pair(self):
        self.assertEqual(correct_bracketing("()"), True)

    def test_nested_and_sequential_correct(self):
        self.assertEqual(correct_bracketing("(()())"), True)

    def test_deeply_nested_correct(self):
        self.assertEqual(correct_bracketing("((()))"), True)

    def test_empty_string(self):
        self.assertEqual(correct_bracketing(""), True)

    def test_single_opening_bracket(self):
        self.assertEqual(correct_bracketing("("), False)

    def test_single_closing_bracket(self):
        self.assertEqual(correct_bracketing(")"), False)

    def test_inverted_brackets(self):
        self.assertEqual(correct_bracketing(")("), False)

    def test_double_opening_brackets(self):
        self.assertEqual(correct_bracketing("(("), False)

    def test_double_closing_brackets(self):
        self.assertEqual(correct_bracketing("))"), False)

    def test_correct_pair_with_extra_opening(self):
        self.assertEqual(correct_bracketing("()("), False)

if __name__ == '__main__':
    unittest.main()