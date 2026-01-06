import unittest
from sut.problem_HumanEval_56 import correct_bracketing

class Test_correct_bracketing(unittest.TestCase):

    def test_normal_case_simple_pair(self):
        self.assertEqual(correct_bracketing("<>"), True)

    def test_normal_case_nested(self):
        self.assertEqual(correct_bracketing("<<><>>"), True)

    def test_normal_case_sequential(self):
        self.assertEqual(correct_bracketing("<<<>>>"), True)

    def test_edge_case_empty_string(self):
        self.assertEqual(correct_bracketing(""), True)

    def test_edge_case_single_open(self):
        self.assertEqual(correct_bracketing("<"), False)

    def test_edge_case_single_close(self):
        self.assertEqual(correct_bracketing(">"), False)

    def test_edge_case_incorrect_start(self):
        self.assertEqual(correct_bracketing("><<>"), False)

    def test_edge_case_multiple_close(self):
        self.assertEqual(correct_bracketing(">>"), False)

    def test_edge_case_multiple_open(self):
        self.assertEqual(correct_bracketing("<<<"), False)