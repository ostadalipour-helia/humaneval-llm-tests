import unittest
from sut.problem_HumanEval_77 import iscube

class Test_iscube(unittest.TestCase):
    def test_normal_positive_cube(self):
        # Normal case: Positive integer that is a perfect cube (4*4*4).
        self.assertTrue(iscube(64))

    def test_normal_negative_cube(self):
        # Normal case: Negative integer that is a perfect cube (-1*-1*-1).
        self.assertTrue(iscube(-1))

    def test_normal_positive_not_cube_small(self):
        # Normal case: Positive integer that is not a perfect cube.
        self.assertFalse(iscube(2))

    def test_normal_positive_not_cube_large(self):
        # Normal case: Larger positive integer that is not a perfect cube.
        self.assertFalse(iscube(180))

    def test_edge_zero_cube(self):
        # Edge case: Zero is a perfect cube (0*0*0).
        self.assertTrue(iscube(0))

    def test_edge_one_cube(self):
        # Edge case: One is a perfect cube (1*1*1).
        self.assertTrue(iscube(1))

    def test_edge_another_negative_cube(self):
        # Edge case: Another negative perfect cube (-2*-2*-2).
        self.assertTrue(iscube(-8))

    def test_edge_positive_just_below_cube(self):
        # Edge case: Positive integer just below a perfect cube (8).
        self.assertFalse(iscube(7))

    def test_edge_positive_just_above_cube(self):
        # Edge case: Positive integer just above a perfect cube (8).
        self.assertFalse(iscube(9))

    def test_edge_negative_just_above_negative_cube(self):
        # Edge case: Negative integer just above a negative perfect cube (-8).
        self.assertFalse(iscube(-7))

    def test_edge_negative_just_below_negative_cube(self):
        # Edge case: Negative integer just below a negative perfect cube (-8).
        self.assertFalse(iscube(-9))