import unittest
from sut_llm.problem_HumanEval_109 import move_one_ball

class TestMoveOneBall(unittest.TestCase):

    def test_empty_array(self):
        self.assertTrue(move_one_ball([]))

    def test_already_sorted_array(self):
        self.assertTrue(move_one_ball([1, 2, 3, 4, 5]))

    def test_one_right_shift_needed(self):
        self.assertTrue(move_one_ball([5, 1, 2, 3, 4]))

    def test_multiple_right_shifts_needed_example(self):
        self.assertTrue(move_one_ball([3, 4, 5, 1, 2]))

    def test_cannot_be_sorted_example(self):
        self.assertFalse(move_one_ball([3, 5, 4, 1, 2]))

    def test_two_elements_sorted(self):
        self.assertTrue(move_one_ball([1, 2]))

    def test_two_elements_one_shift(self):
        self.assertTrue(move_one_ball([2, 1]))

    def test_three_elements_cannot_sort(self):
        self.assertFalse(move_one_ball([1, 3, 2]))

    def test_longer_array_multiple_shifts(self):
        self.assertTrue(move_one_ball([6, 7, 8, 9, 1, 2, 3, 4, 5]))

    def test_longer_array_cannot_sort(self):
        self.assertFalse(move_one_ball([1, 2, 4, 3, 5]))

if __name__ == '__main__':
    unittest.main()