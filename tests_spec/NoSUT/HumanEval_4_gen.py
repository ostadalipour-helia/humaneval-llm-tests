import unittest
from sut.problem_HumanEval_4 import mean_absolute_deviation

class Test_mean_absolute_deviation(unittest.TestCase):

    def test_normal_sequence_positive_floats(self):
        # Example from the docstring: a simple sequence of positive floats.
        numbers = [1.0, 2.0, 3.0, 4.0]
        expected_mad = 1.0
        self.assertAlmostEqual(mean_absolute_deviation(numbers), expected_mad, places=10)

    def test_normal_three_positive_floats_non_int_mean(self):
        # A list of three positive floats with a non-integer mean.
        numbers = [10.0, 20.0, 30.0]
        expected_mad = 6.666666666666667
        self.assertAlmostEqual(mean_absolute_deviation(numbers), expected_mad, places=10)

    def test_normal_mixed_sign_floats(self):
        # A list including negative, zero, and positive floats.
        numbers = [-1.0, 0.0, 1.0]
        expected_mad = 0.6666666666666666
        self.assertAlmostEqual(mean_absolute_deviation(numbers), expected_mad, places=10)

    def test_edge_single_element_list(self):
        # A list with a single element. MAD should be 0 as x - mean = 0.
        numbers = [5.0]
        expected_mad = 0.0
        self.assertAlmostEqual(mean_absolute_deviation(numbers), expected_mad, places=10)

    def test_edge_all_elements_identical(self):
        # A list where all elements are identical. MAD should be 0.
        numbers = [2.5, 2.5, 2.5]
        expected_mad = 0.0
        self.assertAlmostEqual(mean_absolute_deviation(numbers), expected_mad, places=10)

    def test_edge_all_zeros(self):
        # A list of all zeros. MAD should be 0.
        numbers = [0.0, 0.0, 0.0, 0.0]
        expected_mad = 0.0
        self.assertAlmostEqual(mean_absolute_deviation(numbers), expected_mad, places=10)

    def test_edge_only_negative_numbers(self):
        # A list of only negative numbers.
        numbers = [-5.0, -4.0, -3.0, -2.0, -1.0]
        expected_mad = 1.2
        self.assertAlmostEqual(mean_absolute_deviation(numbers), expected_mad, places=10)

    def test_error_empty_list(self):
        # Input list is empty. Should raise an error (e.g., ValueError or ZeroDivisionError).
        numbers = []
        with self.assertRaises((ValueError, ZeroDivisionError)):
            mean_absolute_deviation(numbers)

    def test_error_list_of_integers(self):
        # Input list contains integers instead of floats (violates type hint).
        # This assumes the function does not implicitly convert integers to floats
        # or that type checking raises an error.
        numbers = [1, 2, 3]
        with self.assertRaises(TypeError):
            mean_absolute_deviation(numbers)

    def test_error_list_with_non_numeric(self):
        # Input list contains non-numeric elements.
        numbers = [1.0, 'a', 3.0]
        with self.assertRaises(TypeError):
            mean_absolute_deviation(numbers)