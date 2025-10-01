import unittest
from sut.problem_HumanEval_149 import sorted_list_sum

class TestSortedListSum(unittest.TestCase):

    def test_1_basic_filtering_and_sorting_example_1(self):
        # Test case similar to the first example in the docstring
        input_list = ["aa", "a", "aaa"]
        expected_output = ["aa"]
        self.assertEqual(sorted_list_sum(input_list), expected_output)

    def test_2_basic_filtering_and_sorting_example_2(self):
        # Test case similar to the second example in the docstring
        input_list = ["ab", "a", "aaa", "cd"]
        expected_output = ["ab", "cd"]
        self.assertEqual(sorted_list_sum(input_list), expected_output)

    def test_3_all_odd_length_strings(self):
        # Test case where all strings have odd lengths, resulting in an empty list
        input_list = ["a", "b", "cde", "fghij"]
        expected_output = []
        self.assertEqual(sorted_list_sum(input_list), expected_output)

    def test_4_all_even_length_strings_different_lengths(self):
        # Test case with only even length strings, sorted primarily by length
        input_list = ["bbbb", "aa", "dddddd", "cc"]
        expected_output = ["aa", "cc", "bbbb", "dddddd"]
        self.assertEqual(sorted_list_sum(input_list), expected_output)

    def test_5_all_even_length_strings_same_length_alphabetical_sort(self):
        # Test case with only even length strings of the same length, sorted alphabetically
        input_list = ["cccc", "aaaa", "bbbb"]
        expected_output = ["aaaa", "bbbb", "cccc"]
        self.assertEqual(sorted_list_sum(input_list), expected_output)

    def test_6_empty_input_list(self):
        # Test case with an empty input list
        input_list = []
        expected_output = []
        self.assertEqual(sorted_list_sum(input_list), expected_output)

    def test_7_list_with_duplicates_some_filtered_some_kept(self):
        # Test case with duplicate strings, some of which are filtered out
        input_list = ["apple", "banana", "kiwi", "apple", "grape", "pear"]
        expected_output = ["kiwi", "pear", "banana"]
        self.assertEqual(sorted_list_sum(input_list), expected_output)

    def test_8_mixed_lengths_mixed_filtering_complex_sort(self):
        # Test case with a mix of odd and even length strings, requiring both length and alphabetical sorting
        input_list = ["cat", "dog", "elephant", "bird", "fish", "zebra"]
        expected_output = ["bird", "fish", "elephant"]
        self.assertEqual(sorted_list_sum(input_list), expected_output)

    def test_9_single_element_odd_length(self):
        # Test case with a single string of odd length
        input_list = ["hello"]
        expected_output = []
        self.assertEqual(sorted_list_sum(input_list), expected_output)

    def test_10_single_element_even_length(self):
        # Test case with a single string of even length
        input_list = ["python"]
        expected_output = ["python"]
        self.assertEqual(sorted_list_sum(input_list), expected_output)

if __name__ == '__main__':
    unittest.main()