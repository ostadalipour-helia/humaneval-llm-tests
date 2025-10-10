import unittest
from sut_llm.problem_HumanEval_95 import check_dict_case

class TestCheckDictCase(unittest.TestCase):

    def test_1_empty_dictionary(self):
        # Edge Case: Empty dictionary should return False as per docstring.
        self.assertFalse(check_dict_case({}))

    def test_2_all_lowercase_keys(self):
        # Boundary/Typical: All keys are lowercase strings.
        self.assertTrue(check_dict_case({"apple": 1, "banana": 2, "cherry": 3}))

    def test_3_all_uppercase_keys(self):
        # Boundary/Typical: All keys are uppercase strings.
        self.assertTrue(check_dict_case({"APPLE": 1, "BANANA": 2, "CHERRY": 3}))

    def test_4_mixed_case_string_keys(self):
        # Logic Mutation/Boundary: Keys are a mix of lowercase and uppercase strings.
        self.assertFalse(check_dict_case({"a": 1, "B": 2}))

    def test_5_dictionary_with_non_string_keys(self):
        # Logic Mutation/Edge Case: Contains non-string keys (e.g., integer).
        self.assertFalse(check_dict_case({"a": 1, 2: "two", "c": 3}))

    def test_6_single_lowercase_string_key(self):
        # Off-by-One/Edge Case: Dictionary with a single lowercase string key.
        self.assertTrue(check_dict_case({"single": "value"}))

    def test_7_single_uppercase_string_key(self):
        # Off-by-One/Edge Case: Dictionary with a single uppercase string key.
        self.assertTrue(check_dict_case({"SINGLE": "VALUE"}))

    def test_8_keys_with_mixed_casing_styles_from_docstring_example(self):
        # Logic Mutation/Boundary: Keys are strings but not strictly all lower or all upper (e.g., Title Case).
        self.assertFalse(check_dict_case({"Name": "John", "Age": "36", "City": "Houston"}))

    def test_9_keys_with_numbers_and_symbols_but_consistent_case(self):
        # Extreme/Unusual: Keys contain non-alphabetic characters but maintain consistent case.
        self.assertTrue(check_dict_case({"key_1": "value1", "key-2": "value2"}))

    def test_10_dictionary_with_an_empty_string_key(self):
        # Extreme/Unusual/Edge Case: Dictionary contains an empty string as a key.
        # An empty string is neither lower nor upper, so it should cause False.
        self.assertFalse(check_dict_case({"": "empty", "a": "value"}))