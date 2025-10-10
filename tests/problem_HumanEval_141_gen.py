import unittest
from sut.problem_HumanEval_141 import file_name_check

class TestFileNameCheck(unittest.TestCase):

    def test_valid_typical_case(self):
        # Test 1: Typical valid case, all conditions met.
        self.assertEqual(file_name_check("example.txt"), 'Yes')

    def test_valid_max_three_digits(self):
        # Test 2: Boundary condition - exactly three digits, should be valid.
        self.assertEqual(file_name_check("file123.exe"), 'Yes')

    def test_invalid_four_digits(self):
        # Test 3: Boundary condition - four digits, off-by-one from max valid, should be invalid.
        self.assertEqual(file_name_check("file1234.dll"), 'No')

    def test_invalid_no_dot(self):
        # Test 4: Boundary condition - zero dots, should be invalid.
        self.assertEqual(file_name_check("filename"), 'No')

    def test_invalid_two_dots(self):
        # Test 5: Boundary condition - two dots, should be invalid.
        self.assertEqual(file_name_check("file.name.txt"), 'No')

    def test_invalid_empty_prefix(self):
        # Test 6: Edge case - empty string before the dot, should be invalid.
        self.assertEqual(file_name_check(".txt"), 'No')

    def test_invalid_prefix_starts_with_digit(self):
        # Test 7: Logic mutation - prefix starts with a digit, should be invalid.
        self.assertEqual(file_name_check("1example.dll"), 'No')

    def test_invalid_bad_extension(self):
        # Test 8: Logic mutation - invalid extension, should be invalid.
        self.assertEqual(file_name_check("document.pdf"), 'No')

    def test_valid_long_name_with_digits(self):
        # Test 9: Extreme valid case - long file name with mixed case and digits.
        self.assertEqual(file_name_check("My_Very_Long_Document_v123.txt"), 'Yes')

    def test_invalid_multiple_failures(self):
        # Test 10: Extreme invalid case - multiple conditions fail (digits, dots, extension, prefix start).
        self.assertEqual(file_name_check("1234.bad.ext"), 'No')