import unittest
from sut.problem_HumanEval_94 import skjkasdkd

class Test_skjkasdkd(unittest.TestCase):

    def test_normal_case_1(self):
        self.assertEqual(skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]), 10)

    def test_normal_case_2(self):
        self.assertEqual(skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]), 25)

    def test_normal_case_3(self):
        self.assertEqual(skjkasdkd([1, 3, 1, 32, 5107, 34, 83278, 109, 163, 23, 2323, 32, 30, 1, 9, 3]), 13)

    def test_normal_case_4(self):
        self.assertEqual(skjkasdkd([0, 724, 32, 71, 99, 32, 6, 0, 5, 91, 83, 0, 5, 6]), 11)

    def test_normal_case_5(self):
        self.assertEqual(skjkasdkd([0, 81, 12, 3, 1, 21]), 3)

    def test_edge_case_empty_list(self):
        self.assertEqual(skjkasdkd([]), 0)

    def test_edge_case_no_primes(self):
        self.assertEqual(skjkasdkd([0, 1, 4, 6, 8, 9, 10, 12]), 1)

    def test_edge_case_single_prime(self):
        self.assertEqual(skjkasdkd([10, 11, 12, 14]), 2)

    def test_edge_case_with_negatives(self):
        self.assertEqual(skjkasdkd([-2, -3, 5, 7, -10]), 7)

    def test_edge_case_large_prime(self):
        self.assertEqual(skjkasdkd([1000000007]), 8)