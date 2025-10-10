import unittest
from sut.problem_HumanEval_156 import int_to_mini_roman

class TestIntToMiniRoman(unittest.TestCase):

    def test_minimum_value(self):
        self.assertEqual(int_to_mini_roman(1), 'i')

    def test_small_subtraction(self):
        self.assertEqual(int_to_mini_roman(4), 'iv')

    def test_another_small_subtraction(self):
        self.assertEqual(int_to_mini_roman(9), 'ix')

    def test_docstring_example_1(self):
        self.assertEqual(int_to_mini_roman(19), 'xix')

    def test_tens_and_units(self):
        self.assertEqual(int_to_mini_roman(42), 'xlii')

    def test_complex_subtraction_and_combination(self):
        self.assertEqual(int_to_mini_roman(99), 'xcix')

    def test_docstring_example_2(self):
        self.assertEqual(int_to_mini_roman(152), 'clii')

    def test_docstring_example_3(self):
        self.assertEqual(int_to_mini_roman(426), 'cdxxvi')

    def test_hundreds_and_tens(self):
        self.assertEqual(int_to_mini_roman(583), 'dlxxxiii')

    def test_maximum_value(self):
        self.assertEqual(int_to_mini_roman(1000), 'm')

if __name__ == '__main__':
    unittest.main()