import unittest
import sut.problem_HumanEval_141 as mod

class TestHybrid(unittest.TestCase):
    def test_valid_typical_case(self):
            # Test 1: Typical valid case, all conditions met.
            self.assertEqual(mod.file_name_check("example.txt"), 'Yes')

    def test_valid_max_three_digits(self):
            # Test 2: Boundary condition - exactly three digits, should be valid.
            self.assertEqual(mod.file_name_check("file123.exe"), 'Yes')

    def test_invalid_four_digits(self):
            # Test 3: Boundary condition - four digits, off-by-one from max valid, should be invalid.
            self.assertEqual(mod.file_name_check("file1234.dll"), 'No')

    def test_invalid_no_dot(self):
            # Test 4: Boundary condition - zero dots, should be invalid.
            self.assertEqual(mod.file_name_check("filename"), 'No')

    def test_invalid_two_dots(self):
            # Test 5: Boundary condition - two dots, should be invalid.
            self.assertEqual(mod.file_name_check("file.name.txt"), 'No')

    def test_invalid_empty_prefix(self):
            # Test 6: Edge case - empty string before the dot, should be invalid.
            self.assertEqual(mod.file_name_check(".txt"), 'No')

    def test_invalid_prefix_starts_with_digit(self):
            # Test 7: Logic mutation - prefix starts with a digit, should be invalid.
            self.assertEqual(mod.file_name_check("1example.dll"), 'No')

    def test_invalid_bad_extension(self):
            # Test 8: Logic mutation - invalid extension, should be invalid.
            self.assertEqual(mod.file_name_check("document.pdf"), 'No')

    def test_valid_long_name_with_digits(self):
            # Test 9: Extreme valid case - long file name with mixed case and digits.
            self.assertEqual(mod.file_name_check("My_Very_Long_Document_v123.txt"), 'Yes')

    def test_invalid_multiple_failures(self):
            # Test 10: Extreme invalid case - multiple conditions fail (digits, dots, extension, prefix start).
            self.assertEqual(mod.file_name_check("1234.bad.ext"), 'No')

    def test_normal_valid_txt(self):
            # Normal case: Valid name, one dot, starts with letter, valid extension, 0 digits.
            self.assertEqual(mod.file_name_check("example.txt"), "Yes")

    def test_normal_valid_dll_one_digit(self):
            # Normal case: Valid name, one dot, starts with letter, valid extension, 1 digit.
            self.assertEqual(mod.file_name_check("my_document_1.dll"), "Yes")

    def test_edge_starts_with_digit(self):
            # Edge case: The name should start with a latin alphabet letter (starts with a digit).
            self.assertEqual(mod.file_name_check("1example.dll"), "No")

    def test_edge_more_than_three_digits(self):
            # Edge case: Contains more than three digits.
            self.assertEqual(mod.file_name_check("file_name_with_4_digits_1234.txt"), "No")

    def test_edge_no_dot(self):
            # Edge case: Does not contain exactly one dot (contains zero dots).
            self.assertEqual(mod.file_name_check("no_dot_here"), "No")

    def test_edge_multiple_dots(self):
            # Edge case: Does not contain exactly one dot (contains multiple dots).
            self.assertEqual(mod.file_name_check("multiple.dots.txt"), "No")

    def test_edge_empty_before_dot(self):
            # Edge case: The substring before the dot is empty.
            self.assertEqual(mod.file_name_check(".txt"), "No")

    def test_edge_invalid_extension(self):
            # Edge case: The substring after the dot is not one of ['txt', 'exe', 'dll'].
            self.assertEqual(mod.file_name_check("file.jpg"), "No")

