import unittest
from sut.problem_HumanEval_123 import get_odd_collatz

class TestGetOddCollatz(unittest.TestCase):

    def test_n_is_one_boundary_case(self):
        # Boundary: Smallest positive integer, explicit base case.
        # Sequence for 1 is [1]. Odd numbers: [1].
        self.assertListEqual(get_odd_collatz(1), [1])

    def test_n_is_two_smallest_even(self):
        # Boundary: Smallest even number.
        # Sequence for 2 is [2, 1]. Odd numbers: [1].
        self.assertListEqual(get_odd_collatz(2), [1])

    def test_n_is_three_smallest_odd_greater_than_one(self):
        # Boundary: Smallest odd number > 1, leads to a longer sequence.
        # Sequence for 3 is [3, 10, 5, 16, 8, 4, 2, 1]. Odd numbers: [1, 3, 5].
        self.assertListEqual(get_odd_collatz(3), [1, 3, 5])

    def test_n_is_four_power_of_two_edge_case(self):
        # Edge Case: Power of two, sequence quickly reaches 1, only 1 is odd.
        # Sequence for 4 is [4, 2, 1]. Odd numbers: [1].
        self.assertListEqual(get_odd_collatz(4), [1])

    def test_n_is_five_docstring_example(self):
        # Typical Input: Example from docstring.
        # Sequence for 5 is [5, 16, 8, 4, 2, 1]. Odd numbers: [1, 5].
        self.assertListEqual(get_odd_collatz(5), [1, 5])

    def test_n_is_six_even_leading_to_odd(self):
        # Typical Input: Even number that leads to an odd number other than 1.
        # Sequence for 6 is [6, 3, 10, 5, 16, 8, 4, 2, 1]. Odd numbers: [1, 3, 5].
        self.assertListEqual(get_odd_collatz(6), [1, 3, 5])

    def test_n_is_seven_longer_sequence(self):
        # Typical Input: Odd number leading to a moderately long sequence.
        # Sequence for 7 is [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1].
        # Odd numbers: [1, 5, 7, 11, 13, 17].
        self.assertListEqual(get_odd_collatz(7), [1, 5, 7, 11, 13, 17])

    def test_n_is_eight_another_power_of_two(self):
        # Edge Case: Another power of two, only 1 is odd.
        # Sequence for 8 is [8, 4, 2, 1]. Odd numbers: [1].
        self.assertListEqual(get_odd_collatz(8), [1])

    def test_n_large_odd_extreme_long_sequence(self):
        # Extreme Input: A known number (27) that generates a very long Collatz sequence.
        # Odd numbers in sequence for 27: [1, 5, 7, 11, 13, 17, 23, 27, 31, 35, 41, 47, 53, 61, 71, 91, 103, 107, 115, 121, 137, 155, 161, 167, 175, 205, 233, 251, 263, 283, 319, 325, 377, 395, 425, 433, 445, 479, 577, 593, 911, 1079, 1367, 1619, 2051, 2429, 3077].
        expected_odds = [1, 5, 7, 11, 13, 17, 23, 27, 31, 35, 41, 47, 53, 61, 71, 91, 103, 107, 115, 121, 137, 155, 161, 167, 175, 205, 233, 251, 263, 283, 319, 325, 377, 395, 425, 433, 445, 479, 577, 593, 911, 1079, 1367, 1619, 2051, 2429, 3077]
        self.assertListEqual(get_odd_collatz(27), expected_odds)

    def test_n_large_even_extreme_input(self):
        # Extreme Input: A moderately large even number.
        # Sequence for 100 is [100, 50, 25, 76, 38, 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1].
        # Odd numbers: [1, 5, 11, 13, 17, 19, 25, 29].
        self.assertListEqual(get_odd_collatz(100), [1, 5, 11, 13, 17, 19, 25, 29])