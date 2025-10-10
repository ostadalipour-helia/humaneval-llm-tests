import unittest
from sut_llm.problem_HumanEval_142 import sum_squares

class TestSumSquares(unittest.TestCase):

    def test_example_1(self):
        lst = [1, 2, 3]
        self.assertEqual(sum_squares(lst), 6)

    def test_example_2_empty_list(self):
        lst = []
        self.assertEqual(sum_squares(lst), 0)

    def test_example_3_negative_numbers(self):
        lst = [-1, -5, 2, -1, -5]
        self.assertEqual(sum_squares(lst), -126)

    def test_single_element_list(self):
        lst = [5]
        self.assertEqual(sum_squares(lst), 25)

    def test_mixed_indices_short_list(self):
        lst = [1, 2, 3, 4, 5]
        # idx 0 (mult of 3): 1^2 = 1
        # idx 1 (no change): 2
        # idx 2 (no change): 3
        # idx 3 (mult of 3): 4^2 = 16
        # idx 4 (mult of 4, not 3): 5^3 = 125
        # Sum: 1 + 2 + 3 + 16 + 125 = 147
        self.assertEqual(sum_squares(lst), 147)

    def test_longer_list_with_all_rules(self):
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # idx 0 (mult of 3): 1^2 = 1
        # idx 1 (no change): 2
        # idx 2 (no change): 3
        # idx 3 (mult of 3): 4^2 = 16
        # idx 4 (mult of 4, not 3): 5^3 = 125
        # idx 5 (no change): 6
        # idx 6 (mult of 3): 7^2 = 49
        # idx 7 (no change): 8
        # idx 8 (mult of 4, not 3): 9^3 = 729
        # Sum: 1 + 2 + 3 + 16 + 125 + 6 + 49 + 8 + 729 = 939
        self.assertEqual(sum_squares(lst), 939)

    def test_list_with_zeros(self):
        lst = [0, 0, 0, 0, 0]
        self.assertEqual(sum_squares(lst), 0)

    def test_list_with_large_numbers(self):
        lst = [10, 20, 30, 40, 50]
        # idx 0 (mult of 3): 10^2 = 100
        # idx 1 (no change): 20
        # idx 2 (no change): 30
        # idx 3 (mult of 3): 40^2 = 1600
        # idx 4 (mult of 4, not 3): 50^3 = 125000
        # Sum: 100 + 20 + 30 + 1600 + 125000 = 126750
        self.assertEqual(sum_squares(lst), 126750)

    def test_list_with_only_no_change_indices(self):
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        # Recalculating based on the actual list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] (indices 0-10)
        # idx 0 (0 % 3 == 0): 1^2 = 1
        # idx 1 (no change): 2
        # idx 2 (no change): 3
        # idx 3 (3 % 3 == 0): 4^2 = 16
        # idx 4 (4 % 4 == 0, not % 3): 5^3 = 125
        # idx 5 (no change): 6
        # idx 6 (6 % 3 == 0): 7^2 = 49
        # idx 7 (no change): 8
        # idx 8 (8 % 4 == 0, not % 3): 9^3 = 729
        # idx 9 (9 % 3 == 0): 10^2 = 100
        # idx 10 (no change): 11
        # Sum: 1 + 2 + 3 + 16 + 125 + 6 + 49 + 8 + 729 + 100 + 11 = 1050
        self.assertEqual(sum_squares(lst), 1050)

    def test_mixed_positive_negative_long_list(self):
        lst = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13]
        # idx 0 (mult of 3): 1^2 = 1
        # idx 1 (no change): -2
        # idx 2 (no change): 3
        # idx 3 (mult of 3): (-4)^2 = 16
        # idx 4 (mult of 4, not 3): 5^3 = 125
        # idx 5 (no change): -6
        # idx 6 (mult of 3): 7^2 = 49
        # idx 7 (no change): -8
        # idx 8 (mult of 4, not 3): 9^3 = 729
        # idx 9 (mult of 3): (-10)^2 = 100
        # idx 10 (no change): 11
        # idx 11 (no change): -12
        # idx 12 (mult of 3): 13^2 = 169
        # Sum: 1 - 2 + 3 + 16 + 125 - 6 + 49 - 8 + 729 + 100 + 11 - 12 + 169 = 1175
        self.assertEqual(sum_squares(lst), 1175)

if __name__ == '__main__':
    unittest.main()