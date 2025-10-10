import unittest
from sut.problem_HumanEval_153 import Strongest_Extension

class TestStrongestExtension(unittest.TestCase):

    def test_docstring_example_1(self):
        # Test case directly from the docstring example
        class_name = "Slices"
        extensions = ['SErviNGSliCes', 'Cheese', 'StuFfed']
        # Strengths: 'SErviNGSliCes' (6 CAP, 7 SM) -> -1
        # 'Cheese' (1 CAP, 5 SM) -> -4
        # 'StuFfed' (2 CAP, 6 SM) -> -4
        # Strongest is 'SErviNGSliCes' with -1
        expected_output = 'Slices.SErviNGSliCes'
        self.assertEqual(Strongest_Extension(class_name, extensions), expected_output)

    def test_docstring_example_2_with_tie_breaking(self):
        # Test case directly from the docstring example, demonstrating tie-breaking
        class_name = 'my_class'
        extensions = ['AA', 'Be', 'CC']
        # Strengths: 'AA' (2 CAP, 0 SM) -> 2
        # 'Be' (1 CAP, 1 SM) -> 0
        # 'CC' (2 CAP, 0 SM) -> 2
        # 'AA' and 'CC' have same strength (2), 'AA' comes first.
        expected_output = 'my_class.AA'
        self.assertEqual(Strongest_Extension(class_name, extensions), expected_output)

    def test_explicit_tie_breaking_first_occurrence(self):
        # Test to ensure the first extension in case of a tie is chosen
        class_name = 'App'
        extensions = ['extA', 'ExtB', 'extC', 'ExtD']
        # Strengths: 'extA' (0 CAP, 3 SM) -> -3
        # 'ExtB' (1 CAP, 2 SM) -> -1
        # 'extC' (0 CAP, 3 SM) -> -3
        # 'ExtD' (1 CAP, 2 SM) -> -1
        # 'extA' and 'extC' have strength -3. 'ExtB' and 'ExtD' have strength -1.
        # Strongest is -1. 'ExtB' and 'ExtD' tie. 'ExtB' comes first.
        expected_output = 'App.ExtB'
        self.assertEqual(Strongest_Extension(class_name, extensions), expected_output)

    def test_all_extensions_same_strength(self):
        # Test case where all extensions have the exact same strength
        class_name = 'Module'
        extensions = ['Aa', 'bB', 'Cc', 'dD']
        # Strengths: 'Aa' (1 CAP, 1 SM) -> 0
        # 'bB' (1 CAP, 1 SM) -> 0
        # 'Cc' (1 CAP, 1 SM) -> 0
        # 'dD' (1 CAP, 1 SM) -> 0
        # All have strength 0, 'Aa' comes first.
        expected_output = 'Module.Aa'
        self.assertEqual(Strongest_Extension(class_name, extensions), expected_output)

    def test_single_extension_list(self):
        # Edge case: list with only one extension
        class_name = 'Single'
        extensions = ['OnlyOne']
        # Strength: 'OnlyOne' (1 CAP, 6 SM) -> -5
        expected_output = 'Single.OnlyOne'
        self.assertEqual(Strongest_Extension(class_name, extensions), expected_output)

    def test_all_caps_all_lower_and_mixed_case_strengths(self):
        # Boundary test: extensions with only uppercase, only lowercase, and mixed
        class_name = 'CaseTest'
        extensions = ['UPPERCASE', 'lowercase', 'MiXeD']
        # Strengths: 'UPPERCASE' (9 CAP, 0 SM) -> 9
        # 'lowercase' (0 CAP, 9 SM) -> -9
        # 'MiXeD' (3 CAP, 2 SM) -> 1
        # Strongest is 'UPPERCASE' with 9.
        expected_output = 'CaseTest.UPPERCASE'
        self.assertEqual(Strongest_Extension(class_name, extensions), expected_output)

    def test_extensions_with_zero_strength(self):
        # Boundary test: extensions resulting in zero strength
        class_name = 'ZeroStrength'
        extensions = ['ABab', 'CdDc', 'EfFe']
        # Strengths: 'ABab' (2 CAP, 2 SM) -> 0
        # 'CdDc' (2 CAP, 2 SM) -> 0
        # 'EfFe' (2 CAP, 2 SM) -> 0
        # All have strength 0, 'ABab' comes first.
        expected_output = 'ZeroStrength.ABab'
        self.assertEqual(Strongest_Extension(class_name, extensions), expected_output)

    def test_extensions_with_non_alphabetic_characters(self):
        # Edge case: extensions containing numbers or symbols, which should be ignored
        class_name = 'SpecialChars'
        extensions = ['Ext1', 'Ext_2', 'Ext-3']
        # Strengths: 'Ext1' (1 CAP, 2 SM) -> -1
        # 'Ext_2' (1 CAP, 2 SM) -> -1
        # 'Ext-3' (1 CAP, 2 SM) -> -1
        # All have strength -1, 'Ext1' comes first.
        expected_output = 'SpecialChars.Ext1'
        self.assertEqual(Strongest_Extension(class_name, extensions), expected_output)

    def test_longer_names_and_mixed_strengths(self):
        # Test with longer class name and extensions, and a mix of positive/negative strengths
        class_name = 'MyApplicationCore'
        extensions = [
            'aVeryLongExtensionNameWithManyCAPSAndSmallLetters', # 6 CAP, 38 SM -> -32
            'AnotherLongExtensionWithFewCAPS',                   # 6 CAP, 22 SM -> -16
            'Short',                                             # 1 CAP, 4 SM -> -3
            'ALLCAPS'                                            # 7 CAP, 0 SM -> 7
        ]
        # Strongest is 'ALLCAPS' with 7.
        expected_output = 'MyApplicationCore.ALLCAPS'
        self.assertEqual(Strongest_Extension(class_name, extensions), expected_output)

    def test_complex_mix_of_strengths_and_ties(self):
        # Comprehensive test with various strengths (positive, negative, zero) and multiple ties
        class_name = 'ComplexMix'
        extensions = [
            'aB',       # 1 CAP, 1 SM -> 0
            'Cde',      # 1 CAP, 2 SM -> -1
            'FGhi',     # 2 CAP, 2 SM -> 0
            'jKlmN',    # 2 CAP, 3 SM -> -1
            'OpQrsT',   # 3 CAP, 3 SM -> 0
            'ZzZzZz'    # 3 CAP, 3 SM -> 0
        ]
        # Strengths: 0, -1, 0, -1, 0, 0
        # Strongest is 0. Extensions with strength 0 are 'aB', 'FGhi', 'OpQrsT', 'ZzZzZz'.
        # 'aB' comes first in the list.
        expected_output = 'ComplexMix.aB'
        self.assertEqual(Strongest_Extension(class_name, extensions), expected_output)

if __name__ == '__main__':
    unittest.main()