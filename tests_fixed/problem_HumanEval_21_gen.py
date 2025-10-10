import unittest
from sut_llm.problem_HumanEval_21 import rescale_to_unit

class TestRescaleToUnit(unittest.TestCase):

    def test_01_basic_increasing_sequence(self):
        # Test with the example from the docstring
        # Coverage: Typical input, exact output verification.
        numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
        expected = [0.0, 0.25, 0.5, 0.75, 1.0]
        self.assertListEqual(rescale_to_unit(numbers), expected)

    def test_02_all_elements_are_same(self):
        # Test case where min_val == max_val, a critical boundary condition
        # All elements should map to 0.0.
        # Coverage: Boundary condition (min_val == max_val), logic mutation (division by zero).
        numbers = [5.0, 5.0, 5.0, 5.0]
        expected = [0.0, 0.0, 0.0, 0.0]
        self.assertListEqual(rescale_to_unit(numbers), expected)

    def test_03_exactly_two_elements(self):
        # Test with the minimum allowed number of elements (n=2)
        # Coverage: Boundary condition (minimum list length), off-by-one.
        numbers = [10.0, 20.0]
        expected = [0.0, 1.0]
        self.assertListEqual(rescale_to_unit(numbers), expected)

    def test_04_negative_numbers_only(self):
        # Test with a list containing only negative numbers
        # Coverage: Sign testing (negative values), typical input.
        numbers = [-5.0, -4.0, -3.0, -2.0, -1.0]
        expected = [0.0, 0.25, 0.5, 0.75, 1.0]
        self.assertListEqual(rescale_to_unit(numbers), expected)

    def test_05_mixed_positive_negative_and_zero(self):
        # Test with a list containing positive, negative, and zero values
        # Coverage: Sign testing (mixed), zero testing.
        numbers = [-10.0, 0.0, 10.0]
        expected = [0.0, 0.5, 1.0]
        self.assertListEqual(rescale_to_unit(numbers), expected)

    def test_06_decreasing_sequence(self):
        # Test with a list of numbers in decreasing order
        # Coverage: Logic mutation (order of elements), typical input.
        numbers = [5.0, 4.0, 3.0, 2.0, 1.0]
        expected = [1.0, 0.75, 0.5, 0.25, 0.0]
        self.assertListEqual(rescale_to_unit(numbers), expected)

    def test_07_min_max_not_at_ends_with_duplicates(self):
        # Test where min and max values are not at the start/end, and with duplicates
        # Coverage: Boundary (min/max position), edge case (duplicates), logic mutation.
        numbers = [3.0, 1.0, 5.0, 2.0, 5.0, 1.0]
        expected = [0.5, 0.0, 1.0, 0.25, 1.0, 0.0]
        self.assertListEqual(rescale_to_unit(numbers), expected)

    def test_08_extreme_large_float_values(self):
        # Test with very large floating-point numbers
        # Coverage: Extreme inputs, sign testing (large positive).
        numbers = [1000000.0, 2000000.0, 3000000.0]
        expected = [0.0, 0.5, 1.0]
        self.assertListEqual(rescale_to_unit(numbers), expected)

    def test_09_extreme_small_float_values_near_zero(self):
        # Test with very small floating-point numbers close to zero
        # Coverage: Extreme inputs, precision.
        numbers = [0.000001, 0.000002, 0.000003]
        expected = [0.0, 0.5, 1.0]
        actual = rescale_to_unit(numbers)

        self.assertEqual(len(actual), len(expected), "Lengths of rescaled list and expected list differ.")
        for i in range(len(expected)):
            # Use assertAlmostEqual for floating-point comparisons due to potential precision issues
            self.assertAlmostEqual(actual[i], expected[i], places=12, msg=f"Element at index {i} differs.")

    def test_10_two_identical_elements(self):
        # Test with exactly two identical elements (minimum length, all same)
        # Coverage: Boundary (min length), edge case (all same), off-by-one.
        numbers = [7.7, 7.7]
        expected = [0.0, 0.0]
        self.assertListEqual(rescale_to_unit(numbers), expected)