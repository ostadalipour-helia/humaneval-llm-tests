import unittest
from sut.problem_HumanEval_43 import pairs_sum_to_zero

class Test_pairs_sum_to_zero(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]), True)

    def test_case_2(self):
        self.assertEqual(pairs_sum_to_zero([1, 3, 5, 0]), False)

    def test_case_3(self):
        self.assertEqual(pairs_sum_to_zero([1, 3, -2, 1]), False)

    def test_case_4(self):
        self.assertEqual(pairs_sum_to_zero([1, -1, 2, -2]), True)

    def test_case_5(self):
        self.assertEqual(pairs_sum_to_zero([]), False)

    def test_case_6(self):
        self.assertEqual(pairs_sum_to_zero([1]), False)

    def test_case_7(self):
        self.assertEqual(pairs_sum_to_zero([0, 0]), True)

    def test_case_8(self):
        self.assertEqual(pairs_sum_to_zero([0]), False)

    def test_case_9(self):
        self.assertEqual(pairs_sum_to_zero([1, -1]), True)

    def test_case_10(self):
        self.assertEqual(pairs_sum_to_zero([-1000000, 1000000]), True)