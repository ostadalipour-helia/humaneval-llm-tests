import unittest
from sut.problem_HumanEval_7 import filter_by_substring

class Test_filter_by_substring(unittest.TestCase):

    def test_normal_common_substring(self):
        # Description: Filter a list of strings for a common substring.
        strings_input = ["abc", "bacd", "cde", "array"]
        substring_input = "a"
        expected_output = ["abc", "bacd", "array"]
        
        # Test postcondition: The original 'strings' list must not be modified.
        original_strings_copy = list(strings_input) 

        result = filter_by_substring(strings_input, substring_input)
        self.assertEqual(result, expected_output)
        self.assertEqual(strings_input, original_strings_copy, "Original strings list was modified.")

    def test_normal_multiple_matches(self):
        # Description: Filter strings where multiple matches exist.
        strings_input = ["hello", "world", "python"]
        substring_input = "o"
        expected_output = ["hello", "world"]

        original_strings_copy = list(strings_input)

        result = filter_by_substring(strings_input, substring_input)
        self.assertEqual(result, expected_output)
        self.assertEqual(strings_input, original_strings_copy, "Original strings list was modified.")

    def test_normal_no_match(self):
        # Description: No strings contain the given substring.
        strings_input = ["apple", "banana", "cherry"]
        substring_input = "z"
        expected_output = []

        original_strings_copy = list(strings_input)

        result = filter_by_substring(strings_input, substring_input)
        self.assertEqual(result, expected_output)
        self.assertEqual(strings_input, original_strings_copy, "Original strings list was modified.")

    def test_edge_empty_strings_list(self):
        # Description: Input list of strings is empty.
        strings_input = []
        substring_input = "a"
        expected_output = []

        original_strings_copy = list(strings_input)

        result = filter_by_substring(strings_input, substring_input)
        self.assertEqual(result, expected_output)
        self.assertEqual(strings_input, original_strings_copy, "Original strings list was modified.")

    def test_edge_empty_substring(self):
        # Description: Substring is an empty string (all strings contain an empty string).
        strings_input = ["abc", "def", "ghi"]
        substring_input = ""
        expected_output = ["abc", "def", "ghi"]

        original_strings_copy = list(strings_input)

        result = filter_by_substring(strings_input, substring_input)
        self.assertEqual(result, expected_output)
        self.assertEqual(strings_input, original_strings_copy, "Original strings list was modified.")

    def test_edge_case_sensitive(self):
        # Description: Case-sensitive filtering.
        strings_input = ["apple", "Apple", "APple"]
        substring_input = "apple"
        expected_output = ["apple"]

        original_strings_copy = list(strings_input)

        result = filter_by_substring(strings_input, substring_input)
        self.assertEqual(result, expected_output)
        self.assertEqual(strings_input, original_strings_copy, "Original strings list was modified.")

    def test_edge_substring_is_full_string(self):
        # Description: Substring is an entire string in the list.
        strings_input = ["fullmatch", "partial", "nomatch"]
        substring_input = "fullmatch"
        expected_output = ["fullmatch"]

        original_strings_copy = list(strings_input)

        result = filter_by_substring(strings_input, substring_input)
        self.assertEqual(result, expected_output)
        self.assertEqual(strings_input, original_strings_copy, "Original strings list was modified.")

    def test_edge_substring_multiple_times_in_string(self):
        # Description: Substring appears multiple times within a single string.
        strings_input = ["aaaaa", "bbbbb", "ccccc"]
        substring_input = "a"
        expected_output = ["aaaaa"]

        original_strings_copy = list(strings_input)

        result = filter_by_substring(strings_input, substring_input)
        self.assertEqual(result, expected_output)
        self.assertEqual(strings_input, original_strings_copy, "Original strings list was modified.")

    def test_error_strings_not_list(self):
        # Description: The 'strings' argument is not a list.
        strings_input = "not_a_list"
        substring_input = "a"
        with self.assertRaises(TypeError):
            filter_by_substring(strings_input, substring_input)

    def test_error_strings_elements_not_str(self):
        # Description: Elements in 'strings' list are not all strings.
        strings_input = [123, "abc"]
        substring_input = "a"
        with self.assertRaises(TypeError):
            filter_by_substring(strings_input, substring_input)

    def test_error_substring_not_str(self):
        # Description: The 'substring' argument is not a string.
        strings_input = ["abc", "def"]
        substring_input = 123
        with self.assertRaises(TypeError):
            filter_by_substring(strings_input, substring_input)