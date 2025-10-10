import unittest
from sut_llm.problem_HumanEval_97 import multiply

class TestMultiply(unittest.TestCase):

    def test_example_positive_multi_digit(self):
        # Typical/Expected input, verifies example 1
        self.assertEqual(multiply(148, 412), 16)

    def test_example_positive_two_digit(self):
        # Typical/Expected input, verifies example 2
        self.assertEqual(multiply(19, 28), 72)

    def test_example_one_zero_unit_digit(self):
        # Boundary condition: one unit digit is 0, verifies example 3
        self.assertEqual(multiply(2020, 1851), 0)

    def test_example_one_negative_number(self):
        # Sign testing: one negative input, verifies example 4. Crucial for `abs()` logic.
        self.assertEqual(multiply(14, -15), 20)

    def test_both_negative_numbers(self):
        # Sign testing: both negative inputs. Crucial for `abs()` logic.
        self.assertEqual(multiply(-13, -27), 21) # abs(3) * abs(7) = 21

    def test_unit_digits_are_one(self):
        # Boundary condition: unit digits are 1. Tests off-by-one from 0.
        self.assertEqual(multiply(11, 21), 1) # 1 * 1 = 1

    def test_unit_digits_are_nine(self):
        # Boundary condition: unit digits are 9. Tests maximum possible product (81).
        self.assertEqual(multiply(9, 19), 81) # 9 * 9 = 81

    def test_single_digit_numbers(self):
        # Edge case: inputs are single-digit numbers.
        self.assertEqual(multiply(5, 7), 35) # 5 * 7 = 35

    def test_one_input_is_zero(self):
        # Edge case: one input is exactly 0. Boundary condition for unit digit 0.
        self.assertEqual(multiply(0, 123), 0) # 0 * 3 = 0

    def test_large_numbers_different_unit_digits(self):
        # Extreme input: very large numbers with specific unit digits (1 and 9).
        self.assertEqual(multiply(987654321, 123456789), 9) # 1 * 9 = 9

if __name__ == '__main__':
    unittest.main()