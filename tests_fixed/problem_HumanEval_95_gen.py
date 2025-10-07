import unittest
from sut_llm.problem_HumanEval_95 import check_dict_case

class TestCheckDictCase(unittest.TestCase):

    def test_empty_dictionary(self):
        """Test case for an empty dictionary."""
        self.assertFalse(check_dict_case({}))

    def test_all_lowercase_keys(self):
        """Test case with all keys being lowercase strings."""
        self.assertTrue(check_dict_case({"a": "apple", "b": "banana"}))

    def test_all_uppercase_keys(self):
        """Test case with all keys being uppercase strings."""
        self.assertTrue(check_dict_case({"STATE": "NC", "ZIP": "12345"}))

    def test_mixed_case_string_keys(self):
        """Test case with a mix of lowercase and uppercase string keys."""
        self.assertFalse(check_dict_case({"a": "apple", "A": "banana", "B": "banana"}))

    def test_non_string_key_present(self):
        """Test case with a non-string key present."""
        self.assertFalse(check_dict_case({"a": "apple", 8: "banana", "c": "cherry"}))

    def test_mixed_case_string_keys_another_example(self):
        """Another test case with mixed case string keys."""
        self.assertFalse(check_dict_case({"Name": "John", "Age": "36", "City": "Houston"}))

    def test_single_lowercase_key(self):
        """Test case with a single lowercase string key."""
        self.assertTrue(check_dict_case({"key": "value"}))

    def test_single_uppercase_key(self):
        """Test case with a single uppercase string key."""
        self.assertTrue(check_dict_case({"KEY": "VALUE"}))

    def test_keys_with_mixed_types_and_cases(self):
        """Test case with a mix of non-string keys and string keys of different cases."""
        self.assertFalse(check_dict_case({"a": 1, 10: 2, "B": 3}))

    def test_keys_not_purely_lower_or_upper(self):
        """Test case where string keys are neither purely lowercase nor purely uppercase."""
        self.assertFalse(check_dict_case({"aBc": 1, "DeF": 2}))

if __name__ == '__main__':
    unittest.main()