import unittest
from sut_llm.problem_HumanEval_65 import circular_shift

class TestCircularShift(unittest.TestCase):

    def test_example_basic_shift(self):
        self.assertEqual(circular_shift(12, 1), "21")

    def test_example_full_shift(self):
        self.assertEqual(circular_shift(12, 2), "12")

    def test_shift_greater_than_digits_simple(self):
        self.assertEqual(circular_shift(12, 3), "21")

    def test_shift_greater_than_digits_complex(self):
        self.assertEqual(circular_shift(12345, 6), "54321")

    def test_zero_shift(self):
        self.assertEqual(circular_shift(9876, 0), "9876")

    def test_single_digit_number_zero_shift(self):
        self.assertEqual(circular_shift(7, 0), "7")

    def test_single_digit_number_any_shift(self):
        self.assertEqual(circular_shift(7, 5), "7")

    def test_multi_digit_partial_shift(self):
        self.assertEqual(circular_shift(12345, 3), "34512")

    def test_number_with_zero_digit_partial_shift(self):
        self.assertEqual(circular_shift(102, 1), "210")

    def test_number_with_zero_digit_full_shift(self):
        self.assertEqual(circular_shift(102, 3), "102")

if __name__ == '__main__':
    unittest.main()