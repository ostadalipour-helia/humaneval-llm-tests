import unittest
from sut.problem_HumanEval_127 import intersection

class TestIntersection(unittest.TestCase):

    def test_sample_one_touching_intervals(self):
        # Intersection: (2,2), Length: 1. 1 is not prime.
        self.assertEqual(intersection((1, 2), (2, 3)), "NO")

    def test_sample_two_crossing_zero(self):
        # Intersection: (0,1), Length: 2. Based on sample, 2 is not considered prime.
        self.assertEqual(intersection((-1, 1), (0, 4)), "NO")

    def test_sample_three_negative_prime_length(self):
        # Intersection: (-3,-1), Length: 3. 3 is prime.
        self.assertEqual(intersection((-3, -1), (-5, 5)), "YES")

    def test_no_intersection_disjoint(self):
        # Intervals are disjoint.
        self.assertEqual(intersection((1, 2), (3, 4)), "NO")

    def test_full_overlap_prime_length(self):
        # Intervals are identical. Intersection: (1,5), Length: 5. 5 is prime.
        self.assertEqual(intersection((1, 5), (1, 5)), "YES")

    def test_one_contained_non_prime_length(self):
        # One interval fully contained. Intersection: (3,6), Length: 4. 4 is not prime.
        self.assertEqual(intersection((1, 10), (3, 6)), "NO")

    def test_single_point_intersection_non_prime(self):
        # Single point intervals, intersection is a single point. Length: 1. 1 is not prime.
        self.assertEqual(intersection((5, 5), (5, 5)), "NO")

    def test_large_numbers_prime_length(self):
        # Large numbers, intersection: (103,105), Length: 3. 3 is prime.
        self.assertEqual(intersection((100, 105), (103, 109)), "YES")

    def test_negative_disjoint_intervals(self):
        # Negative intervals, disjoint.
        self.assertEqual(intersection((-10, -5), (-4, 0)), "NO")

    def test_overlapping_non_prime_length(self):
        # Overlapping intervals, intersection: (3,6), Length: 4. 4 is not prime.
        self.assertEqual(intersection((0, 6), (3, 8)), "NO")