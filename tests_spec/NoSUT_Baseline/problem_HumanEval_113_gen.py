import unittest
import sut.problem_HumanEval_113 as mod

class TestHybrid(unittest.TestCase):
    def test_example_one(self):
            # Test case from the docstring example 1
            self.assertEqual(mod.odd_count(['1234567']), ["the number of odd elements 4n the str4ng 4 of the 4nput."])

    def test_example_two(self):
            # Test case from the docstring example 2
            self.assertEqual(mod.odd_count(['3',"11111111"]), ["the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 8n the str8ng 8 of the 8nput."])

    def test_empty_list(self):
            # Edge case: empty input list
            self.assertEqual(mod.odd_count([]), [])

    def test_list_with_empty_strings(self):
            # Edge case: list containing empty strings, tests count 0
            self.assertEqual(mod.odd_count(['', '']), ["the number of odd elements 0n the str0ng 0 of the 0nput.", "the number of odd elements 0n the str0ng 0 of the 0nput."])

    def test_all_even_digits(self):
            # Boundary condition: string with no odd digits (count 0)
            self.assertEqual(mod.odd_count(['24680']), ["the number of odd elements 0n the str0ng 0 of the 0nput."])

    def test_all_odd_digits(self):
            # Boundary condition: string with all odd digits (max count for its length)
            self.assertEqual(mod.odd_count(['13579']), ["the number of odd elements 5n the str5ng 5 of the 5nput."])

    def test_single_digit_strings(self):
            # Off-by-one/Boundary: list of single-digit strings (mix of odd/even)
            self.assertEqual(mod.odd_count(['1', '2', '3', '0']), [
                "the number of odd elements 1n the str1ng 1 of the 1nput.",
                "the number of odd elements 0n the str0ng 0 of the 0nput.",
                "the number of odd elements 1n the str1ng 1 of the 1nput.",
                "the number of odd elements 0n the str0ng 0 of the 0nput."
            ])

    def test_long_string_mixed_digits(self):
            # Extreme input: a very long string with mixed odd/even digits
            # Count of odd digits in '12345678901234567890' is 10
            self.assertEqual(mod.odd_count(['12345678901234567890']), ["the number of odd elements 10n the str10ng 10 of the 10nput."])

    def test_duplicate_strings(self):
            # Edge case: list with duplicate strings to ensure independent processing
            self.assertEqual(mod.odd_count(['12', '34', '12']), [
                "the number of odd elements 1n the str1ng 1 of the 1nput.",
                "the number of odd elements 1n the str1ng 1 of the 1nput.",
                "the number of odd elements 1n the str1ng 1 of the 1nput."
            ])

    def test_zero_digit_string(self):
            # Boundary/Off-by-one: string containing only '0' (which is even)
            self.assertEqual(mod.odd_count(['000']), ["the number of odd elements 0n the str0ng 0 of the 0nput."])
    
    if __name__ == '__main__':
        unittest.main()

    def test_normal_single_string_multiple_odd(self):
            """
            A single string with multiple odd digits.
            """
            lst = ['1234567']
            expected_output = ["the number of odd elements 4n the str4ng 4 of the 4nput."]
            self.assertEqual(mod.odd_count(lst), expected_output)

    def test_normal_multiple_strings_different_odd_counts(self):
            """
            Multiple strings, each with a different count of odd digits.
            """
            lst = ['3', '11111111']
            expected_output = ["the number of odd elements 1n the str1ng 1 of the 1nput.",
                               "the number of odd elements 8n the str8ng 8 of the 8nput."]
            self.assertEqual(mod.odd_count(lst), expected_output)

    def test_normal_mixed_even_and_odd_strings(self):
            """
            Strings with no odd digits and strings with all odd digits.
            """
            lst = ['02468', '13579']
            expected_output = ["the number of odd elements 0n the str0ng 0 of the 0nput.",
                               "the number of odd elements 5n the str5ng 5 of the 5nput."]
            self.assertEqual(mod.odd_count(lst), expected_output)
    
        # Edge Cases

    def test_edge_empty_list(self):
            """
            An empty input list.
            """
            lst = []
            expected_output = []
            self.assertEqual(mod.odd_count(lst), expected_output)

    def test_edge_list_with_empty_string(self):
            """
            A list containing a single empty string.
            """
            lst = ['']
            expected_output = ["the number of odd elements 0n the str0ng 0 of the 0nput."]
            self.assertEqual(mod.odd_count(lst), expected_output)

    def test_edge_single_digit_odd(self):
            """
            A list containing a single-digit odd number string.
            """
            lst = ['7']
            expected_output = ["the number of odd elements 1n the str1ng 1 of the 1nput."]
            self.assertEqual(mod.odd_count(lst), expected_output)

    def test_edge_single_digit_even(self):
            """
            A list containing a single-digit even number string.
            """
            lst = ['8']
            expected_output = ["the number of odd elements 0n the str0ng 0 of the 0nput."]
            self.assertEqual(mod.odd_count(lst), expected_output)
    
        # Error Cases

    def test_error_input_none(self):
            """
            Input is not a list (None).
            """
            with self.assertRaises(TypeError):
                mod.odd_count(None)

    def test_error_input_not_list_integer(self):
            """
            Input is an integer, not a list.
            """
            with self.assertRaises(TypeError):
                mod.odd_count(123)

    def test_error_list_contains_non_string_element(self):
            """
            List contains a non-string element.
            """
            with self.assertRaises(TypeError):
                mod.odd_count(['123', 456])

    def test_error_string_contains_non_digit_character(self):
            """
            A string in the list contains non-digit characters.
            """
            with self.assertRaises(ValueError):
                mod.odd_count(['12a34'])

    def test_error_string_contains_only_non_digit_characters(self):
            """
            A string in the list contains only non-digit characters.
            """
            with self.assertRaises(ValueError):
                mod.odd_count(['hello'])

