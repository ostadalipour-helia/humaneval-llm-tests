import unittest
from sut.problem_HumanEval_97 import multiply

class Test_multiply(unittest.TestCase):
    def test_normal_case_1(self):
        # Unit digit of 148 is 8. Unit digit of 412 is 2. Product is 8 * 2 = 16.
        self.assertEqual(multiply(148, 412), 16)

    def test_normal_case_2(self):
        # Unit digit of 19 is 9. Unit digit of 28 is 8. Product is 9 * 8 = 72.
        self.assertEqual(multiply(19, 28), 72)

    def test_normal_case_3(self):
        # Unit digit of 2020 is 0. Unit digit of 1851 is 1. Product is 0 * 1 = 0.
        self.assertEqual(multiply(2020, 1851), 0)

    def test_edge_case_negative_b(self):
        # Unit digit of 14 is 4. Unit digit of -15 is 5 (since -15 % 10 = 5 in Python). Product is 4 * 5 = 20.
        self.assertEqual(multiply(14, -15), 20)

    def test_edge_case_single_digits(self):
        # Single-digit numbers. Unit digit of 5 is 5. Unit digit of 7 is 7. Product is 5 * 7 = 35.
        self.assertEqual(multiply(5, 7), 35)

    def test_edge_case_zero_and_hundred(self):
        # One number is zero. Unit digit of 0 is 0. Unit digit of 100 is 0. Product is 0 * 0 = 0.
        self.assertEqual(multiply(0, 100), 0)

    def test_edge_case_both_negative(self):
        # Both numbers are negative. Unit digit of -1 is 9 (since -1 % 10 = 9 in Python). Product is 9 * 9 = 81.
        self.assertEqual(multiply(-1, -1), 81)