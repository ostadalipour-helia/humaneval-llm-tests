import unittest
from sut.problem_HumanEval_94 import skjkasdkd

class Test_skjkasdkd(unittest.TestCase):
    def test_normal_case_largest_prime_181(self):
        lst = [0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]
        self.assertEqual(skjkasdkd(lst), 10)

    def test_normal_case_largest_prime_4597(self):
        lst = [1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]
        self.assertEqual(skjkasdkd(lst), 25)

    def test_normal_case_largest_prime_5107(self):
        lst = [1, 3, 1, 32, 5107, 34, 83278, 109, 163, 23, 2323, 32, 30, 1, 9, 3]
        self.assertEqual(skjkasdkd(lst), 13)

    def test_edge_case_empty_list(self):
        lst = []
        self.assertEqual(skjkasdkd(lst), 0)

    def test_edge_case_no_prime_numbers(self):
        lst = [0, 1, 4, 6, 8, 9, 10, 12]
        self.assertEqual(skjkasdkd(lst), 0)

    def test_edge_case_single_prime_in_list(self):
        lst = [10, 11, 12, 14]
        self.assertEqual(skjkasdkd(lst), 2)

    def test_edge_case_negative_numbers_ignored(self):
        lst = [-2, -3, 5, 7, -10]
        self.assertEqual(skjkasdkd(lst), 7)

    def test_edge_case_large_prime_number(self):
        lst = [1000000007]
        self.assertEqual(skjkasdkd(lst), 8)

    def test_error_case_input_not_a_list(self):
        lst = "not_a_list"
        with self.assertRaises(TypeError):
            skjkasdkd(lst)

    def test_error_case_list_contains_string(self):
        lst = [1, 2, "three", 4]
        with self.assertRaises(TypeError):
            skjkasdkd(lst)

    def test_error_case_list_contains_float(self):
        lst = [1, 2, 3.5, 4]
        with self.assertRaises(TypeError):
            skjkasdkd(lst)