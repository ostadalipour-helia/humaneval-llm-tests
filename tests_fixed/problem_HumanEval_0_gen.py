import unittest
from sut_llm.problem_HumanEval_0 import has_close_elements

class TestHasCloseElements(unittest.TestCase):

    def test_docstring_example_1(self):
        # Typical input, no close elements
        numbers = [1.0, 2.0, 3.0]
        threshold = 0.5
        self.assertEqual(has_close_elements(numbers, threshold), False)

    def test_docstring_example_2(self):
        # Typical input, with close elements
        numbers = [1.0, 2.8, 3.0, 4.0, 5.0, 2.0]
        threshold = 0.3
        self.assertEqual(has_close_elements(numbers, threshold), True)

    def test_boundary_exact_threshold_false(self):
        # Test when difference is exactly equal to threshold (should be False due to '<')
        numbers = [1.0, 2.0]
        threshold = 1.0
        self.assertEqual(has_close_elements(numbers, threshold), False)

    def test_boundary_just_below_threshold_true(self):
        # Test when difference is just below threshold (should be True)
        numbers = [1.0, 1.999]
        threshold = 1.0
        self.assertEqual(has_close_elements(numbers, threshold), True)

    def test_edge_empty_list(self):
        # Edge case: empty list of numbers
        numbers = []
        threshold = 0.1
        self.assertEqual(has_close_elements(numbers, threshold), False)

    def test_edge_single_element_list(self):
        # Edge case: list with a single number
        numbers = [5.0]
        threshold = 0.1
        self.assertEqual(has_close_elements(numbers, threshold), False)

    def test_edge_two_elements_not_close(self):
        # Edge case: list with two elements, but not close enough
        numbers = [1.0, 5.0]
        threshold = 1.0
        self.assertEqual(has_close_elements(numbers, threshold), False)

    def test_extreme_large_numbers_close(self):
        # Extreme input: very large numbers that are close
        numbers = [1000000.0, 1000000.0001]
        threshold = 0.001
        self.assertEqual(has_close_elements(numbers, threshold), True)

    def test_extreme_negative_numbers_close(self):
        # Extreme input: negative numbers that are close
        numbers = [-5.0, -4.95]
        threshold = 0.1
        self.assertEqual(has_close_elements(numbers, threshold), True)

    def test_logic_multiple_close_pairs_mixed_signs(self):
        # Logic mutation: multiple pairs satisfy the condition, including zero and mixed signs
        numbers = [-1.0, 0.0, 0.05, 1.0, 1.02]
        threshold = 0.1
        # abs(0.0 - 0.05) = 0.05 < 0.1
        # abs(1.0 - 1.02) = 0.02 < 0.1
        self.assertEqual(has_close_elements(numbers, threshold), True)

if __name__ == '__main__':
    unittest.main()