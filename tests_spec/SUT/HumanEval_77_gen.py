import unittest
from sut.problem_HumanEval_77 import iscube

class Test_iscube(unittest.TestCase):

    def test_positive_perfect_cube(self):
        self.assertEqual(iscube(64), True)

    def test_negative_one_is_cube(self):
        self.assertEqual(iscube(-1), True)

    def test_positive_not_cube(self):
        self.assertEqual(iscube(2), False)

    def test_larger_positive_not_cube(self):
        self.assertEqual(iscube(180), False)

    def test_zero_is_cube(self):
        self.assertEqual(iscube(0), True)

    def test_one_is_cube(self):
        self.assertEqual(iscube(1), True)

    def test_negative_perfect_cube(self):
        self.assertEqual(iscube(-8), True)

    def test_below_perfect_cube(self):
        self.assertEqual(iscube(7), False)

    def test_above_perfect_cube(self):
        self.assertEqual(iscube(9), False)

    def test_negative_above_negative_cube(self):
        self.assertEqual(iscube(-7), False)