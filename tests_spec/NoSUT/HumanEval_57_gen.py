import unittest
from sut.problem_HumanEval_57 import monotonic

class Test_monotonic(unittest.TestCase):

    def test_normal_increasing(self):
        # Monotonically increasing list.
        self.assertTrue(monotonic([1, 2, 4, 20]))

    def test_normal_non_monotonic(self):
        # Non-monotonic list.
        self.assertFalse(monotonic([1, 20, 4, 10]))

    def test_normal_decreasing(self):
        # Monotonically decreasing list.
        self.assertTrue(monotonic([4, 1, 0, -10]))

    def test_normal_constant(self):
        # List with all identical elements (considered both increasing and decreasing).
        self.assertTrue(monotonic([5, 5, 5, 5]))

    def test_edge_empty_list(self):
        # Empty list (vacuously monotonic).
        self.assertTrue(monotonic([]))

    def test_edge_single_element_list(self):
        # Single-element list (vacuously monotonic).
        self.assertTrue(monotonic([7]))

    def test_edge_two_element_increasing(self):
        # Two-element increasing list.
        self.assertTrue(monotonic([1, 2]))

    def test_edge_two_element_decreasing(self):
        # Two-element decreasing list.
        self.assertTrue(monotonic([2, 1]))

    def test_edge_two_element_constant(self):
        # Two-element constant list.
        self.assertTrue(monotonic([1, 1]))

    def test_error_none_input(self):
        # Input is not a list.
        with self.assertRaises(TypeError):
            monotonic(None)

    def test_error_integer_input(self):
        # Input is an integer, not a list.
        with self.assertRaises(TypeError):
            monotonic(123)

    def test_error_string_input(self):
        # Input is a string, not a list.
        with self.assertRaises(TypeError):
            monotonic("hello")

    def test_error_non_comparable_elements(self):
        # List contains non-comparable elements (e.g., int and str).
        with self.assertRaises(TypeError):
            monotonic([1, 'a', 3])