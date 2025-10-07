import unittest
from sut_llm.problem_HumanEval_4 import mean_absolute_deviation

class TestMeanAbsoluteDeviation(unittest.TestCase):

    def test_docstring_example(self):
        numbers = [1.0, 2.0, 3.0, 4.0]
        expected_mad = 1.0
        self.assertAlmostEqual(mean_absolute_deviation(numbers), expected_mad, places=7)

    def test_single_element_list(self):
        numbers = [5.0]
        expected_mad = 0.0
        self.assertAlmostEqual(mean_absolute_deviation(numbers), expected_mad, places=7)

    def test_all_same_elements(self):
        numbers = [7.0, 7.0, 7.0, 7.0, 7.0]
        expected_mad = 0.0
        self.assertAlmostEqual(mean_absolute_deviation(numbers), expected_mad, places=7)

    def test_negative_numbers(self):
        numbers = [-1.0, -2.0, -3.0, -4.0]
        expected_mad = 1.0
        self.assertAlmostEqual(mean_absolute_deviation(numbers), expected_mad, places=7)

    def test_mixed_positive_and_negative(self):
        numbers = [-1.0, 0.0, 1.0]
        expected_mad = 2/3
        self.assertAlmostEqual(mean_absolute_deviation(numbers), expected_mad, places=7)

    def test_decimal_numbers_simple(self):
        numbers = [0.5, 1.5, 2.5]
        expected_mad = 2/3
        self.assertAlmostEqual(mean_absolute_deviation(numbers), expected_mad, places=7)

    def test_larger_numbers(self):
        numbers = [100.0, 200.0, 300.0, 400.0]
        expected_mad = 100.0
        self.assertAlmostEqual(mean_absolute_deviation(numbers), expected_mad, places=7)

    def test_even_elements_non_integer_mean(self):
        numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
        expected_mad = 1.5
        self.assertAlmostEqual(mean_absolute_deviation(numbers), expected_mad, places=7)

    def test_odd_elements_integer_mean(self):
        numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
        expected_mad = 1.2
        self.assertAlmostEqual(mean_absolute_deviation(numbers), expected_mad, places=7)

    def test_zero_values(self):
        numbers = [0.0, 0.0, 0.0, 0.0, 0.0]
        expected_mad = 0.0
        self.assertAlmostEqual(mean_absolute_deviation(numbers), expected_mad, places=7)

    def test_mad_with_two_elements(self):
        # This test provides a non-empty list, ensuring line 14 (mean calculation) is executed.
        numbers = [0.0, 2.0]
        expected_mad = 1.0
        result = mean_absolute_deviation(numbers)
        self.assertAlmostEqual(result, expected_mad)

    def test_mad_with_mixed_numbers(self):
        # This test also provides a non-empty list, covering line 14 with mixed positive/negative values.
        numbers = [1.0, -1.0]
        expected_mad = 1.0
        result = mean_absolute_deviation(numbers)
        self.assertAlmostEqual(result, expected_mad)

    def test_mad_with_float_numbers(self):
        # Another test with a non-empty list of floats, executing line 14.
        numbers = [1.5, 2.5, 3.5]
        expected_mad = 2.0 / 3.0
        result = mean_absolute_deviation(numbers)
        self.assertAlmostEqual(result, expected_mad)

if __name__ == '__main__':
    unittest.main()