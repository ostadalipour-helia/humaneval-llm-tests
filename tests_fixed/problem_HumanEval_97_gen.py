import unittest
from sut_llm.problem_HumanEval_97 import multiply

class TestMultiply(unittest.TestCase):

    def test_example_positive_numbers_1(self):
        self.assertEqual(multiply(148, 412), 16)

    def test_example_positive_numbers_2(self):
        self.assertEqual(multiply(19, 28), 72)

    def test_example_one_zero_unit_digit(self):
        self.assertEqual(multiply(2020, 1851), 0)

    def test_example_one_negative_number(self):
        self.assertEqual(multiply(14, -15), 20)

    def test_both_negative_numbers(self):
        self.assertEqual(multiply(-123, -456), 28)

    def test_single_digit_numbers(self):
        self.assertEqual(multiply(7, 8), 56)

    def test_single_digit_negative_and_positive(self):
        self.assertEqual(multiply(-3, 9), 63)

    def test_numbers_ending_in_one(self):
        self.assertEqual(multiply(101, 221), 1)

    def test_large_numbers_different_unit_digits(self):
        self.assertEqual(multiply(999999999, 1000000008), 72)

    def test_one_zero_unit_digit_and_negative(self):
        self.assertEqual(multiply(50, -17), 0)

if __name__ == '__main__':
    unittest.main()