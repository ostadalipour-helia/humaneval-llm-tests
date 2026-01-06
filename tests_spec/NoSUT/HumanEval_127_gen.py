import unittest
from sut.problem_HumanEval_127 import intersection

class Test_intersection(unittest.TestCase):

    def test_normal_overlapping_prime_length(self):
        # Intersection is (2, 3), length is 2. 2 is a prime number.
        interval1 = [1, 3]
        interval2 = [2, 4]
        self.assertEqual(intersection(interval1, interval2), "YES")

    def test_normal_overlapping_composite_length(self):
        # Intersection is (5, 10), length is 6. 6 is not a prime number.
        interval1 = [1, 10]
        interval2 = [5, 15]
        self.assertEqual(intersection(interval1, interval2), "NO")

    def test_normal_negative_intervals_prime_length(self):
        # Intersection is (-3, -1), length is 3. 3 is a prime number.
        interval1 = [-3, -1]
        interval2 = [-5, 5]
        self.assertEqual(intersection(interval1, interval2), "YES")

    def test_edge_touching_intervals(self):
        # Intersection is (2, 2), length is 1. 1 is not a prime number.
        interval1 = [1, 2]
        interval2 = [2, 3]
        self.assertEqual(intersection(interval1, interval2), "NO")

    def test_edge_disjoint_intervals(self):
        # Intervals do not intersect. Length of intersection is 0. 0 is not a prime number.
        interval1 = [1, 2]
        interval2 = [3, 4]
        self.assertEqual(intersection(interval1, interval2), "NO")

    def test_edge_identical_intervals(self):
        # Intervals are identical. Intersection is (1, 5), length is 5. 5 is a prime number.
        interval1 = [1, 5]
        interval2 = [1, 5]
        self.assertEqual(intersection(interval1, interval2), "YES")

    def test_edge_one_contains_another(self):
        # One interval fully contains another. Intersection is (-5, 5), length is 11. 11 is a prime number.
        interval1 = [-10, 10]
        interval2 = [-5, 5]
        self.assertEqual(intersection(interval1, interval2), "YES")

    def test_error_interval1_start_gt_end(self):
        # The first interval violates the assumption that its start is less than or equal to its end.
        with self.assertRaises(ValueError):
            intersection([5, 1], [2, 3])

    def test_error_non_integer_element(self):
        # Non-integer element in interval1.
        with self.assertRaises(TypeError):
            intersection([1, "a"], [2, 3])

    def test_error_invalid_interval_type(self):
        # Invalid type for interval1 (not a tuple or list).
        with self.assertRaises(TypeError):
            intersection(None, [2, 3])

    def test_error_interval_incorrect_length(self):
        # Interval1 is not a pair of integers (length 3 instead of 2).
        with self.assertRaises(ValueError):
            intersection([1, 2, 3], [2, 3])