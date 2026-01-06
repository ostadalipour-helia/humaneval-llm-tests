import unittest
from sut.problem_HumanEval_139 import special_factorial

class Test_special_factorial(unittest.TestCase):
    def test_normal_case_four(self):
        # n = 4, output = 288 (4! * 3! * 2! * 1! = 24 * 6 * 2 * 1)
        self.assertEqual(special_factorial(4), 288)

    def test_normal_case_three(self):
        # n = 3, output = 12 (3! * 2! * 1! = 6 * 2 * 1)
        self.assertEqual(special_factorial(3), 12)

    def test_normal_case_five(self):
        # n = 5, output = 69120 (5! * 4! * 3! * 2! * 1! = 120 * 24 * 6 * 2 * 1)
        self.assertEqual(special_factorial(5), 69120)

    def test_edge_case_one(self):
        # n = 1, output = 1 (1! = 1)
        self.assertEqual(special_factorial(1), 1)

    def test_error_case_zero(self):
        # n = 0, n must be greater than 0
        with self.assertRaises((ValueError, AssertionError)):
            special_factorial(0)

    def test_error_case_negative(self):
        # n = -5, n must be greater than 0
        with self.assertRaises((ValueError, AssertionError)):
            special_factorial(-5)

    def test_error_case_float(self):
        # n = 3.5, n must be an integer
        with self.assertRaises(TypeError):
            special_factorial(3.5)

    def test_error_case_string(self):
        # n = 'abc', n must be an integer
        with self.assertRaises(TypeError):
            special_factorial('abc')