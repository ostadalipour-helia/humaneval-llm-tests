import unittest
from sut.problem_HumanEval_95 import check_dict_case

class Test_check_dict_case(unittest.TestCase):

    def test_normal_all_lowercase(self):
        # Description: All keys are lowercase strings.
        input_dict = {"a": "apple", "b": "banana"}
        original_dict_copy = input_dict.copy()
        expected_output = True
        result = check_dict_case(input_dict)
        self.assertEqual(result, expected_output)
        self.assertEqual(input_dict, original_dict_copy, "Input dictionary should remain unchanged.")

    def test_normal_all_uppercase(self):
        # Description: All keys are uppercase strings.
        input_dict = {"STATE": "NC", "ZIP": "12345"}
        original_dict_copy = input_dict.copy()
        expected_output = True
        result = check_dict_case(input_dict)
        self.assertEqual(result, expected_output)
        self.assertEqual(input_dict, original_dict_copy, "Input dictionary should remain unchanged.")

    def test_normal_mixed_case_keys(self):
        # Description: Keys contain a mix of lowercase and uppercase strings.
        input_dict = {"a": "apple", "A": "banana", "B": "banana"}
        original_dict_copy = input_dict.copy()
        expected_output = False
        result = check_dict_case(input_dict)
        self.assertEqual(result, expected_output)
        self.assertEqual(input_dict, original_dict_copy, "Input dictionary should remain unchanged.")

    def test_edge_empty_dict(self):
        # Description: The dictionary is empty.
        input_dict = {}
        original_dict_copy = input_dict.copy()
        expected_output = False
        result = check_dict_case(input_dict)
        self.assertEqual(result, expected_output)
        self.assertEqual(input_dict, original_dict_copy, "Input dictionary should remain unchanged.")

    def test_edge_lowercase_digit_string_key(self):
        # Description: Keys are strings, all lowercase, one is a digit string.
        input_dict = {"a": "apple", "8": "banana"}
        original_dict_copy = input_dict.copy()
        expected_output = True
        result = check_dict_case(input_dict)
        self.assertEqual(result, expected_output)
        self.assertEqual(input_dict, original_dict_copy, "Input dictionary should remain unchanged.")

    def test_edge_non_string_key(self):
        # Description: Keys include non-string types (assuming 8 is an int key, not string '8').
        input_dict = {"a": "apple", 8: "banana"}
        original_dict_copy = input_dict.copy()
        expected_output = False
        result = check_dict_case(input_dict)
        self.assertEqual(result, expected_output)
        self.assertEqual(input_dict, original_dict_copy, "Input dictionary should remain unchanged.")

    def test_edge_single_uppercase_key(self):
        # Description: Dictionary with a single uppercase string key.
        input_dict = {"A": 1}
        original_dict_copy = input_dict.copy()
        expected_output = True
        result = check_dict_case(input_dict)
        self.assertEqual(result, expected_output)
        self.assertEqual(input_dict, original_dict_copy, "Input dictionary should remain unchanged.")

    def test_edge_single_lowercase_key(self):
        # Description: Dictionary with a single lowercase string key.
        input_dict = {"a": 1}
        original_dict_copy = input_dict.copy()
        expected_output = True
        result = check_dict_case(input_dict)
        self.assertEqual(result, expected_output)
        self.assertEqual(input_dict, original_dict_copy, "Input dictionary should remain unchanged.")

    def test_error_none_input(self):
        # Description: Input is not a dictionary (None).
        with self.assertRaises(TypeError):
            check_dict_case(None)

    def test_error_list_input(self):
        # Description: Input is not a dictionary (list).
        with self.assertRaises(TypeError):
            check_dict_case([])

    def test_error_string_input(self):
        # Description: Input is not a dictionary (string).
        with self.assertRaises(TypeError):
            check_dict_case("hello")

    def test_error_int_input(self):
        # Description: Input is not a dictionary (integer).
        with self.assertRaises(TypeError):
            check_dict_case(123)