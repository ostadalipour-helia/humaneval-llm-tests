import unittest
import sut.problem_HumanEval_135 as mod

class TestHybrid(unittest.TestCase):
    def test_example_one_from_docstring(self):
            # Test a typical case with a decreasing pair, verifying the exact output.
            # Covers: Typical input, specific output verification.
            self.assertEqual(mod.can_arrange([1, 2, 4, 3, 5]), 3)

    def test_example_two_from_docstring_sorted_array(self):
            # Test a fully sorted array where no decreasing pair exists.
            # Covers: Return -1 path, typical input (sorted).
            self.assertEqual(mod.can_arrange([1, 2, 3]), -1)

    def test_empty_array_edge_case(self):
            # Test with an empty array.
            # Covers: Edge case (empty collection), off-by-one (no i-1), return -1.
            self.assertEqual(mod.can_arrange([]), -1)

    def test_single_element_array_edge_case(self):
            # Test with a single-element array.
            # Covers: Edge case (single element collection), off-by-one (no i-1), return -1.
            self.assertEqual(mod.can_arrange([5]), -1)

    def test_two_elements_decreasing_boundary(self):
            # Test the smallest array with a decreasing pair.
            # Covers: Boundary condition (first possible index), off-by-one.
            self.assertEqual(mod.can_arrange([2, 1]), 1)

    def test_two_elements_increasing_boundary(self):
            # Test the smallest array without a decreasing pair.
            # Covers: Boundary condition (no decreasing pair), off-by-one.
            self.assertEqual(mod.can_arrange([1, 2]), -1)

    def test_multiple_decreasing_pairs_largest_at_end(self):
            # Test an array with multiple decreasing pairs, ensuring the largest index is returned.
            # Covers: Logic mutation (ensuring 'largest' index), return value testing.
            self.assertEqual(mod.can_arrange([1, 5, 2, 6, 3]), 4) # 5>2 at index 2, 6>3 at index 4

    def test_multiple_decreasing_pairs_largest_in_middle(self):
            # Test an array with multiple decreasing pairs, where the largest index is not the last element.
            # Covers: Logic mutation (ensuring 'largest' index), return value testing.
            self.assertEqual(mod.can_arrange([1, 5, 2, 3, 0, 4]), 4) # 5>2 at index 2, 3>0 at index 4

    def test_array_with_negative_numbers_and_zero(self):
            # Test with negative numbers and zero to cover sign and zero testing.
            # Covers: Sign and zero testing, extreme/unusual inputs.
            self.assertEqual(mod.can_arrange([-5, -2, 0, -1, 3]), 3) # 0 > -1 at index 3

    def test_large_numbers_single_drop_at_beginning(self):
            # Test with large numbers and a decreasing pair at the very beginning.
            # Covers: Extreme/unusual inputs, boundary condition (first possible index).
            self.assertEqual(mod.can_arrange([1000, 500, 2000, 3000, 4000]), 1) # 1000 > 500 at index 1

    def test_normal_single_disorder(self):
            # A typical case with a single 'disorder' at index 3 (4 > 3).
            arr = [1, 2, 4, 3, 5]
            self.assertEqual(mod.can_arrange(arr), 3)

    def test_normal_multiple_disorders(self):
            # Multiple 'disorders', returning the largest index (6 > 3 at index 4).
            arr = [1, 5, 2, 6, 3]
            self.assertEqual(mod.can_arrange(arr), 4)

    def test_normal_reverse_sorted(self):
            # A fully reverse-sorted array, returning the last possible index.
            arr = [5, 4, 3, 2, 1]
            self.assertEqual(mod.can_arrange(arr), 4)

    def test_edge_already_sorted(self):
            # An already sorted array, no disorder.
            arr = [1, 2, 3]
            self.assertEqual(mod.can_arrange(arr), -1)

    def test_edge_empty_array(self):
            # An empty array, no elements to compare.
            arr = []
            self.assertEqual(mod.can_arrange(arr), -1)

    def test_edge_single_element_array(self):
            # A single-element array, no preceding element for comparison.
            arr = [5]
            self.assertEqual(mod.can_arrange(arr), -1)

    def test_edge_smallest_disorder(self):
            # The smallest possible array with a disorder.
            arr = [3, 2]
            self.assertEqual(mod.can_arrange(arr), 1)

    def test_edge_disorder_then_sorted(self):
            # Disorder at index 1, then sorted again.
            arr = [2, 1, 3]
            self.assertEqual(mod.can_arrange(arr), 1)

    def test_error_non_list_input_none(self):
            # Input 'arr' is not a list (None).
            with self.assertRaises(TypeError):
                mod.can_arrange(None)

    def test_error_non_comparable_elements(self):
            # Elements of 'arr' are not comparable (mixed types).
            arr = [1, 'a', 3]
            with self.assertRaises(TypeError):
                mod.can_arrange(arr)

