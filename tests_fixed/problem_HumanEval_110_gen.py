import unittest
from sut_llm.problem_HumanEval_110 import exchange

class TestExchange(unittest.TestCase):

    def test_example_yes(self):
        # Example from docstring: lst1 has 2 odds, lst2 has 2 evens. 2 >= 2 -> YES
        self.assertEqual(exchange([1, 2, 3, 4], [1, 2, 3, 4]), "YES")

    def test_example_no(self):
        # Example from docstring: lst1 has 2 odds, lst2 has 1 even. 1 < 2 -> NO
        self.assertEqual(exchange([1, 2, 3, 4], [1, 5, 3, 4]), "NO")

    def test_lst1_already_all_even(self):
        # lst1 is already all even, no exchange needed. 0 odds in lst1, 0 evens in lst2. 0 >= 0 -> YES
        self.assertEqual(exchange([2, 4, 6], [1, 3, 5]), "YES")

    def test_lst1_all_odd_enough_evens(self):
        # lst1 is all odd, lst2 has exactly enough evens. 3 odds in lst1, 3 evens in lst2. 3 >= 3 -> YES
        self.assertEqual(exchange([1, 3, 5], [2, 4, 6]), "YES")

    def test_lst1_all_odd_not_enough_evens(self):
        # lst1 is all odd, lst2 does not have enough evens. 3 odds in lst1, 2 evens in lst2. 2 < 3 -> NO
        self.assertEqual(exchange([1, 3, 5], [2, 4]), "NO")

    def test_lst1_few_odds_lst2_many_evens(self):
        # lst1 has few odds, lst2 has many evens. 1 odd in lst1, 4 evens in lst2. 4 >= 1 -> YES
        self.assertEqual(exchange([1], [2, 4, 6, 8]), "YES")

    def test_lst1_many_odds_lst2_few_evens(self):
        # lst1 has many odds, lst2 has few evens. 5 odds in lst1, 2 evens in lst2. 2 < 5 -> NO
        self.assertEqual(exchange([1, 3, 5, 7, 9], [2, 4]), "NO")

    def test_mixed_parity_yes(self):
        # Mixed parity lists, enough evens. 2 odds in lst1, 2 evens in lst2. 2 >= 2 -> YES
        self.assertEqual(exchange([10, 1, 20, 3], [5, 6, 7, 8, 9]), "YES")

    def test_mixed_parity_no(self):
        # Mixed parity lists, not enough evens. 3 odds in lst1, 1 even in lst2. 1 < 3 -> NO
        self.assertEqual(exchange([10, 1, 20, 3, 5], [5, 6, 7, 9]), "NO")

    def test_single_element_lists(self):
        # Single element lists, enough evens. 1 odd in lst1, 1 even in lst2. 1 >= 1 -> YES
        self.assertEqual(exchange([1], [2]), "YES")

if __name__ == '__main__':
    unittest.main()