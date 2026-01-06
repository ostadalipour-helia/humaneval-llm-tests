import unittest
from sut.problem_HumanEval_133 import sum_squares

class Test_sum_squares(unittest.TestCase):

    def test_case_0(self):
        self.assertEqual(sum_squares([1, 2, 3]), 14)

    def test_case_1(self):
        self.assertEqual(sum_squares([1, 4, 9]), 98)

    def test_case_2(self):
        self.assertEqual(sum_squares([1, 3, 5, 7]), 84)

    def test_case_3(self):
        self.assertEqual(sum_squares([1.4, 4.2, 0]), 29)

    def test_case_4(self):
        self.assertEqual(sum_squares([-2.4, 1, 1]), 6)

    def test_case_5(self):
        self.assertEqual(sum_squares([]), 0)

    def test_case_6(self):
        self.assertEqual(sum_squares([5]), 25)

    def test_case_7(self):
        self.assertEqual(sum_squares([3.1]), 16)

    def test_case_8(self):
        self.assertEqual(sum_squares([-1.5, -3.8]), 10)

    def test_case_9(self):
        self.assertEqual(sum_squares([0]), 0)