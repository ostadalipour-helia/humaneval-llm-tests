import unittest
from sut.problem_HumanEval_7 import filter_by_substring

class Test_filter_by_substring(unittest.TestCase):

    def test_filter_common_substring(self):
        args = {
            "strings": [
                "abc",
                "bacd",
                "cde",
                "array"
            ],
            "substring": "a"
        }
        expected = ['abc', 'bacd', 'array']
        self.assertEqual(filter_by_substring(**args), expected)

    def test_filter_multiple_matches(self):
        args = {
            "strings": [
                "hello",
                "world",
                "python"
            ],
            "substring": "o"
        }
        expected = ['hello', 'world', 'python']
        self.assertEqual(filter_by_substring(**args), expected)

    def test_no_matches(self):
        args = {
            "strings": [
                "apple",
                "banana",
                "cherry"
            ],
            "substring": "z"
        }
        expected = []
        self.assertEqual(filter_by_substring(**args), expected)

    def test_empty_input_list(self):
        args = {
            "strings": [],
            "substring": "a"
        }
        expected = []
        self.assertEqual(filter_by_substring(**args), expected)

    def test_empty_substring(self):
        args = {
            "strings": [
                "abc",
                "def",
                "ghi"
            ],
            "substring": ""
        }
        expected = ['abc', 'def', 'ghi']
        self.assertEqual(filter_by_substring(**args), expected)

    def test_case_sensitive_filtering(self):
        args = {
            "strings": [
                "apple",
                "Apple",
                "APple"
            ],
            "substring": "apple"
        }
        expected = ['apple']
        self.assertEqual(filter_by_substring(**args), expected)

    def test_substring_is_entire_string(self):
        args = {
            "strings": [
                "fullmatch",
                "partial",
                "nomatch"
            ],
            "substring": "fullmatch"
        }
        expected = ['fullmatch']
        self.assertEqual(filter_by_substring(**args), expected)

    def test_substring_appears_multiple_times_in_string(self):
        args = {
            "strings": [
                "aaaaa",
                "bbbbb",
                "ccccc"
            ],
            "substring": "a"
        }
        expected = ['aaaaa']
        self.assertEqual(filter_by_substring(**args), expected)

    def test_postcondition_original_list_unmodified(self):
        # Postcondition test: The original 'strings' list must not be modified.
        original_list = ['abc', 'bacd', 'cde', 'array']
        list_to_pass = original_list[:]
        filter_by_substring(strings=list_to_pass, substring='a')
        self.assertEqual(list_to_pass, original_list, "The original list should not be modified.")

    def test_postcondition_all_returned_strings_contain_substring(self):
        # Postcondition test: Every string in the returned list must contain the 'substring'.
        input_list = ['abc', 'bacd', 'cde', 'array']
        substring = 'a'
        result = filter_by_substring(strings=input_list, substring=substring)
        for item in result:
            self.assertIn(substring, item)