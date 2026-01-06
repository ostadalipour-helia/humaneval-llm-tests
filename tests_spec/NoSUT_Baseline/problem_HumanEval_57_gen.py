import unittest
import sut.problem_HumanEval_57 as mod

class TestHybrid(unittest.TestCase):
    def test_edge_empty_list(self):
            """Test with an empty list, which should be considered monotonic."""
            self.assertEqual(mod.monotonic([]), True)

    def test_edge_single_element(self):
            """Test with a single-element list, which should be considered monotonic."""
            self.assertEqual(mod.monotonic([5]), True)

    def test_typical_strictly_increasing(self):
            """Test a typical strictly increasing list, as per docstring example."""
            self.assertEqual(mod.monotonic([1, 2, 4, 20]), True)

    def test_typical_strictly_decreasing(self):
            """Test a typical strictly decreasing list, including zero and negative numbers."""
            self.assertEqual(mod.monotonic([4, 1, 0, -10]), True)

    def test_non_monotonic_mixed_trends(self):
            """Test a list that is not monotonic due to mixed increasing/decreasing trends."""
            self.assertEqual(mod.monotonic([1, 20, 4, 10]), False)

    def test_boundary_constant_values(self):
            """Test a list with all identical values, which is both increasing and decreasing."""
            self.assertEqual(mod.monotonic([7, 7, 7, 7]), True)

    def test_boundary_increasing_with_duplicates(self):
            """Test an increasing list that includes duplicate adjacent values."""
            self.assertEqual(mod.monotonic([1, 2, 2, 3]), True)

    def test_boundary_decreasing_with_duplicates(self):
            """Test a decreasing list that includes duplicate adjacent values."""
            self.assertEqual(mod.monotonic([3, 2, 2, 1]), True)

    def test_extreme_negative_decreasing(self):
            """Test an extreme case with only negative numbers in decreasing order."""
            self.assertEqual(mod.monotonic([-1, -5, -10, -100]), True)

    def test_non_monotonic_mixed_signs_peak(self):
            """Test a non-monotonic list with mixed positive, negative, and zero values, forming a peak."""
            self.assertEqual(mod.monotonic([-5, 0, 5, -1]), False)
    
    if __name__ == '__main__':
        unittest.main()

    def test_normal_increasing(self):
            # Monotonically increasing list.
            self.assertTrue(mod.monotonic([1, 2, 4, 20]))

    def test_normal_decreasing(self):
            # Monotonically decreasing list.
            self.assertTrue(mod.monotonic([4, 1, 0, -10]))

    def test_normal_constant(self):
            # List with all identical elements (considered both increasing and decreasing).
            self.assertTrue(mod.monotonic([5, 5, 5, 5]))

    def test_edge_single_element_list(self):
            # Single-element list (vacuously monotonic).
            self.assertTrue(mod.monotonic([7]))

    def test_edge_two_element_increasing(self):
            # Two-element increasing list.
            self.assertTrue(mod.monotonic([1, 2]))

    def test_edge_two_element_decreasing(self):
            # Two-element decreasing list.
            self.assertTrue(mod.monotonic([2, 1]))

    def test_edge_two_element_constant(self):
            # Two-element constant list.
            self.assertTrue(mod.monotonic([1, 1]))

    def test_error_none_input(self):
            # Input is not a list.
            with self.assertRaises(TypeError):
                mod.monotonic(None)

    def test_error_integer_input(self):
            # Input is an integer, not a list.
            with self.assertRaises(TypeError):
                mod.monotonic(123)

    def test_error_non_comparable_elements(self):
            # List contains non-comparable elements (e.g., int and str).
            with self.assertRaises(TypeError):
                mod.monotonic([1, 'a', 3])

