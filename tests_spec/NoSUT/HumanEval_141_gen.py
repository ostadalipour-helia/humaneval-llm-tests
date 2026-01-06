import unittest
from sut.problem_HumanEval_141 import file_name_check

class Test_file_name_check(unittest.TestCase):

    def test_normal_valid_txt(self):
        # Normal case: Valid name, one dot, starts with letter, valid extension, 0 digits.
        self.assertEqual(file_name_check("example.txt"), "Yes")

    def test_normal_valid_dll_one_digit(self):
        # Normal case: Valid name, one dot, starts with letter, valid extension, 1 digit.
        self.assertEqual(file_name_check("my_document_1.dll"), "Yes")

    def test_normal_valid_exe_three_digits(self):
        # Normal case: Valid name, one dot, starts with letter, valid extension, 3 digits.
        self.assertEqual(file_name_check("Report_2023_final.exe"), "Yes")

    def test_edge_starts_with_digit(self):
        # Edge case: The name should start with a latin alphabet letter (starts with a digit).
        self.assertEqual(file_name_check("1example.dll"), "No")

    def test_edge_more_than_three_digits(self):
        # Edge case: Contains more than three digits.
        self.assertEqual(file_name_check("file_name_with_4_digits_1234.txt"), "No")

    def test_edge_exactly_three_digits(self):
        # Edge case: Contains exactly three digits, which is allowed.
        self.assertEqual(file_name_check("file_name_with_3_digits_123.txt"), "Yes")

    def test_edge_no_dot(self):
        # Edge case: Does not contain exactly one dot (contains zero dots).
        self.assertEqual(file_name_check("no_dot_here"), "No")

    def test_edge_multiple_dots(self):
        # Edge case: Does not contain exactly one dot (contains multiple dots).
        self.assertEqual(file_name_check("multiple.dots.txt"), "No")

    def test_edge_empty_before_dot(self):
        # Edge case: The substring before the dot is empty.
        self.assertEqual(file_name_check(".txt"), "No")

    def test_edge_invalid_extension(self):
        # Edge case: The substring after the dot is not one of ['txt', 'exe', 'dll'].
        self.assertEqual(file_name_check("file.jpg"), "No")

    def test_error_input_is_none(self):
        # Error case: Input `file_name` is not a string (None).
        with self.assertRaises(TypeError):
            file_name_check(None)

    def test_error_input_is_int(self):
        # Error case: Input `file_name` is not a string (integer).
        with self.assertRaises(TypeError):
            file_name_check(123)