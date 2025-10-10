import unittest
from sut_llm.problem_HumanEval_0 import has_close_elements

class TestHasCloseElements(unittest.TestCase):

    def test_docstring_example_false(self):
        # Test case from docstring where no two elements are closer than the threshold.
        numbers = [1.0, 2.0, 3.0]
        threshold = 0.5
        self.assertFalse(has_close_elements(numbers, threshold))

    def test_docstring_example_true(self):
        # Test case from docstring where two elements are closer than the threshold.
        numbers = [1.0, 2.8, 3.0, 4.0, 5.0, 2.0]
        threshold = 0.3
        self.assertTrue(has_close_elements(numbers, threshold))

    def test_empty_list(self):
        # Test with an empty list, should always be False as no pairs exist.
        numbers = []
        threshold = 1.0
        self.assertFalse(has_close_elements(numbers, threshold))

    def test_single_element_list(self):
        # Test with a list containing only one element, should always be False.
        numbers = [5.0]
        threshold = 0.1
        self.assertFalse(has_close_elements(numbers, threshold))

    def test_two_elements_clearly_close(self):
        # Test with two elements that are clearly closer than the threshold.
        numbers = [10.0, 10.05]
        threshold = 0.1
        self.assertTrue(has_close_elements(numbers, threshold))

    def test_two_elements_exactly_at_threshold(self):
        # Test with two elements whose difference is exactly equal to the threshold.
        # The condition is 'less than' threshold, so this should be False.
        numbers = [2.0, 2.5]
        threshold = 0.5
        self.assertFalse(has_close_elements(numbers, threshold))

    def test_two_elements_not_close(self):
        # Test with two elements that are clearly not closer than the threshold.
        numbers = [1.0, 5.0]
        threshold = 1.0
        self.assertFalse(has_close_elements(numbers, threshold))

    def test_multiple_elements_close_pair_in_middle(self):
        # Test with multiple elements where a close pair exists in the middle of the list.
        numbers = [1.0, 2.0, 2.001, 3.0, 4.0]
        threshold = 0.01
        self.assertTrue(has_close_elements(numbers, threshold))

    def test_multiple_elements_all_far_apart(self):
        # Test with multiple elements where all pairs are far apart.
        numbers = [100.0, 200.0, 300.0]
        threshold = 50.0
        self.assertFalse(has_close_elements(numbers, threshold))

    def test_threshold_is_zero(self):
        # Test with a threshold of zero. Only identical numbers would satisfy abs(diff) < 0,
        # which is impossible. So, it should be False unless numbers are identical and the
        # condition was <=. With <, it should always be False.
        numbers = [1.0, 1.0000000000000001] # A very small difference
        threshold = 0.0
        self.assertFalse(has_close_elements(numbers, threshold))
