import unittest
from sut_llm.problem_HumanEval_138 import is_equal_to_sum_even

class TestIsEqualToSumEven(unittest.TestCase):

    def test_minimum_valid_sum(self):
        self.assertTrue(is_equal_to_sum_even(8))

    def test_example_too_small_4(self):
        self.assertFalse(is_equal_to_sum_even(4))

    def test_example_too_small_6(self):
        self.assertFalse(is_equal_to_sum_even(6))

    def test_valid_sum_10(self):
        self.assertTrue(is_equal_to_sum_even(10))

    def test_valid_sum_12(self):
        self.assertTrue(is_equal_to_sum_even(12))

    def test_odd_number_too_small(self):
        self.assertFalse(is_equal_to_sum_even(7))

    def test_odd_number_greater_than_min(self):
        self.assertFalse(is_equal_to_sum_even(9))

    def test_even_number_too_small(self):
        self.assertFalse(is_equal_to_sum_even(2))

    def test_larger_valid_sum(self):
        self.assertTrue(is_equal_to_sum_even(16))

    def test_zero_input(self):
        self.assertFalse(is_equal_to_sum_even(0))

if __name__ == '__main__':
    unittest.main()