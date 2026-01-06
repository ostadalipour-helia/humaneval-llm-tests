import unittest
from sut.problem_HumanEval_40 import triples_sum_to_zero

class Test_triples_sum_to_zero(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(triples_sum_to_zero([1, 3, 5, 0]), False)

    def test_case_2(self):
        self.assertEqual(triples_sum_to_zero([1, 3, -2, 1]), False)

    def test_case_3(self):
        self.assertEqual(triples_sum_to_zero([2, 4, -5, 3, 9, 7]), False)

    def test_case_4(self):
        self.assertEqual(triples_sum_to_zero([1, 2, 3, 7]), False)

    def test_case_5(self):
        self.assertEqual(triples_sum_to_zero([]), False)

    def test_case_6(self):
        self.assertEqual(triples_sum_to_zero([1, 2]), False)

    def test_case_7(self):
        self.assertEqual(triples_sum_to_zero([0, 0, 0]), False)

    def test_case_8(self):
        self.assertEqual(triples_sum_to_zero([-1, 0, 1]), False)

    def test_case_9(self):
        self.assertEqual(triples_sum_to_zero([1, 1, 1, -2]), False)

    def test_case_10(self):
        self.assertEqual(triples_sum_to_zero([10, 20, -30, 40, -50]), False)