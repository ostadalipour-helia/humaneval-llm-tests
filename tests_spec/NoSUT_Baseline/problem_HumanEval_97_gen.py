import unittest
import sut.problem_HumanEval_97 as mod

class TestHybrid(unittest.TestCase):
    def test_example_positive_two_digit(self):
            # Typical/Expected input, verifies example 2
            self.assertEqual(mod.multiply(19, 28), 72)

    def test_example_one_zero_unit_digit(self):
            # Boundary condition: one unit digit is 0, verifies example 3
            self.assertEqual(mod.multiply(2020, 1851), 0)

    def test_example_one_negative_number(self):
            # Sign testing: one negative input, verifies example 4. Crucial for `abs()` logic.
            self.assertEqual(mod.multiply(14, -15), 20)

    def test_both_negative_numbers(self):
            # Sign testing: both negative inputs. Crucial for `abs()` logic.
            self.assertEqual(mod.multiply(-13, -27), 21) # abs(3) * abs(7) = 21

    def test_unit_digits_are_one(self):
            # Boundary condition: unit digits are 1. Tests off-by-one from 0.
            self.assertEqual(mod.multiply(11, 21), 1) # 1 * 1 = 1

    def test_unit_digits_are_nine(self):
            # Boundary condition: unit digits are 9. Tests maximum possible product (81).
            self.assertEqual(mod.multiply(9, 19), 81) # 9 * 9 = 81

    def test_single_digit_numbers(self):
            # Edge case: inputs are single-digit numbers.
            self.assertEqual(mod.multiply(5, 7), 35) # 5 * 7 = 35

    def test_one_input_is_zero(self):
            # Edge case: one input is exactly 0. Boundary condition for unit digit 0.
            self.assertEqual(mod.multiply(0, 123), 0) # 0 * 3 = 0

    def test_large_numbers_different_unit_digits(self):
            # Extreme input: very large numbers with specific unit digits (1 and 9).
            self.assertEqual(mod.multiply(987654321, 123456789), 9) # 1 * 9 = 9
    
    if __name__ == '__main__':
        unittest.main()

    def test_normal_case_1(self):
            # Unit digit of 148 is 8. Unit digit of 412 is 2. Product is 8 * 2 = 16.
            self.assertEqual(mod.multiply(148, 412), 16)

    def test_normal_case_2(self):
            # Unit digit of 19 is 9. Unit digit of 28 is 8. Product is 9 * 8 = 72.
            self.assertEqual(mod.multiply(19, 28), 72)

    def test_normal_case_3(self):
            # Unit digit of 2020 is 0. Unit digit of 1851 is 1. Product is 0 * 1 = 0.
            self.assertEqual(mod.multiply(2020, 1851), 0)

    def test_edge_case_negative_b(self):
            # Unit digit of 14 is 4. Unit digit of -15 is 5 (since -15 % 10 = 5 in Python). Product is 4 * 5 = 20.
            self.assertEqual(mod.multiply(14, -15), 20)

    def test_edge_case_single_digits(self):
            # Single-digit numbers. Unit digit of 5 is 5. Unit digit of 7 is 7. Product is 5 * 7 = 35.
            self.assertEqual(mod.multiply(5, 7), 35)

    def test_edge_case_zero_and_hundred(self):
            # One number is zero. Unit digit of 0 is 0. Unit digit of 100 is 0. Product is 0 * 0 = 0.
            self.assertEqual(mod.multiply(0, 100), 0)

    def test_edge_case_both_negative(self):
            # Both numbers are negative. Unit digit of -1 is 9 (since -1 % 10 = 9 in Python). Product is 9 * 9 = 81.
            self.assertEqual(mod.multiply(-1, -1), 81)

