import unittest
from sut.problem_HumanEval_36 import fizz_buzz

class Test_fizz_buzz(unittest.TestCase):
    def test_normal_case_n50(self):
        """
        Numbers less than 50 divisible by 11 or 13 are: 11, 13, 22, 26, 33, 39, 44.
        None of these contain the digit '7'.
        """
        self.assertEqual(fizz_buzz(50), 0)

    def test_normal_case_n78(self):
        """
        Numbers less than 78 divisible by 11 or 13 include 77 (11 * 7).
        The number 77 contains two '7's. No other qualifying numbers in this range contain '7'.
        """
        self.assertEqual(fizz_buzz(78), 2)

    def test_normal_case_n100(self):
        """
        Numbers less than 100 divisible by 11 or 13 that contain the digit '7' are:
        77 (two '7's) and 91 (13 * 7, one '7'). The total count is 2 + 1 = 3.
        """
        self.assertEqual(fizz_buzz(100), 3)

    def test_edge_case_n0(self):
        """
        When n is 0, the range of integers (1 to n-1) is empty,
        so no numbers are checked and the count is 0.
        """
        self.assertEqual(fizz_buzz(0), 0)

    def test_edge_case_n1(self):
        """
        When n is 1, the range of integers (1 to n-1) is empty,
        so no numbers are checked and the count is 0.
        """
        self.assertEqual(fizz_buzz(1), 0)

    def test_edge_case_n10(self):
        """
        No numbers less than 10 are divisible by 11 or 13, so the count is 0.
        """
        self.assertEqual(fizz_buzz(10), 0)

    def test_edge_case_n77(self):
        """
        Numbers less than 77 divisible by 11 or 13 (e.g., 11, 13, ..., 66)
        do not contain the digit '7'. The number 77 itself is not included
        as it is not 'less than n'.
        """
        self.assertEqual(fizz_buzz(77), 0)

    def test_error_case_n_string(self):
        """
        Input 'n' must be an integer.
        """
        with self.assertRaises(TypeError):
            fizz_buzz("invalid")

    def test_error_case_n_float(self):
        """
        Input 'n' must be an integer.
        """
        with self.assertRaises(TypeError):
            fizz_buzz(7.5)

    def test_error_case_n_none(self):
        """
        Input 'n' must be an integer.
        """
        with self.assertRaises(TypeError):
            fizz_buzz(None)