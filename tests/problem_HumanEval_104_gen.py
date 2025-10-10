import unittest
from sut.problem_HumanEval_104 import unique_digits

class TestUniqueDigits(unittest.TestCase):

    def test_docstring_example_1(self):
        # Typical input, verifies filtering and sorting
        self.assertListEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])

    def test_docstring_example_2(self):
        # Typical input, verifies all elements are filtered out (includes 0 as even digit)
        self.assertListEqual(unique_digits([152, 323, 1422, 10]), [])

    def test_empty_list(self):
        # Edge case: empty input list
        self.assertListEqual(unique_digits([]), [])

    def test_single_element_valid(self):
        # Edge case: single element, all odd digits
        self.assertListEqual(unique_digits([13579]), [13579])

    def test_single_element_invalid(self):
        # Edge case: single element, all even digits
        self.assertListEqual(unique_digits([2468]), [])

    def test_all_valid_elements_unsorted(self):
        # Boundary test: all elements qualify, requires sorting
        self.assertListEqual(unique_digits([9, 1, 3, 7, 5]), [1, 3, 5, 7, 9])

    def test_all_invalid_elements_mixed_even_odd(self):
        # Boundary test: all elements contain at least one even digit
        self.assertListEqual(unique_digits([12, 34, 56, 78, 90]), [])

    def test_numbers_with_zero_digit(self):
        # Logic mutation test: specifically checks 0 as an even digit, mixed valid/invalid
        self.assertListEqual(unique_digits([10, 23, 305, 11, 4]), [11, 23])

    def test_large_numbers_mixed(self):
        # Extreme input: large numbers, mix of all odd, all even, and mixed digits
        self.assertListEqual(unique_digits([13579, 24680, 111111111, 987654321]), [111111111, 13579])

    def test_duplicates_and_sorting(self):
        # Edge case: input with duplicate qualifying elements, verifies preservation and sorting
        self.assertListEqual(unique_digits([15, 1, 33, 15, 1, 22]), [1, 1, 15, 15, 33])