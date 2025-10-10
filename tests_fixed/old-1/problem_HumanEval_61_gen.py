import unittest
from sut_llm.problem_HumanEval_61 import correct_bracketing

class TestCorrectBracketing(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(correct_bracketing(""))

    def test_simple_valid(self):
        self.assertTrue(correct_bracketing("()"))

    def test_simple_invalid_open(self):
        self.assertFalse(correct_bracketing("("))

    def test_simple_invalid_close(self):
        self.assertFalse(correct_bracketing(")"))

    def test_nested_valid(self):
        self.assertTrue(correct_bracketing("(()())"))

    def test_invalid_order(self):
        self.assertFalse(correct_bracketing(")(()"))

    def test_unmatched_open_at_end(self):
        self.assertFalse(correct_bracketing("((())"))

    def test_unmatched_close_at_start(self):
        self.assertFalse(correct_bracketing("))(())"))

    def test_complex_valid(self):
        self.assertTrue(correct_bracketing("((()())(()))"))

    def test_complex_invalid(self):
        self.assertFalse(correct_bracketing("((()())()))"))

if __name__ == '__main__':
    unittest.main()