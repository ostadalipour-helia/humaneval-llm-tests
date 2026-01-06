import unittest
from sut.problem_HumanEval_110 import exchange

class Test_exchange(unittest.TestCase):

    # Normal Cases
    def test_normal_case_1(self):
        # lst1 has 2 odd numbers (1, 3). lst2 has 2 even numbers (2, 4). 2 <= 2, so 'YES'.
        self.assertEqual(exchange([1, 2, 3, 4], [1, 2, 3, 4]), "YES")

    def test_normal_case_2(self):
        # lst1 has 2 odd numbers (1, 3). lst2 has 1 even number (4). 2 > 1, so 'NO'.
        self.assertEqual(exchange([1, 2, 3, 4], [1, 5, 3, 4]), "NO")

    def test_normal_case_3(self):
        # lst1 has 0 odd numbers. lst2 has 0 even numbers. 0 <= 0, so 'YES'.
        self.assertEqual(exchange([2, 4, 6], [1, 3, 5]), "YES")

    def test_normal_case_4(self):
        # lst1 has 3 odd numbers (1, 3, 5). lst2 has 3 even numbers (2, 4, 6). 3 <= 3, so 'YES'.
        self.assertEqual(exchange([1, 3, 5], [2, 4, 6]), "YES")

    # Edge Cases
    def test_edge_case_single_element_yes(self):
        # lst1 has 1 odd number. lst2 has 1 even number. 1 <= 1, so 'YES'.
        self.assertEqual(exchange([1], [2]), "YES")

    def test_edge_case_single_element_no(self):
        # lst1 has 1 odd number. lst2 has 0 even numbers. 1 > 0, so 'NO'.
        self.assertEqual(exchange([1], [3]), "NO")

    def test_edge_case_no_odds_no_evens(self):
        # lst1 has 0 odd numbers. lst2 has 0 even numbers. 0 <= 0, so 'YES'.
        self.assertEqual(exchange([2], [1]), "YES")

    def test_edge_case_more_odds_than_evens(self):
        # lst1 has 2 odd numbers. lst2 has 1 even number. 2 > 1, so 'NO'.
        self.assertEqual(exchange([1, 3], [2]), "NO")

    # Error Cases
    def test_error_lst1_not_list(self):
        # `lst1` is not a list.
        with self.assertRaises(TypeError):
            exchange("not_a_list", [1, 2])

    def test_error_lst2_not_list(self):
        # `lst2` is not a list.
        with self.assertRaises(TypeError):
            exchange([1, 2], None)

    def test_error_lst1_contains_non_int(self):
        # `lst1` contains non-integer elements.
        with self.assertRaises(TypeError):
            exchange([1, "a", 3], [2, 4])

    def test_error_lst2_contains_non_int_float(self):
        # `lst2` contains non-integer elements (float).
        with self.assertRaises(TypeError):
            exchange([1, 2], [3, 4.5])