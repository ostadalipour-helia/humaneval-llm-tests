import unittest
from sut_llm.problem_HumanEval_163 import generate_integers

class TestGenerateIntegers(unittest.TestCase):

    def test_example_basic_ascending(self):
        self.assertEqual(generate_integers(2, 8), [2, 4, 6, 8])

    def test_example_basic_descending(self):
        self.assertEqual(generate_integers(8, 2), [2, 4, 6, 8])

    def test_example_no_single_digit_evens_in_range(self):
        self.assertEqual(generate_integers(10, 14), [])

    def test_single_even_digit(self):
        self.assertEqual(generate_integers(4, 4), [4])

    def test_single_odd_digit_no_evens(self):
        self.assertEqual(generate_integers(3, 3), [])

    def test_range_with_no_even_digits_between_odds(self):
        self.assertEqual(generate_integers(1, 1), [])

    def test_range_with_one_even_digit_between_odds(self):
        self.assertEqual(generate_integers(1, 3), [2])

    def test_full_single_digit_range(self):
        self.assertEqual(generate_integers(1, 9), [2, 4, 6, 8])

    def test_full_single_digit_range_reversed(self):
        self.assertEqual(generate_integers(9, 1), [2, 4, 6, 8])

    def test_range_crossing_ten_with_single_digit_evens(self):
        self.assertEqual(generate_integers(7, 12), [8])