import unittest
import sut.problem_HumanEval_21 as mod

class TestHybrid(unittest.TestCase):
    def test_01_basic_increasing_sequence(self):
            # Test with the example from the docstring
            # Coverage: Typical input, exact output verification.
            numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
            expected = [0.0, 0.25, 0.5, 0.75, 1.0]
            self.assertListEqual(mod.rescale_to_unit(numbers), expected)

    def test_03_exactly_two_elements(self):
            # Test with the minimum allowed number of elements (n=2)
            # Coverage: Boundary condition (minimum list length), off-by-one.
            numbers = [10.0, 20.0]
            expected = [0.0, 1.0]
            self.assertListEqual(mod.rescale_to_unit(numbers), expected)

    def test_04_negative_numbers_only(self):
            # Test with a list containing only negative numbers
            # Coverage: Sign testing (negative values), typical input.
            numbers = [-5.0, -4.0, -3.0, -2.0, -1.0]
            expected = [0.0, 0.25, 0.5, 0.75, 1.0]
            self.assertListEqual(mod.rescale_to_unit(numbers), expected)

    def test_05_mixed_positive_negative_and_zero(self):
            # Test with a list containing positive, negative, and zero values
            # Coverage: Sign testing (mixed), zero testing.
            numbers = [-10.0, 0.0, 10.0]
            expected = [0.0, 0.5, 1.0]
            self.assertListEqual(mod.rescale_to_unit(numbers), expected)

    def test_06_decreasing_sequence(self):
            # Test with a list of numbers in decreasing order
            # Coverage: Logic mutation (order of elements), typical input.
            numbers = [5.0, 4.0, 3.0, 2.0, 1.0]
            expected = [1.0, 0.75, 0.5, 0.25, 0.0]
            self.assertListEqual(mod.rescale_to_unit(numbers), expected)

    def test_07_min_max_not_at_ends_with_duplicates(self):
            # Test where min and max values are not at the start/end, and with duplicates
            # Coverage: Boundary (min/max position), edge case (duplicates), logic mutation.
            numbers = [3.0, 1.0, 5.0, 2.0, 5.0, 1.0]
            expected = [0.5, 0.0, 1.0, 0.25, 1.0, 0.0]
            self.assertListEqual(mod.rescale_to_unit(numbers), expected)

    def test_08_extreme_large_float_values(self):
            # Test with very large floating-point numbers
            # Coverage: Extreme inputs, sign testing (large positive).
            numbers = [1000000.0, 2000000.0, 3000000.0]
            expected = [0.0, 0.5, 1.0]
            self.assertListEqual(mod.rescale_to_unit(numbers), expected)

    def test_empty_list_error(self):
            numbers = []
            with self.assertRaises((ValueError, IndexError)):
                mod.rescale_to_unit(numbers)

    def test_list_of_strings_error(self):
            numbers = ["a", "b", "c"]
            with self.assertRaises(TypeError):
                mod.rescale_to_unit(numbers)

