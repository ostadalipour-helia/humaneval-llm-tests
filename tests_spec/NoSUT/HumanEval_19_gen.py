import unittest
from sut.problem_HumanEval_19 import sort_numbers

class Test_sort_numbers(unittest.TestCase):

    def test_normal_unsorted_numbers(self):
        # Normal case: Typical case with multiple unsorted numbers.
        input_str = "three one five"
        expected_output = "one three five"
        self.assertEqual(sort_numbers(input_str), expected_output)

    def test_normal_already_sorted(self):
        # Normal case: Input is already sorted.
        input_str = "one two three"
        expected_output = "one two three"
        self.assertEqual(sort_numbers(input_str), expected_output)

    def test_normal_duplicate_numbers(self):
        # Normal case: Input with duplicate numbers.
        input_str = "seven four seven one"
        expected_output = "one four seven seven"
        self.assertEqual(sort_numbers(input_str), expected_output)

    def test_normal_all_numbers_reverse(self):
        # Normal case: All numbers in reverse order.
        input_str = "nine eight seven six five four three two one zero"
        expected_output = "zero one two three four five six seven eight nine"
        self.assertEqual(sort_numbers(input_str), expected_output)

    def test_edge_empty_string(self):
        # Edge case: Empty input string.
        input_str = ""
        expected_output = ""
        self.assertEqual(sort_numbers(input_str), expected_output)

    def test_edge_single_number(self):
        # Edge case: Single number in the input string.
        input_str = "five"
        expected_output = "five"
        self.assertEqual(sort_numbers(input_str), expected_output)

    def test_edge_all_identical_numbers(self):
        # Edge case: All numbers are identical.
        input_str = "two two two"
        expected_output = "two two two"
        self.assertEqual(sort_numbers(input_str), expected_output)

    def test_edge_extreme_numbers(self):
        # Edge case: Numbers at the extremes of the valid range.
        input_str = "zero nine"
        expected_output = "zero nine"
        self.assertEqual(sort_numbers(input_str), expected_output)

    def test_error_invalid_numeral_word(self):
        # Error case: Input string contains a word that is not a valid numeral ('ten').
        # Assuming ValueError for invalid numeral words.
        with self.assertRaises(ValueError):
            sort_numbers("one ten three")

    def test_error_incorrect_delimiter(self):
        # Error case: Input string uses an invalid delimiter (comma instead of space).
        # Assuming ValueError for incorrect delimiters.
        with self.assertRaises(ValueError):
            sort_numbers("one,two,three")

    def test_error_non_string_input_int(self):
        # Error case: Input is not a string (integer).
        with self.assertRaises(TypeError):
            sort_numbers(123)

    def test_error_non_string_input_null(self):
        # Error case: Input is null.
        with self.assertRaises(TypeError):
            sort_numbers(None)