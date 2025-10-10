import unittest
from sut.problem_HumanEval_130 import tri

class TestTri(unittest.TestCase):

    def test_01_n_is_zero(self):
        # Based on tri(3) example, tri(0) is inferred to be 1.
        self.assertEqual(tri(0), [1])

    def test_02_n_is_one(self):
        # tri(0) = 1
        # tri(1) = 3 (explicit rule)
        self.assertEqual(tri(1), [1, 3])

    def test_03_n_is_two(self):
        # tri(0) = 1
        # tri(1) = 3
        # tri(2) = 1 + (2 / 2) = 2 (even rule)
        self.assertEqual(tri(2), [1, 3, 2])

    def test_04_n_is_three(self):
        # This is the example provided in the docstring.
        # tri(0) = 1
        # tri(1) = 3
        # tri(2) = 2
        # tri(4) = 1 + (4 / 2) = 3
        # tri(3) = tri(2) + tri(1) + tri(4) = 2 + 3 + 3 = 8 (odd rule)
        self.assertEqual(tri(3), [1, 3, 2, 8])

    def test_05_n_is_four(self):
        # tri(0) = 1
        # tri(1) = 3
        # tri(2) = 2
        # tri(3) = 8
        # tri(4) = 1 + (4 / 2) = 3 (even rule)
        self.assertEqual(tri(4), [1, 3, 2, 8, 3])

    def test_06_n_is_five(self):
        # tri(0) = 1
        # tri(1) = 3
        # tri(2) = 2
        # tri(3) = 8
        # tri(4) = 3
        # tri(6) = 1 + (6 / 2) = 4
        # tri(5) = tri(4) + tri(3) + tri(6) = 3 + 8 + 4 = 15 (odd rule)
        self.assertEqual(tri(5), [1, 3, 2, 8, 3, 15])

    def test_07_n_is_six(self):
        # tri(0) = 1
        # tri(1) = 3
        # tri(2) = 2
        # tri(3) = 8
        # tri(4) = 3
        # tri(5) = 15
        # tri(6) = 1 + (6 / 2) = 4 (even rule)
        self.assertEqual(tri(6), [1, 3, 2, 8, 3, 15, 4])

    def test_08_n_is_seven(self):
        # tri(0) = 1
        # tri(1) = 3
        # tri(2) = 2
        # tri(3) = 8
        # tri(4) = 3
        # tri(5) = 15
        # tri(6) = 4
        # tri(8) = 1 + (8 / 2) = 5
        # tri(7) = tri(6) + tri(5) + tri(8) = 4 + 15 + 5 = 24 (odd rule)
        self.assertEqual(tri(7), [1, 3, 2, 8, 3, 15, 4, 24])

    def test_09_n_is_eight(self):
        # tri(0) = 1
        # tri(1) = 3
        # tri(2) = 2
        # tri(3) = 8
        # tri(4) = 3
        # tri(5) = 15
        # tri(6) = 4
        # tri(7) = 24
        # tri(8) = 1 + (8 / 2) = 5 (even rule)
        self.assertEqual(tri(8), [1, 3, 2, 8, 3, 15, 4, 24, 5])

    def test_10_n_is_nine(self):
        # tri(0) = 1
        # tri(1) = 3
        # tri(2) = 2
        # tri(3) = 8
        # tri(4) = 3
        # tri(5) = 15
        # tri(6) = 4
        # tri(7) = 24
        # tri(8) = 5
        # tri(10) = 1 + (10 / 2) = 6
        # tri(9) = tri(8) + tri(7) + tri(10) = 5 + 24 + 6 = 35 (odd rule)
        self.assertEqual(tri(9), [1, 3, 2, 8, 3, 15, 4, 24, 5, 35])