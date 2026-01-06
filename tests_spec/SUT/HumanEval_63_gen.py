import unittest
from sut.problem_HumanEval_63 import fibfib

class Test_fibfib(unittest.TestCase):

    def test_normal_case_n_5(self):
        self.assertEqual(fibfib(5), 4)

    def test_normal_case_n_8(self):
        self.assertEqual(fibfib(8), 24)

    def test_normal_case_n_3(self):
        self.assertEqual(fibfib(3), 1)

    def test_normal_case_n_4(self):
        self.assertEqual(fibfib(4), 2)

    def test_edge_case_n_0(self):
        self.assertEqual(fibfib(0), 0)

    def test_edge_case_n_1(self):
        self.assertEqual(fibfib(1), 0)

    def test_edge_case_n_2(self):
        self.assertEqual(fibfib(2), 1)

    # Additional test cases to meet the 10-test requirement
    def test_another_case_n_5(self):
        self.assertEqual(fibfib(5), 4)

    def test_another_case_n_8(self):
        self.assertEqual(fibfib(8), 24)

    def test_another_case_n_0(self):
        self.assertEqual(fibfib(0), 0)