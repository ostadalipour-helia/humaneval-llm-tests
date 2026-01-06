import unittest
import sut.problem_HumanEval_103 as mod

class TestHybrid(unittest.TestCase):
    def test_n_greater_than_m_boundary(self):
            """
            Test case where n is exactly one greater than m,
            triggering the n > m condition.
            """
            self.assertEqual(mod.rounded_avg(2, 1), -1)

    def test_n_equals_m_single_element(self):
            """
            Test case where n equals m, representing a single-element range.
            This checks the boundary for the n > m condition and basic average.
            """
            self.assertEqual(mod.rounded_avg(5, 5), "0b101") # avg = 5, bin = "0b101"

    def test_n_greater_than_m_general(self):
            """
            Test a general case where n is significantly greater than m,
            verifying the -1 return path. (From example)
            """
            self.assertEqual(mod.rounded_avg(7, 5), -1)

    def test_typical_integer_average_odd_sum(self):
            """
            Test a typical scenario where the average is an exact integer
            and the sum (n+m) is even. (From example)
            """
            self.assertEqual(mod.rounded_avg(1, 5), "0b11") # avg = (1+5)/2 = 3, bin = "0b11"

    def test_typical_integer_average_even_sum(self):
            """
            Test another typical scenario with a larger range where the average
            is an exact integer and the sum (n+m) is even. (From example)
            """
            self.assertEqual(mod.rounded_avg(10, 20), "0b1111") # avg = (10+20)/2 = 15, bin = "0b1111"

    def test_rounding_up_half_odd_sum(self):
            """
            Test a case where the average ends in .5 and rounds up.
            This specifically checks the rounding behavior (0.5 rounds up). (From example)
            """
            self.assertEqual(mod.rounded_avg(20, 33), "0b11010") # avg = (20+33)/2 = 26.5, rounds to 27, bin = "0b11010"

    def test_smallest_positive_inputs(self):
            """
            Test the smallest possible valid inputs for n and m (both 1).
            This is an edge case for minimum values.
            """
            self.assertEqual(mod.rounded_avg(1, 1), "0b1") # avg = 1, bin = "0b1"

    def test_large_numbers_integer_average(self):
            """
            Test with very large numbers where the average is an exact integer.
            Checks for potential overflow issues or incorrect handling of large values.
            """
            self.assertEqual(mod.rounded_avg(1000000, 1000000), "0b11110100001001000000") # avg = 1000000

    def test_large_numbers_rounding_up_half(self):
            """
            Test with very large numbers where the average ends in .5 and rounds up.
            Combines large number testing with rounding behavior.
            """
            self.assertEqual(mod.rounded_avg(999999, 1000000), "0b11110100001001000000") # avg = 999999.5, rounds to 1000000

    def test_normal_case_1_to_5(self):
            # Average of 1,2,3,4,5 is 3. Rounded is 3. Binary is 0b11.
            self.assertEqual(mod.rounded_avg(1, 5), "0b11")

    def test_normal_case_10_to_20(self):
            # Average of 10..20 is 15. Rounded is 15. Binary is 0b1111.
            self.assertEqual(mod.rounded_avg(10, 20), "0b1111")

    def test_normal_case_20_to_33_rounds_up(self):
            # Average of 20..33 is 26.5. Rounded is 27. Binary is 0b11010.
            self.assertEqual(mod.rounded_avg(20, 33), "0b11010")
    
        # Edge Cases

    def test_edge_n_greater_than_m(self):
            # n is greater than m, so -1 is returned.
            self.assertEqual(mod.rounded_avg(7, 5), -1)

    def test_edge_n_equals_m_one(self):
            # n equals m, average is 1. Rounded is 1. Binary is 0b1.
            self.assertEqual(mod.rounded_avg(1, 1), "0b1")

    def test_edge_average_rounds_up_point_5(self):
            # Average of 1,2 is 1.5. Rounded is 2. Binary is 0b10.
            self.assertEqual(mod.rounded_avg(1, 2), "0b10")

    def test_edge_average_exact_integer(self):
            # Average of 3,4,5 is 4. Rounded is 4. Binary is 0b100.
            self.assertEqual(mod.rounded_avg(3, 5), "0b100")
    
        # Error Cases (Preconditions: n, m are positive integers)

    def test_error_m_not_int_float(self):
            # m is not an integer.
            with self.assertRaises(TypeError):
                mod.rounded_avg(1, 5.0) # Using 5.0 instead of "xyz" to show float type error

