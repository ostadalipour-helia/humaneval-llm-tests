import unittest
from sut.problem_HumanEval_141 import file_name_check

class Test_file_name_check(unittest.TestCase):

    def test_normal_valid_cases(self):
        self.assertEqual(file_name_check("example.txt"), 'Yes')
        self.assertEqual(file_name_check("my_document_1.dll"), 'Yes')
        self.assertEqual(file_name_check("A.txt"), 'Yes')
        self.assertEqual(file_name_check("file_name_with_no_digits.txt"), 'Yes')

    def test_invalid_start_character(self):
        self.assertEqual(file_name_check("1example.dll"), 'No')

    def test_too_many_digits(self):
        self.assertEqual(file_name_check("Report_2023_final.exe"), 'No')
        self.assertEqual(file_name_check("file_name_with_4_digits_1234.txt"), 'No')
        # Note: The name 'file_name_with_3_digits_123.txt' actually contains 4 digits (3, 1, 2, 3)
        self.assertEqual(file_name_check("file_name_with_3_digits_123.txt"), 'No')

    def test_no_dot(self):
        self.assertEqual(file_name_check("no_dot_here"), 'No')

    def test_multiple_dots(self):
        self.assertEqual(file_name_check("multiple.dots.txt"), 'No')

    def test_empty_name_part(self):
        self.assertEqual(file_name_check(".txt"), 'No')

    def test_empty_extension_part(self):
        self.assertEqual(file_name_check("file."), 'No')

    def test_invalid_extension(self):
        self.assertEqual(file_name_check("file.jpg"), 'No')

    def test_case_sensitive_extension(self):
        self.assertEqual(file_name_check("file.TXT"), 'No')

    def test_combined_invalid_cases(self):
        # A mix of various invalid cases to ensure robustness
        self.assertEqual(file_name_check("1.txt"), 'No')
        self.assertEqual(file_name_check("a.b.c.d"), 'No')
        self.assertEqual(file_name_check("a1234.exe"), 'No')
        self.assertEqual(file_name_check("a.jpeg"), 'No')