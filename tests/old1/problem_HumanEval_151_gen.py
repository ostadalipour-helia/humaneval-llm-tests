import unittest
from sut.problem_HumanEval_151 import double_the_difference

class TestDoubleTheDifference(unittest.TestCase):

    def test_example_basic_positive_odds(self):
        self.assertEqual(double_the_difference([1, 3, 2, 0]), 10)

    def test_example_all_negative_numbers(self):
        self.assertEqual(double_the_difference([-1, -2, 0]), 0)

    def test_example_mixed_positive_odd_and_negative(self):
        self.assertEqual(double_the_difference([9, -2]), 81)

    def test_example_single_even_number(self):
        self.assertEqual(double_the_difference([0]), 0)

    def test_empty_list(self):
        self.assertEqual(double_the_difference([]), 0)

    def test_list_with_only_even_positive_numbers(self):
        self.assertEqual(double_the_difference([2, 4, 6, 8]), 0)

    def test_list_with_mixed_types_and_valid_integers(self):
        self.assertEqual(double_the_difference([1, 2.5, 3, "hello", 5]), 35)

    def test_list_with_large_odd_numbers(self):
        self.assertEqual(double_the_difference([11, 13]), 290)

    def test_list_with_zero_and_negative_odd_numbers(self):
        self.assertEqual(double_the_difference([0, -3, -5, 7]), 49)

    def test_list_with_only_one_positive_odd_number(self):
        self.assertEqual(double_the_difference([17]), 289)

if __name__ == '__main__':
    unittest.main()