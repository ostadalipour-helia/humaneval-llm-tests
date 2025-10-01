import unittest
from sut.problem_HumanEval_153 import Strongest_Extension

class TestStrongestExtension(unittest.TestCase):

    def test_example_from_docstring_1(self):
        # Test case directly from the docstring example
        class_name = 'my_class'
        extensions = ['AA', 'Be', 'CC']
        expected_output = 'my_class.AA'
        self.assertEqual(Strongest_Extension(class_name, extensions), expected_output)

    def test_example_from_docstring_2(self):
        # Another test case directly from the docstring example
        class_name = 'Slices'
        extensions = ['SErviNGSliCes', 'Cheese', 'StuFfed']
        expected_output = 'Slices.SErviNGSliCes'
        self.assertEqual(Strongest_Extension(class_name, extensions), expected_output)

    def test_clear_strongest_all_uppercase(self):
        # Test with extensions primarily having uppercase letters, clear strongest
        class_name = 'App'
        extensions = ['ABC', 'DEf', 'GHIj']
        expected_output = 'App.ABC' # ABC: CAP=3, SM=0, Str=3; DEf: CAP=2, SM=1, Str=1; GHIj: CAP=3, SM=1, Str=2
        self.assertEqual(Strongest_Extension(class_name, extensions), expected_output)

    def test_clear_strongest_all_lowercase(self):
        # Test with extensions primarily having lowercase letters, clear strongest
        class_name = 'Module'
        extensions = ['abc', 'defG', 'hijkL']
        expected_output = 'Module.defG' # abc: CAP=0, SM=3, Str=-3; defG: CAP=1, SM=3, Str=-2; hijkL: CAP=1, SM=4, Str=-3
        self.assertEqual(Strongest_Extension(class_name, extensions), expected_output)

    def test_tie_breaking_first_occurrence(self):
        # Test tie-breaking rule: choose the one that comes first in the list
        class_name = 'Component'
        extensions = ['aBc', 'XyZ', 'AbC']
        expected_output = 'Component.aBc' # All have CAP=2, SM=1, Str=1. 'aBc' is first.
        self.assertEqual(Strongest_Extension(class_name, extensions), expected_output)

    def test_single_extension(self):
        # Test with only one extension in the list
        class_name = 'Solo'
        extensions = ['OnlyOne']
        expected_output = 'Solo.OnlyOne' # OnlyOne: CAP=2, SM=5, Str=-3
        self.assertEqual(Strongest_Extension(class_name, extensions), expected_output)

    def test_extensions_with_non_alphabetic_chars(self):
        # Test that non-alphabetic characters are ignored in strength calculation
        class_name = 'Data'
        extensions = ['Ext123', 'Ext_A', 'Ext-b']
        expected_output = 'Data.Ext_A' # Ext123: CAP=1, SM=2, Str=-1; Ext_A: CAP=2, SM=2, Str=0; Ext-b: CAP=1, SM=2, Str=-1
        self.assertEqual(Strongest_Extension(class_name, extensions), expected_output)

    def test_all_negative_strengths(self):
        # Test where all extensions result in negative strengths
        class_name = 'Negative'
        extensions = ['aa', 'bbb', 'c']
        expected_output = 'Negative.c' # aa: Str=-2; bbb: Str=-3; c: Str=-1. 'c' is strongest (least negative).
        self.assertEqual(Strongest_Extension(class_name, extensions), expected_output)

    def test_all_positive_strengths(self):
        # Test where all extensions result in positive strengths
        class_name = 'Positive'
        extensions = ['AA', 'BBB', 'C']
        expected_output = 'Positive.BBB' # AA: Str=2; BBB: Str=3; C: Str=1. 'BBB' is strongest.
        self.assertEqual(Strongest_Extension(class_name, extensions), expected_output)

    def test_mixed_strengths_including_zero(self):
        # Test with a mix of positive, negative, and zero strengths
        class_name = 'Mixed'
        extensions = ['aB', 'CdE', 'fGhi', 'JkLmN']
        expected_output = 'Mixed.CdE' # aB: Str=0; CdE: Str=1; fGhi: Str=-2; JkLmN: Str=-1. 'CdE' is strongest.
        self.assertEqual(Strongest_Extension(class_name, extensions), expected_output)

if __name__ == '__main__':
    unittest.main()