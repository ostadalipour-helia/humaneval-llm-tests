import unittest
from sut_llm.problem_HumanEval_113 import odd_count

class TestOddCount(unittest.TestCase):

    def test_01_empty_list(self):
        self.assertEqual(odd_count([]), [])

    def test_02_list_with_one_empty_string(self):
        self.assertEqual(odd_count(['']), ["the number of odd elements 0n the str0ng 0 of the 0nput."])

    def test_03_list_with_one_all_even_string(self):
        self.assertEqual(odd_count(['24680']), ["the number of odd elements 0n the str0ng 0 of the 0nput."])

    def test_04_list_with_one_all_odd_string(self):
        self.assertEqual(odd_count(['13579']), ["the number of odd elements 5n the str5ng 5 of the 5nput."])

    def test_05_list_with_one_mixed_string(self):
        self.assertEqual(odd_count(['12345']), ["the number of odd elements 3n the str3ng 3 of the 3nput."])

    def test_06_list_with_multiple_strings_varying_counts(self):
        input_list = ['1', '2', '34', '567']
        expected_output = [
            "the number of odd elements 1n the str1ng 1 of the 1nput.",
            "the number of odd elements 0n the str0ng 0 of the 0nput.",
            "the number of odd elements 1n the str1ng 1 of the 1nput.",
            "the number of odd elements 2n the str2ng 2 of the 2nput."
        ]
        self.assertEqual(odd_count(input_list), expected_output)

    def test_07_list_with_long_string_many_odds(self):
        input_list = ['12345678901234567890']
        expected_output = ["the number of odd elements 10n the str10ng 10 of the 10nput."]
        self.assertEqual(odd_count(input_list), expected_output)

    def test_08_list_with_strings_same_odd_count(self):
        input_list = ['13', '57', '91']
        expected_output = [
            "the number of odd elements 2n the str2ng 2 of the 2nput.",
            "the number of odd elements 2n the str2ng 2 of the 2nput.",
            "the number of odd elements 2n the str2ng 2 of the 2nput."
        ]
        self.assertEqual(odd_count(input_list), expected_output)

    def test_09_list_with_single_digit_strings(self):
        input_list = ['1', '2', '3', '4', '5']
        expected_output = [
            "the number of odd elements 1n the str1ng 1 of the 1nput.",
            "the number of odd elements 0n the str0ng 0 of the 0nput.",
            "the number of odd elements 1n the str1ng 1 of the 1nput.",
            "the number of odd elements 0n the str0ng 0 of the 0nput.",
            "the number of odd elements 1n the str1ng 1 of the 1nput."
        ]
        self.assertEqual(odd_count(input_list), expected_output)

    def test_10_list_with_mixed_types_of_strings(self):
        input_list = ['', '24', '135', '123']
        expected_output = [
            "the number of odd elements 0n the str0ng 0 of the 0nput.",
            "the number of odd elements 0n the str0ng 0 of the 0nput.",
            "the number of odd elements 3n the str3ng 3 of the 3nput.",
            "the number of odd elements 2n the str2ng 2 of the 2nput."
        ]
        self.assertEqual(odd_count(input_list), expected_output)