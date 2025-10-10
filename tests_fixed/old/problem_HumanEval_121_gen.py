import unittest
from sut_llm.problem_HumanEval_121 import solution

class TestSolution(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(solution([5, 8, 7, 1]), 12)

    def test_example_2(self):
        self.assertEqual(solution([3, 3, 3, 3, 3]), 9)

    def test_example_3(self):
        self.assertEqual(solution([30, 13, 24, 321]), 0)

    def test_single_element_odd_at_even_position(self):
        self.assertEqual(solution([1]), 1)

    def test_single_element_even_at_even_position(self):
        self.assertEqual(solution([2]), 0)

    def test_all_even_numbers_mixed_positions(self):
        self.assertEqual(solution([10, 20, 30, 40, 50]), 0)

    def test_mixed_long_list_positive_integers(self):
        self.assertEqual(solution([1, 2, 3, 4, 5, 6, 7, 8, 9]), 25)

    def test_negative_odd_numbers_at_even_positions(self):
        self.assertEqual(solution([-1, -2, -3, -4, -5]), -9)

    def test_list_with_zeros_and_odds(self):
        self.assertEqual(solution([0, 1, 0, 3, 0, 5]), 0)

    def test_all_odd_numbers_some_at_even_positions(self):
        self.assertEqual(solution([11, 22, 33, 44, 55, 66, 77]), 176)