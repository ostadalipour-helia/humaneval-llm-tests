import unittest
from sut.problem_HumanEval_103 import rounded_avg

class TestRoundedAvg(unittest.TestCase):

    def test_n_greater_than_m_boundary(self):
        """
        Test case where n is exactly one greater than m,
        triggering the n > m condition.
        """
        self.assertEqual(rounded_avg(2, 1), -1)

    def test_n_equals_m_single_element(self):
        """
        Test case where n equals m, representing a single-element range.
        This checks the boundary for the n > m condition and basic average.
        """
        self.assertEqual(rounded_avg(5, 5), "0b101") # avg = 5, bin = "0b101"

    def test_n_greater_than_m_general(self):
        """
        Test a general case where n is significantly greater than m,
        verifying the -1 return path. (From example)
        """
        self.assertEqual(rounded_avg(7, 5), -1)

    def test_typical_integer_average_odd_sum(self):
        """
        Test a typical scenario where the average is an exact integer
        and the sum (n+m) is even. (From example)
        """
        self.assertEqual(rounded_avg(1, 5), "0b11") # avg = (1+5)/2 = 3, bin = "0b11"

    def test_typical_integer_average_even_sum(self):
        """
        Test another typical scenario with a larger range where the average
        is an exact integer and the sum (n+m) is even. (From example)
        """
        self.assertEqual(rounded_avg(10, 20), "0b1111") # avg = (10+20)/2 = 15, bin = "0b1111"

    def test_rounding_up_half_odd_sum(self):
        """
        Test a case where the average ends in .5 and rounds up.
        This specifically checks the rounding behavior (0.5 rounds up). (From example)
        """
        self.assertEqual(rounded_avg(20, 33), "0b11010") # avg = (20+33)/2 = 26.5, rounds to 27, bin = "0b11010"

    def test_rounding_up_half_even_sum_mutation_check(self):
        """
        Test a case where the average ends in .5, but n+m is even.
        This is critical to catch mutations using Python's built-in `round()`
        which rounds to the nearest even number for .5 (e.g., round(2.5) -> 2).
        The docstring example implies standard rounding (0.5 always rounds up).
        """
        self.assertEqual(rounded_avg(1, 4), "0b11") # avg = (1+4)/2 = 2.5, should round to 3, bin = "0b11"

    def test_smallest_positive_inputs(self):
        """
        Test the smallest possible valid inputs for n and m (both 1).
        This is an edge case for minimum values.
        """
        self.assertEqual(rounded_avg(1, 1), "0b1") # avg = 1, bin = "0b1"

    def test_large_numbers_integer_average(self):
        """
        Test with very large numbers where the average is an exact integer.
        Checks for potential overflow issues or incorrect handling of large values.
        """
        self.assertEqual(rounded_avg(1000000, 1000000), "0b11110100001001000000") # avg = 1000000

    def test_large_numbers_rounding_up_half(self):
        """
        Test with very large numbers where the average ends in .5 and rounds up.
        Combines large number testing with rounding behavior.
        """
        self.assertEqual(rounded_avg(999999, 1000000), "0b11110100001001000000") # avg = 999999.5, rounds to 1000000