import unittest
from sut.problem_HumanEval_95 import check_dict_case

class Test_check_dict_case(unittest.TestCase):

    def test_all_lowercase_keys(self):
        self.assertEqual(check_dict_case({'a': 'apple', 'b': 'banana'}), True)

    def test_all_uppercase_keys(self):
        self.assertEqual(check_dict_case({'STATE': 'NC', 'ZIP': '12345'}), True)

    def test_mixed_case_keys(self):
        self.assertEqual(check_dict_case({'a': 'apple', 'A': 'banana', 'B': 'banana'}), False)

    def test_lowercase_keys_mixed_values(self):
        self.assertEqual(check_dict_case({'a': 'apple', 'b': 'banana', 'c': 1}), True)

    def test_title_case_keys(self):
        self.assertEqual(check_dict_case({'Name': 'John', 'Age': '36', 'City': 'Houston'}), False)

    def test_another_mixed_case(self):
        self.assertEqual(check_dict_case({'a': 'apple', 'b': 'banana', 'C': 'cherry'}), True)

    def test_empty_dict(self):
        self.assertEqual(check_dict_case({}), False)

    def test_lowercase_and_digit_string_keys(self):
        self.assertEqual(check_dict_case({'a': 'apple', '8': 'banana'}), False)

    def test_uppercase_and_digit_string_keys(self):
        self.assertEqual(check_dict_case({'A': 'apple', '8': 'banana'}), False)

    def test_single_uppercase_key(self):
        self.assertEqual(check_dict_case({'A': 1}), True)