import unittest
from sut.problem_HumanEval_29 import filter_by_prefix

class Test_filter_by_prefix(unittest.TestCase):

    def test_normal_basic_filter(self):
        strings = ["abc", "bcd", "cde", "array"]
        prefix = "a"
        original_strings = list(strings) # Copy for invariant check
        expected_output = ["abc", "array"]
        result = filter_by_prefix(strings, prefix)
        self.assertEqual(result, expected_output)
        self.assertEqual(strings, original_strings) # Invariant check

    def test_normal_multiple_matches(self):
        strings = ["apple", "banana", "apricot", "grape"]
        prefix = "ap"
        original_strings = list(strings)
        expected_output = ["apple", "apricot"]
        result = filter_by_prefix(strings, prefix)
        self.assertEqual(result, expected_output)
        self.assertEqual(strings, original_strings)

    def test_normal_no_match(self):
        strings = ["cat", "dog", "cow"]
        prefix = "z"
        original_strings = list(strings)
        expected_output = []
        result = filter_by_prefix(strings, prefix)
        self.assertEqual(result, expected_output)
        self.assertEqual(strings, original_strings)

    def test_normal_all_match(self):
        strings = ["test", "testing", "tester"]
        prefix = "test"
        original_strings = list(strings)
        expected_output = ["test", "testing", "tester"]
        result = filter_by_prefix(strings, prefix)
        self.assertEqual(result, expected_output)
        self.assertEqual(strings, original_strings)

    def test_edge_empty_list(self):
        strings = []
        prefix = "a"
        original_strings = list(strings)
        expected_output = []
        result = filter_by_prefix(strings, prefix)
        self.assertEqual(result, expected_output)
        self.assertEqual(strings, original_strings)

    def test_edge_empty_prefix(self):
        strings = ["abc", "def"]
        prefix = ""
        original_strings = list(strings)
        expected_output = ["abc", "def"]
        result = filter_by_prefix(strings, prefix)
        self.assertEqual(result, expected_output)
        self.assertEqual(strings, original_strings)

    def test_edge_single_element_match(self):
        strings = ["apple"]
        prefix = "ap"
        original_strings = list(strings)
        expected_output = ["apple"]
        result = filter_by_prefix(strings, prefix)
        self.assertEqual(result, expected_output)
        self.assertEqual(strings, original_strings)

    def test_edge_prefix_longer_than_string(self):
        strings = ["short", "longer"]
        prefix = "verylongprefix"
        original_strings = list(strings)
        expected_output = []
        result = filter_by_prefix(strings, prefix)
        self.assertEqual(result, expected_output)
        self.assertEqual(strings, original_strings)

    def test_error_strings_is_none(self):
        with self.assertRaises(TypeError):
            filter_by_prefix(None, "a")

    def test_error_prefix_is_none(self):
        with self.assertRaises(TypeError):
            filter_by_prefix(["a", "b"], None)

    def test_error_strings_not_list(self):
        with self.assertRaises(TypeError):
            filter_by_prefix("not a list", "a")

    def test_error_list_contains_non_str(self):
        # This will raise AttributeError when .startswith is called on an int
        with self.assertRaises(AttributeError):
            filter_by_prefix(["a", 1, "b"], "a")