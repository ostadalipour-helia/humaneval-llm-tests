import unittest
import sut.problem_HumanEval_104 as mod

class TestHybrid(unittest.TestCase):
    def test_docstring_example_1(self):
            # Typical input, verifies filtering and sorting
            self.assertListEqual(mod.unique_digits([15, 33, 1422, 1]), [1, 15, 33])

    def test_docstring_example_2(self):
            # Typical input, verifies all elements are filtered out (includes 0 as even digit)
            self.assertListEqual(mod.unique_digits([152, 323, 1422, 10]), [])

    def test_empty_list(self):
            # Edge case: empty input list
            self.assertListEqual(mod.unique_digits([]), [])

    def test_single_element_valid(self):
            # Edge case: single element, all odd digits
            self.assertListEqual(mod.unique_digits([13579]), [13579])

    def test_single_element_invalid(self):
            # Edge case: single element, all even digits
            self.assertListEqual(mod.unique_digits([2468]), [])

    def test_all_valid_elements_unsorted(self):
            # Boundary test: all elements qualify, requires sorting
            self.assertListEqual(mod.unique_digits([9, 1, 3, 7, 5]), [1, 3, 5, 7, 9])

    def test_all_invalid_elements_mixed_even_odd(self):
            # Boundary test: all elements contain at least one even digit
            self.assertListEqual(mod.unique_digits([12, 34, 56, 78, 90]), [])

    def test_duplicates_and_sorting(self):
            # Edge case: input with duplicate qualifying elements, verifies preservation and sorting
            self.assertListEqual(mod.unique_digits([15, 1, 33, 15, 1, 22]), [1, 1, 15, 15, 33])

    def test_normal_case_basic(self):
            # Normal case with a mix of qualifying and non-qualifying numbers
            x = [15, 33, 1422, 1]
            expected_output = [1, 15, 33]
            self.assertEqual(mod.unique_digits(x), expected_output)

    def test_normal_case_no_matches(self):
            # Normal case where no numbers qualify
            x = [152, 323, 1422, 10]
            expected_output = []
            self.assertEqual(mod.unique_digits(x), expected_output)

    def test_normal_case_all_matches(self):
            # Normal case where all numbers qualify
            x = [1, 3, 5, 7, 9]
            expected_output = [1, 3, 5, 7, 9]
            self.assertEqual(mod.unique_digits(x), expected_output)

    def test_edge_case_empty_list(self):
            # Edge case: empty input list
            x = []
            expected_output = []
            self.assertEqual(mod.unique_digits(x), expected_output)

    def test_edge_case_duplicates(self):
            # Edge case: input list contains duplicate qualifying numbers
            x = [15, 1, 33, 15]
            expected_output = [1, 15, 15, 33]
            self.assertEqual(mod.unique_digits(x), expected_output)

    def test_error_input_not_list(self):
            # Error case: input `x` is not a list (e.g., None)
            with self.assertRaises(TypeError):
                mod.unique_digits(None)

    def test_error_list_contains_negative(self):
            # Error case: list `x` contains non-positive integers (negative)
            with self.assertRaises(ValueError):
                mod.unique_digits([1, -5, 3])

