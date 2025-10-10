import unittest
from sut_llm.problem_HumanEval_102 import choose_num

class TestChooseNum(unittest.TestCase):

    def test_docstring_example_1(self):
        self.assertEqual(choose_num(12, 15), 14)

    def test_docstring_example_2_invalid_range(self):
        self.assertEqual(choose_num(13, 12), -1)

    def test_range_x_equals_y_even(self):
        self.assertEqual(choose_num(10, 10), 10)

    def test_range_x_equals_y_odd(self):
        self.assertEqual(choose_num(11, 11), -1)

    def test_range_starts_odd_ends_odd_multiple_evens(self):
        self.assertEqual(choose_num(1, 5), 4)

    def test_range_starts_even_ends_even_multiple_evens(self):
        self.assertEqual(choose_num(2, 6), 6)

    def test_range_starts_odd_ends_even_single_even(self):
        self.assertEqual(choose_num(7, 8), 8)

    def test_range_starts_even_ends_odd_single_even(self):
        self.assertEqual(choose_num(8, 9), 8)

    def test_range_no_even_number_between_odds(self):
        self.assertEqual(choose_num(1, 1), -1)

    def test_range_large_numbers_multiple_evens(self):
        self.assertEqual(choose_num(99, 105), 104)

if __name__ == '__main__':
    unittest.main()