import unittest
from sut.problem_HumanEval_149 import sorted_list_sum

class Test_sorted_list_sum(unittest.TestCase):
    def test_normal_case_filter_and_sort_single_even(self):
        lst = ["aa", "a", "aaa"]
        expected_output = ["aa"]
        self.assertEqual(sorted_list_sum(lst), expected_output)

    def test_normal_case_filter_and_sort_multiple_even_same_length(self):
        lst = ["ab", "a", "aaa", "cd"]
        expected_output = ["ab", "cd"]
        self.assertEqual(sorted_list_sum(lst), expected_output)

    def test_normal_case_mixed_lengths_filter_and_sort(self):
        lst = ["apple", "banana", "cat", "dog", "elephant", "zebra", "ant", "bat"]
        expected_output = ["banana", "elephant"]
        self.assertEqual(sorted_list_sum(lst), expected_output)

    def test_normal_case_filter_and_sort_equal_length_alphabetical(self):
        lst = ["date", "pear", "fig", "grape"]
        expected_output = ["date", "pear"]
        self.assertEqual(sorted_list_sum(lst), expected_output)

    def test_edge_case_empty_list(self):
        lst = []
        expected_output = []
        self.assertEqual(sorted_list_sum(lst), expected_output)

    def test_edge_case_all_odd_lengths(self):
        lst = ["a", "abc", "abcde"]
        expected_output = []
        self.assertEqual(sorted_list_sum(lst), expected_output)

    def test_edge_case_all_same_even_length_alphabetical_sort(self):
        lst = ["aa", "bb", "cc"]
        expected_output = ["aa", "bb", "cc"]
        self.assertEqual(sorted_list_sum(lst), expected_output)

    def test_edge_case_multiple_lengths_with_duplicates_complex_sort(self):
        lst = ["aaaa", "bb", "cc", "dddd"]
        expected_output = ["bb", "cc", "aaaa", "dddd"]
        self.assertEqual(sorted_list_sum(lst), expected_output)

    def test_edge_case_mixed_odd_even_lengths_varying_lengths(self):
        lst = ["even", "odd", "eveneven", "oddd"]
        expected_output = ["even", "eveneven"]
        self.assertEqual(sorted_list_sum(lst), expected_output)