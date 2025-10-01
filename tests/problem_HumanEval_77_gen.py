import unittest
from sut.problem_HumanEval_77 import iscube

class TestIsCube(unittest.TestCase):

    def test_positive_one_is_cube(self):
        self.assertTrue(iscube(1))

    def test_positive_two_is_not_cube(self):
        self.assertFalse(iscube(2))

    def test_negative_one_is_cube(self):
        self.assertTrue(iscube(-1))

    def test_positive_sixty_four_is_cube(self):
        self.assertTrue(iscube(64))

    def test_zero_is_cube(self):
        self.assertTrue(iscube(0))

    def test_positive_one_eighty_is_not_cube(self):
        self.assertFalse(iscube(180))

    def test_positive_twenty_seven_is_cube(self):
        self.assertTrue(iscube(27))

    def test_negative_eight_is_cube(self):
        self.assertTrue(iscube(-8))

    def test_positive_nine_is_not_cube(self):
        self.assertFalse(iscube(9))

    def test_negative_twenty_six_is_not_cube(self):
        self.assertFalse(iscube(-26))

if __name__ == '__main__':
    unittest.main()