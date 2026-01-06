import unittest
from sut.problem_HumanEval_103 import rounded_avg

class Test_rounded_avg(unittest.TestCase):

    # Normal Cases
    def test_normal_case_1_to_5(self):
        # Average of 1,2,3,4,5 is 3. Rounded is 3. Binary is 0b11.
        self.assertEqual(rounded_avg(1, 5), "0b11")

    def test_normal_case_10_to_20(self):
        # Average of 10..20 is 15. Rounded is 15. Binary is 0b1111.
        self.assertEqual(rounded_avg(10, 20), "0b1111")

    def test_normal_case_20_to_33_rounds_up(self):
        # Average of 20..33 is 26.5. Rounded is 27. Binary is 0b11010.
        self.assertEqual(rounded_avg(20, 33), "0b11010")

    # Edge Cases
    def test_edge_n_greater_than_m(self):
        # n is greater than m, so -1 is returned.
        self.assertEqual(rounded_avg(7, 5), -1)

    def test_edge_n_equals_m_one(self):
        # n equals m, average is 1. Rounded is 1. Binary is 0b1.
        self.assertEqual(rounded_avg(1, 1), "0b1")

    def test_edge_average_rounds_up_point_5(self):
        # Average of 1,2 is 1.5. Rounded is 2. Binary is 0b10.
        self.assertEqual(rounded_avg(1, 2), "0b10")

    def test_edge_average_exact_integer(self):
        # Average of 3,4,5 is 4. Rounded is 4. Binary is 0b100.
        self.assertEqual(rounded_avg(3, 5), "0b100")

    # Error Cases (Preconditions: n, m are positive integers)
    def test_error_n_zero(self):
        # n is not a positive integer.
        with self.assertRaises(ValueError):
            rounded_avg(0, 5)

    def test_error_m_negative(self):
        # m is not a positive integer.
        with self.assertRaises(ValueError):
            rounded_avg(1, -5)

    def test_error_n_not_int_string(self):
        # n is not an integer.
        with self.assertRaises(TypeError):
            rounded_avg("abc", 5)

    def test_error_m_not_int_float(self):
        # m is not an integer.
        with self.assertRaises(TypeError):
            rounded_avg(1, 5.0) # Using 5.0 instead of "xyz" to show float type error