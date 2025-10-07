import unittest
from sut_llm.problem_HumanEval_141 import file_name_check

class TestFileNameCheck(unittest.TestCase):

    def test_valid_basic_txt(self):
        self.assertEqual(file_name_check("example.txt"), 'Yes')

    def test_valid_with_digits_and_dll(self):
        self.assertEqual(file_name_check("my_file12.dll"), 'Yes')

    def test_valid_max_three_digits_exe(self):
        self.assertEqual(file_name_check("doc123.exe"), 'Yes')

    def test_invalid_too_many_digits(self):
        self.assertEqual(file_name_check("report1234.txt"), 'No')

    def test_invalid_no_dot(self):
        self.assertEqual(file_name_check("documentname"), 'No')

    def test_invalid_multiple_dots(self):
        self.assertEqual(file_name_check("archive.data.zip"), 'No')

    def test_invalid_empty_prefix(self):
        self.assertEqual(file_name_check(".txt"), 'No')

    def test_invalid_prefix_starts_with_digit(self):
        self.assertEqual(file_name_check("1image.png"), 'No')

    def test_invalid_prefix_starts_with_symbol(self):
        self.assertEqual(file_name_check("_config.exe"), 'No')

    def test_invalid_extension(self):
        self.assertEqual(file_name_check("photo.jpg"), 'No')

if __name__ == '__main__':
    unittest.main()