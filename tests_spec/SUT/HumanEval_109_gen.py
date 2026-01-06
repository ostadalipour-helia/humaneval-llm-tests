import unittest
from sut.problem_HumanEval_109 import move_one_ball

class Test_move_one_ball(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(move_one_ball([3, 4, 5, 1, 2]), False)

    def test_case_2(self):
        self.assertEqual(move_one_ball([3, 5, 4, 1, 2]), False)

    def test_case_3(self):
        self.assertEqual(move_one_ball([1, 2, 3, 4, 5]), False)

    def test_case_4(self):
        self.assertEqual(move_one_ball([2, 3, 4, 5, 1]), False)

    def test_case_5(self):
        self.assertEqual(move_one_ball([]), True)

    def test_case_6(self):
        self.assertEqual(move_one_ball([7]), False)

    def test_case_7(self):
        self.assertEqual(move_one_ball([2, 1]), False)

    def test_case_8(self):
        self.assertEqual(move_one_ball([1, 2]), False)

    def test_case_9(self):
        self.assertEqual(move_one_ball([3, 4, 5, 1, 2]), False)

    def test_case_10(self):
        self.assertEqual(move_one_ball([3, 5, 4, 1, 2]), False)