import unittest
import sut.problem_HumanEval_127 as mod

class TestHybrid(unittest.TestCase):
    def test_sample_one_touching_intervals(self):
            # Intersection: (2,2), Length: 1. 1 is not prime.
            self.assertEqual(mod.intersection((1, 2), (2, 3)), "NO")

    def test_sample_two_crossing_zero(self):
            # Intersection: (0,1), Length: 2. Based on sample, 2 is not considered prime.
            self.assertEqual(mod.intersection((-1, 1), (0, 4)), "NO")

    def test_sample_three_negative_prime_length(self):
            # Intersection: (-3,-1), Length: 3. 3 is prime.
            self.assertEqual(mod.intersection((-3, -1), (-5, 5)), "YES")

    def test_no_intersection_disjoint(self):
            # Intervals are disjoint.
            self.assertEqual(mod.intersection((1, 2), (3, 4)), "NO")

    def test_single_point_intersection_non_prime(self):
            # Single point intervals, intersection is a single point. Length: 1. 1 is not prime.
            self.assertEqual(mod.intersection((5, 5), (5, 5)), "NO")

    def test_large_numbers_prime_length(self):
            # Large numbers, intersection: (103,105), Length: 3. 3 is prime.
            self.assertEqual(mod.intersection((100, 105), (103, 109)), "YES")

    def test_negative_disjoint_intervals(self):
            # Negative intervals, disjoint.
            self.assertEqual(mod.intersection((-10, -5), (-4, 0)), "NO")

    def test_normal_negative_intervals_prime_length(self):
            # Intersection is (-3, -1), length is 3. 3 is a prime number.
            interval1 = [-3, -1]
            interval2 = [-5, 5]
            self.assertEqual(mod.intersection(interval1, interval2), "YES")

    def test_edge_touching_intervals(self):
            # Intersection is (2, 2), length is 1. 1 is not a prime number.
            interval1 = [1, 2]
            interval2 = [2, 3]
            self.assertEqual(mod.intersection(interval1, interval2), "NO")

    def test_edge_disjoint_intervals(self):
            # Intervals do not intersect. Length of intersection is 0. 0 is not a prime number.
            interval1 = [1, 2]
            interval2 = [3, 4]
            self.assertEqual(mod.intersection(interval1, interval2), "NO")

    def test_error_non_integer_element(self):
            # Non-integer element in interval1.
            with self.assertRaises(TypeError):
                mod.intersection([1, "a"], [2, 3])

    def test_error_invalid_interval_type(self):
            # Invalid type for interval1 (not a tuple or list).
            with self.assertRaises(TypeError):
                mod.intersection(None, [2, 3])

