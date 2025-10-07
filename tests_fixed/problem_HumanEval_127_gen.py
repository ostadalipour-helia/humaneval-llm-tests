import unittest
from sut_llm.problem_HumanEval_127 import intersection

class TestIntersection(unittest.TestCase):

    def test_no_overlap(self):
        # Intervals (1, 2) and (3, 4) do not overlap.
        # Intersection length is 0, which is not prime.
        self.assertEqual(intersection((1, 2), (3, 4)), "NO")

    def test_touching_intervals_length_zero(self):
        # Intervals (1, 2) and (2, 3) touch at point 2.
        # Intersection is (2, 2), length 2 - 2 = 0. Not prime.
        # This matches a docstring example.
        self.assertEqual(intersection((1, 2), (2, 3)), "NO")

    def test_small_overlap_length_one(self):
        # Intervals (1, 3) and (2, 3) overlap to (2, 3).
        # Intersection length is 3 - 2 = 1. Not prime.
        # This matches the logic of another docstring example (-1,1), (0,4) -> (0,1) length 1.
        self.assertEqual(intersection((1, 3), (2, 3)), "NO")

    def test_overlap_length_two_prime(self):
        # Intervals (1, 4) and (2, 4) overlap to (2, 4).
        # Intersection length is 4 - 2 = 2. 2 is prime.
        # This matches the logic of another docstring example (-3,-1), (-5,5) -> (-3,-1) length 2.
        self.assertEqual(intersection((1, 4), (2, 4)), "YES")

    def test_overlap_length_three_prime(self):
        # Intervals (1, 5) and (2, 5) overlap to (2, 5).
        # Intersection length is 5 - 2 = 3. 3 is prime.
        self.assertEqual(intersection((1, 5), (2, 5)), "YES")

    def test_overlap_length_four_not_prime(self):
        # Intervals (1, 6) and (2, 6) overlap to (2, 6).
        # Intersection length is 6 - 2 = 4. 4 is not prime.
        self.assertEqual(intersection((1, 6), (2, 6)), "NO")

    def test_one_interval_contains_another_length_five_prime(self):
        # Interval (0, 10) contains (2, 7).
        # Intersection is (2, 7). Length 7 - 2 = 5. 5 is prime.
        self.assertEqual(intersection((0, 10), (2, 7)), "YES")

    def test_negative_numbers_overlap_length_two_prime(self):
        # Intervals (-5, -1) and (-3, 0) overlap to (-3, -1).
        # Intersection length is -1 - (-3) = 2. 2 is prime.
        self.assertEqual(intersection((-5, -1), (-3, 0)), "YES")

    def test_negative_numbers_overlap_length_one_not_prime(self):
        # Intervals (-5, -2) and (-3, -2) overlap to (-3, -2).
        # Intersection length is -2 - (-3) = 1. 1 is not prime.
        self.assertEqual(intersection((-5, -2), (-3, -2)), "NO")

    def test_identical_intervals_length_zero(self):
        # Intervals (5, 5) and (5, 5) are identical.
        # Intersection is (5, 5). Length 5 - 5 = 0. Not prime.
        self.assertEqual(intersection((5, 5), (5, 5)), "NO")