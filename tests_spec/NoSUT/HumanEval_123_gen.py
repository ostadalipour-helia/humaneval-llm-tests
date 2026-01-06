import unittest
from sut.problem_HumanEval_123 import get_odd_collatz

class Test_get_odd_collatz(unittest.TestCase):

    def test_normal_five(self):
        # Collatz sequence for 5 is [5, 16, 8, 4, 2, 1]. Odd numbers are 1, 5. Sorted: [1, 5].
        self.assertEqual(get_odd_collatz(5), [1, 5])

    def test_normal_six(self):
        # Collatz sequence for 6 is [6, 3, 10, 5, 16, 8, 4, 2, 1]. Odd numbers are 1, 3, 5. Sorted: [1, 3, 5].
        self.assertEqual(get_odd_collatz(6), [1, 3, 5])

    def test_normal_seven(self):
        # Collatz sequence for 7 is [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1].
        # Odd numbers are 1, 5, 7, 11, 13, 17. Sorted: [1, 5, 7, 11, 13, 17].
        self.assertEqual(get_odd_collatz(7), [1, 5, 7, 11, 13, 17])

    def test_edge_one(self):
        # The smallest positive integer. Collatz sequence for 1 is [1]. Odd numbers are 1. Sorted: [1].
        self.assertEqual(get_odd_collatz(1), [1])

    def test_edge_two(self):
        # An even number that quickly reaches 1. Collatz sequence for 2 is [2, 1]. Odd numbers are 1. Sorted: [1].
        self.assertEqual(get_odd_collatz(2), [1])

    def test_error_zero(self):
        # n must be a positive integer (n >= 1).
        with self.assertRaises(ValueError):
            get_odd_collatz(0)

    def test_error_negative(self):
        # n must be a positive integer (n >= 1).
        with self.assertRaises(ValueError):
            get_odd_collatz(-5)

    def test_error_float(self):
        # n must be an integer.
        with self.assertRaises(TypeError):
            get_odd_collatz(3.14)

    def test_error_string(self):
        # n must be an integer.
        with self.assertRaises(TypeError):
            get_odd_collatz('abc')