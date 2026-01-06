import unittest
from sut.problem_HumanEval_74 import total_match

class Test_total_match(unittest.TestCase):

    def test_normal_case_1_lst2_shorter(self):
        lst1 = ["hi", "admin"]
        lst2 = ["hI", "Hi"]
        # char_count(lst1) = 2 + 5 = 7
        # char_count(lst2) = 2 + 2 = 4
        # 7 > 4, so lst2 should be returned
        expected_output = ["hI", "Hi"]
        self.assertEqual(total_match(lst1, lst2), expected_output)

    def test_normal_case_2_lst1_shorter(self):
        lst1 = ["hi", "admin"]
        lst2 = ["hi", "hi", "admin", "project"]
        # char_count(lst1) = 2 + 5 = 7
        # char_count(lst2) = 2 + 2 + 5 + 7 = 16
        # 7 < 16, so lst1 should be returned
        expected_output = ["hi", "admin"]
        self.assertEqual(total_match(lst1, lst2), expected_output)

    def test_normal_case_3_lst2_shorter_again(self):
        lst1 = ["hi", "admin"]
        lst2 = ["hI", "hi", "hi"]
        # char_count(lst1) = 2 + 5 = 7
        # char_count(lst2) = 2 + 2 + 2 = 6
        # 7 > 6, so lst2 should be returned
        expected_output = ["hI", "hi", "hi"]
        self.assertEqual(total_match(lst1, lst2), expected_output)

    def test_normal_case_4_single_element_lst1_shorter(self):
        lst1 = ["4"]
        lst2 = ["1", "2", "3", "4", "5"]
        # char_count(lst1) = 1
        # char_count(lst2) = 1 + 1 + 1 + 1 + 1 = 5
        # 1 < 5, so lst1 should be returned
        expected_output = ["4"]
        self.assertEqual(total_match(lst1, lst2), expected_output)

    def test_edge_case_empty_lists(self):
        lst1 = []
        lst2 = []
        # char_count(lst1) = 0
        # char_count(lst2) = 0
        # 0 == 0, so lst1 should be returned
        expected_output = []
        self.assertEqual(total_match(lst1, lst2), expected_output)

    def test_edge_case_equal_length_single_char(self):
        lst1 = ["a"]
        lst2 = ["b"]
        # char_count(lst1) = 1
        # char_count(lst2) = 1
        # 1 == 1, so lst1 should be returned
        expected_output = ["a"]
        self.assertEqual(total_match(lst1, lst2), expected_output)

    def test_edge_case_long_vs_short_strings(self):
        lst1 = ["longstring"]
        lst2 = ["short"]
        # char_count(lst1) = 10
        # char_count(lst2) = 5
        # 10 > 5, so lst2 should be returned
        expected_output = ["short"]
        self.assertEqual(total_match(lst1, lst2), expected_output)

    def test_error_lst1_not_list(self):
        lst1 = None
        lst2 = ["a"]
        with self.assertRaises(TypeError):
            total_match(lst1, lst2)

    def test_error_lst2_not_list(self):
        lst1 = ["a"]
        lst2 = 123
        with self.assertRaises(TypeError):
            total_match(lst1, lst2)

    def test_error_lst1_contains_non_string(self):
        lst1 = ["a", 1, "b"]
        lst2 = ["c"]
        with self.assertRaises(TypeError):
            total_match(lst1, lst2)

    def test_error_lst2_contains_non_string(self):
        lst1 = ["a"]
        lst2 = ["b", None]
        with self.assertRaises(TypeError):
            total_match(lst1, lst2)