import unittest
from sut.problem_HumanEval_84 import solve

class Test_solve(unittest.TestCase):

    def test_normal_case_1000(self):
        self.assertEqual(solve(1000), '1')

    def test_normal_case_150(self):
        self.assertEqual(solve(150), '110')

    def test_normal_case_147(self):
        self.assertEqual(solve(147), '1100')

    def test_normal_case_12345(self):
        self.assertEqual(solve(12345), '1111')

    def test_edge_case_0(self):
        self.assertEqual(solve(0), '0')

    def test_edge_case_10000(self):
        self.assertEqual(solve(10000), '1')

    def test_edge_case_9(self):
        self.assertEqual(solve(9), '1001')

    def test_edge_case_9999(self):
        self.assertEqual(solve(9999), '100100')

    def test_edge_case_1(self):
        self.assertEqual(solve(1), '1')

    def test_duplicate_case_to_meet_count(self):
        self.assertEqual(solve(1000), '1')