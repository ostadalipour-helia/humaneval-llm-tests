import unittest
from sut_llm.problem_HumanEval_110 import exchange

class TestExchange(unittest.TestCase):

    def test_1_example_one_typical_yes(self):
        # Example from docstring: lst1 has 2 odds, lst2 has 2 evens. 2 <= 2 is YES.
        self.assertEqual(exchange([1, 2, 3, 4], [1, 2, 3, 4]), "YES")

    def test_2_example_two_typical_no(self):
        # Example from docstring: lst1 has 2 odds, lst2 has 1 even. 2 <= 1 is NO.
        self.assertEqual(exchange([1, 2, 3, 4], [1, 5, 3, 4]), "NO")

    def test_3_boundary_equal_counts_yes(self):
        # Boundary condition: Number of odds in lst1 equals number of evens in lst2.
        # lst1 has 3 odds (1, 3, 5), lst2 has 3 evens (2, 4, 6). 3 <= 3 is YES.
        self.assertEqual(exchange([1, 3, 5], [2, 4, 6]), "YES")

    def test_4_boundary_one_more_odd_no(self):
        # Boundary condition: Number of odds in lst1 is one more than evens in lst2.
        # lst1 has 4 odds (1, 3, 5, 7), lst2 has 3 evens (2, 4, 6). 4 <= 3 is NO.
        # Catches potential off-by-one errors like using '<' instead of '<='.
        self.assertEqual(exchange([1, 3, 5, 7], [2, 4, 6]), "NO")

    def test_5_edge_lst1_already_all_even_yes(self):
        # Edge case: lst1 already contains only even numbers.
        # lst1 has 0 odds, lst2 has 0 evens. 0 <= 0 is YES.
        self.assertEqual(exchange([2, 4, 6], [1, 3, 5]), "YES")

    def test_6_edge_lst2_no_even_numbers_no(self):
        # Edge case: lst2 contains no even numbers to exchange.
        # lst1 has 2 odds (1, 3), lst2 has 0 evens. 2 <= 0 is NO.
        self.assertEqual(exchange([1, 2, 3], [1, 3, 5]), "NO")

    def test_7_single_element_lists_yes(self):
        # Edge case: Both lists have a single element, allowing exchange.
        # lst1 has 1 odd (1), lst2 has 1 even (2). 1 <= 1 is YES.
        self.assertEqual(exchange([1], [2]), "YES")

    def test_8_single_element_lists_no(self):
        # Edge case: Both lists have a single element, not allowing exchange.
        # lst1 has 1 odd (1), lst2 has 0 evens. 1 <= 0 is NO.
        self.assertEqual(exchange([1], [3]), "NO")

    def test_9_extreme_many_odds_many_evens_yes(self):
        # Extreme case: Many elements, many odds in lst1, sufficient evens in lst2.
        # lst1 has 10 odds, lst2 has 11 evens. 10 <= 11 is YES.
        self.assertEqual(exchange([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]), "YES")

    def test_10_extreme_zero_and_negative_numbers_no(self):
        # Extreme case: Includes zero and negative numbers, with duplicates.
        # 0 is even. Negative numbers parity: -3 is odd, -7 is odd, -2 is even.
        # lst1 = [1, 0, -3, 5, -7] -> Odds: -3, 5, -7 (3 odds)
        # lst2 = [-1, 3, 0] -> Evens: 0 (1 even)
        # 3 <= 1 is NO.
        self.assertEqual(exchange([1, 0, -3, 5, -7], [-1, 3, 0]), "NO")