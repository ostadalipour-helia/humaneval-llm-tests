import unittest
from sut_llm.problem_HumanEval_149 import sorted_list_sum

class TestSortedListSum(unittest.TestCase):

    def test_1_basic_mixed_lengths_and_duplicates(self):
        # Typical/Expected input: mixed odd/even lengths, some duplicates, verifies filtering and sorting.
        input_list = ["aa", "a", "aaa", "bb", "b", "cccc", "aa"]
        expected_output = ["aa", "aa", "bb", "cccc"]
        self.assertListEqual(sorted_list_sum(input_list), expected_output)

    def test_2_docstring_example_1(self):
        # Typical/Expected input: Verifies basic filtering and sorting as per docstring example.
        input_list = ["aa", "a", "aaa"]
        expected_output = ["aa"]
        self.assertListEqual(sorted_list_sum(input_list), expected_output)

    def test_3_docstring_example_2(self):
        # Typical/Expected input: Verifies sorting by length then alphabetically as per docstring example.
        input_list = ["ab", "a", "aaa", "cd"]
        expected_output = ["ab", "cd"]
        self.assertListEqual(sorted_list_sum(input_list), expected_output)

    def test_4_edge_case_empty_input_list(self):
        # Edge Case: Empty input list should return an empty list.
        input_list = []
        expected_output = []
        self.assertListEqual(sorted_list_sum(input_list), expected_output)

    def test_5_edge_case_all_odd_length_strings(self):
        # Edge Case: All strings have odd lengths, resulting in an empty list after filtering.
        # Tests the filtering logic thoroughly (logic mutation).
        input_list = ["a", "b", "cde", "fghij", "klmno"]
        expected_output = []
        self.assertListEqual(sorted_list_sum(input_list), expected_output)

    def test_6_edge_case_all_even_length_strings(self):
        # Edge Case: All strings have even lengths, all should be kept and sorted.
        # Tests the filtering logic (logic mutation) and sorting.
        input_list = ["bb", "aa", "eeff", "ccdd"]
        expected_output = ["aa", "bb", "ccdd", "eeff"] # Sorted by length (all 2 then all 4), then alphabetically
        self.assertListEqual(sorted_list_sum(input_list), expected_output)

    def test_7_boundary_single_even_length_string(self):
        # Boundary Test: Single element list with an even length string.
        # Tests off-by-one for length check (length 2).
        input_list = ["word"]
        expected_output = ["word"]
        self.assertListEqual(sorted_list_sum(input_list), expected_output)

    def test_8_boundary_single_odd_length_string(self):
        # Boundary Test: Single element list with an odd length string.
        # Tests off-by-one for length check (length 1 or 3).
        input_list = ["a"]
        expected_output = []
        self.assertListEqual(sorted_list_sum(input_list), expected_output)

    def test_9_extreme_multiple_same_even_length_for_alphabetical_sort(self):
        # Extreme/Unusual Input: Multiple strings of the same even length to rigorously test alphabetical sorting.
        # Also includes mixed odd/even lengths.
        input_list = ["apple", "banana", "grape", "orange", "kiwi", "pear", "plum", "date"]
        # "apple" (5, odd) -> removed
        # "banana" (6, even)
        # "grape" (5, odd) -> removed
        # "orange" (6, even)
        # "kiwi" (4, even)
        # "pear" (4, even)
        # "plum" (4, even)
        # "date" (4, even)
        expected_output = ["date", "kiwi", "pear", "plum", "banana", "orange"]
        self.assertListEqual(sorted_list_sum(input_list), expected_output)

    def test_10_extreme_empty_string_and_very_long_strings(self):
        # Extreme/Unusual Input: Includes an empty string (length 0, even) and very long strings.
        # Tests boundary for length 0 and large lengths.
        input_list = ["", "a", "bb", "ccc", "dddd", "eeeeeeeeeeeeeeeeeeee", "f"]
        # "" (0, even)
        # "a" (1, odd) -> removed
        # "bb" (2, even)
        # "ccc" (3, odd) -> removed
        # "dddd" (4, even)
        # "eeeeeeeeeeeeeeeeeeee" (20, even)
        # "f" (1, odd) -> removed
        expected_output = ["", "bb", "dddd", "eeeeeeeeeeeeeeeeeeee"]
        self.assertListEqual(sorted_list_sum(input_list), expected_output)