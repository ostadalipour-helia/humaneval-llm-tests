import unittest
from sut_llm.problem_HumanEval_161 import solve

class TestSolve(unittest.TestCase):

    def test_1_all_lowercase_letters(self):
        self.assertEqual(solve("hello"), "HELLO")

    def test_2_all_uppercase_letters(self):
        self.assertEqual(solve("WORLD"), "world")

    def test_3_mixed_case_letters(self):
        self.assertEqual(solve("PyThOn"), "pYtHoN")

    def test_4_mixed_letters_and_digits(self):
        self.assertEqual(solve("a1B2c3"), "A1b2C3")

    def test_5_mixed_letters_and_symbols(self):
        self.assertEqual(solve("!@a#B$c%"), "!@A#b$C%")

    def test_6_string_with_only_digits(self):
        self.assertEqual(solve("12345"), "54321")


    def test_8_string_with_mixed_digits_and_symbols(self):
        self.assertEqual(solve("1!2@3#"), "#3@2!1")

    def test_9_empty_string(self):
        self.assertEqual(solve(""), "")

    def test_10_string_with_spaces_and_letters(self):
        self.assertEqual(solve("Hello World"), "hELLO wORLD")

if __name__ == '__main__':
    unittest.main()