import unittest
from sut_llm.problem_HumanEval_4 import mean_absolute_deviation

class TestMeanAbsoluteDeviation(unittest.TestCase):

    def test_docstring_example(self):
        # CRITICAL: Typical/Expected Input, Exact Output
        # Mean = (1.0 + 2.0 + 3.0 + 4.0) / 4 = 2.5
        # Abs diffs: |1.0-2.5|=1.5, |2.0-2.5|=0.5, |3.0-2.5|=0.5, |4.0-2.5|=1.5
        # MAD = (1.5 + 0.5 + 0.5 + 1.5) / 4 = 4.0 / 4 = 1.0
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

    def test_single_element_list(self):
        # CRITICAL: Edge Case (single element), Boundary Testing (min list size > 0), Exact Output
        # Mean = 5.0
        # Abs diffs: |5.0-5.0|=0.0
        # MAD = 0.0 / 1 = 0.0
        self.assertEqual(mean_absolute_deviation([5.0]), 0.0)

    def test_all_same_elements(self):
        # CRITICAL: Edge Case (all identical values), Boundary Testing (MAD=0), Exact Output
        # Mean = 7.0
        # Abs diffs: |7.0-7.0|=0.0 for all elements
        # MAD = 0.0 / 4 = 0.0
        self.assertEqual(mean_absolute_deviation([7.0, 7.0, 7.0, 7.0]), 0.0)

    def test_empty_list_raises_error(self):
        # CRITICAL: Edge Case (empty list), Boundary Testing (min list size), Error Handling
        # Calculating the mean of an empty list typically raises ZeroDivisionError.
        # However, the function explicitly raises ValueError for an empty list.
        with self.assertRaises(ValueError):
            mean_absolute_deviation([])

    def test_two_elements_positive(self):
        # CRITICAL: Boundary Testing (two elements), Typical Input, Exact Output
        # Mean = (1.0 + 3.0) / 2 = 2.0
        # Abs diffs: |1.0-2.0|=1.0, |3.0-2.0|=1.0
        # MAD = (1.0 + 1.0) / 2 = 1.0
        self.assertEqual(mean_absolute_deviation([1.0, 3.0]), 1.0)

    def test_mixed_positive_negative(self):
        # CRITICAL: Sign Testing (mixed signs), Logic Mutation (abs() behavior), Exact Output
        # Mean = (-1.0 + 1.0) / 2 = 0.0
        # Abs diffs: |-1.0-0.0|=1.0, |1.0-0.0|=1.0
        # MAD = (1.0 + 1.0) / 2 = 1.0
        self.assertEqual(mean_absolute_deviation([-1.0, 1.0]), 1.0)

    def test_mixed_positive_negative_zero(self):
        # CRITICAL: Sign Testing (mixed signs including zero), Extreme/Unusual Input, Exact Output
        # Mean = (-2.0 + 0.0 + 2.0 + 4.0) / 4 = 4.0 / 4 = 1.0
        # Abs diffs: |-2.0-1.0|=3.0, |0.0-1.0|=1.0, |2.0-1.0|=1.0, |4.0-1.0|=3.0
        # MAD = (3.0 + 1.0 + 1.0 + 3.0) / 4 = 8.0 / 4 = 2.0
        self.assertEqual(mean_absolute_deviation([-2.0, 0.0, 2.0, 4.0]), 2.0)

    def test_large_numbers_exact(self):
        # CRITICAL: Extreme/Unusual Input (large numbers), Exact Output
        # Mean = (100.0 + 300.0) / 2 = 200.0
        # Abs diffs: |100.0-200.0|=100.0, |300.0-200.0|=100.0
        # MAD = (100.0 + 100.0) / 2 = 100.0
        self.assertEqual(mean_absolute_deviation([100.0, 300.0]), 100.0)

    def test_zero_values_list(self):
        # CRITICAL: Sign/Zero Testing (all zeros), Edge Case, Exact Output
        # Mean = (0.0 + 0.0 + 0.0 + 0.0) / 4 = 0.0
        # Abs diffs: |0.0-0.0|=0.0 for all elements
        # MAD = 0.0 / 4 = 0.0
        self.assertEqual(mean_absolute_deviation([0.0, 0.0, 0.0, 0.0]), 0.0)

    def test_longer_list_with_decimals(self):
        # CRITICAL: Typical/Expected Input (longer list), Exact Output, Float precision
        # Mean = (0.0 + 1.0 + 2.0 + 3.0 + 4.0) / 5 = 10.0 / 5 = 2.0
        # Abs diffs: |0.0-2.0|=2.0, |1.0-2.0|=1.0, |2.0-2.0|=0.0, |3.0-2.0|=1.0, |4.0-2.0|=2.0
        # MAD = (2.0 + 1.0 + 0.0 + 1.0 + 2.0) / 5 = 6.0 / 5 = 1.2
        self.assertEqual(mean_absolute_deviation([0.0, 1.0, 2.0, 3.0, 4.0]), 1.2)