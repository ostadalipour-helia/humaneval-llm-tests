import unittest
from sut.problem_HumanEval_104 import unique_digits

class TestUniqueDigits(unittest.TestCase):

    def test_example_one(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])

    def test_example_two(self):
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])

    def test_empty_list(self):
        self.assertEqual(unique_digits([]), [])

    def test_all_valid_numbers_unsorted(self):
        self.assertEqual(unique_digits([3, 1, 15, 13, 5]), [1, 3, 5, 13, 15])

    def test_all_invalid_numbers(self):
        self.assertEqual(unique_digits([2, 4, 6, 8, 10, 12]), [])

    def test_mixed_numbers_with_zero_digit(self):
        self.assertEqual(unique_digits([1, 10, 3, 123, 505, 7]), [1, 3, 7])

    def test_single_digit_numbers_only(self):
        self.assertEqual(unique_digits([1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 3, 5, 7, 9])

    def test_multi_digit_all_odd_numbers(self):
        self.assertEqual(unique_digits([135, 791, 317, 9]), [9, 135, 317, 791])

    def test_duplicates_of_valid_elements(self):
        self.assertEqual(unique_digits([1, 15, 33, 1, 15, 1422]), [1, 1, 15, 15, 33])

    def test_large_numbers_mixed_validity(self):
        self.assertEqual(unique_digits([13579, 24680, 97531, 111111, 2]), [13579, 97531, 111111])

if __name__ == '__main__':
    unittest.main()