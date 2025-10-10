import unittest
from sut.problem_HumanEval_57 import monotonic

class TestMonotonic(unittest.TestCase):

    def test_edge_empty_list(self):
        """Test with an empty list, which should be considered monotonic."""
        self.assertEqual(monotonic([]), True)

    def test_edge_single_element(self):
        """Test with a single-element list, which should be considered monotonic."""
        self.assertEqual(monotonic([5]), True)

    def test_typical_strictly_increasing(self):
        """Test a typical strictly increasing list, as per docstring example."""
        self.assertEqual(monotonic([1, 2, 4, 20]), True)

    def test_typical_strictly_decreasing(self):
        """Test a typical strictly decreasing list, including zero and negative numbers."""
        self.assertEqual(monotonic([4, 1, 0, -10]), True)

    def test_non_monotonic_mixed_trends(self):
        """Test a list that is not monotonic due to mixed increasing/decreasing trends."""
        self.assertEqual(monotonic([1, 20, 4, 10]), False)

    def test_boundary_constant_values(self):
        """Test a list with all identical values, which is both increasing and decreasing."""
        self.assertEqual(monotonic([7, 7, 7, 7]), True)

    def test_boundary_increasing_with_duplicates(self):
        """Test an increasing list that includes duplicate adjacent values."""
        self.assertEqual(monotonic([1, 2, 2, 3]), True)

    def test_boundary_decreasing_with_duplicates(self):
        """Test a decreasing list that includes duplicate adjacent values."""
        self.assertEqual(monotonic([3, 2, 2, 1]), True)

    def test_extreme_negative_decreasing(self):
        """Test an extreme case with only negative numbers in decreasing order."""
        self.assertEqual(monotonic([-1, -5, -10, -100]), True)

    def test_non_monotonic_mixed_signs_peak(self):
        """Test a non-monotonic list with mixed positive, negative, and zero values, forming a peak."""
        self.assertEqual(monotonic([-5, 0, 5, -1]), False)

if __name__ == '__main__':
    unittest.main()