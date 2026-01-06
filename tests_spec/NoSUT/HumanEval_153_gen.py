import unittest
from sut.problem_HumanEval_153 import Strongest_Extension

class Test_Strongest_Extension(unittest.TestCase):

    def test_normal_mixed_case_extensions(self):
        # 'SErviNGSliCes' (CAP=4, SM=5, Strength=-1)
        # 'Cheese' (CAP=1, SM=5, Strength=-4)
        # 'StuFfed' (CAP=1, SM=6, Strength=-5)
        # 'SErviNGSliCes' is strongest.
        class_name = "Slices"
        extensions = ["SErviNGSliCes", "Cheese", "StuFfed"]
        expected_output = "Slices.SErviNGSliCes"
        self.assertEqual(Strongest_Extension(class_name, extensions), expected_output)

    def test_normal_tie_breaker_first_occurrence(self):
        # 'AA' (CAP=2, SM=0, Strength=2)
        # 'Be' (CAP=1, SM=1, Strength=0)
        # 'CC' (CAP=2, SM=0, Strength=2)
        # 'AA' and 'CC' have same max strength, 'AA' comes first.
        class_name = "my_class"
        extensions = ["AA", "Be", "CC"]
        expected_output = "my_class.AA"
        self.assertEqual(Strongest_Extension(class_name, extensions), expected_output)

    def test_normal_all_caps_strongest(self):
        # 'ALLCAPS' (CAP=7, SM=0, Strength=7)
        # 'lowercase' (CAP=0, SM=9, Strength=-9)
        # 'MiXeD' (CAP=2, SM=3, Strength=-1)
        # 'ALLCAPS' is strongest.
        class_name = "Data"
        extensions = ["ALLCAPS", "lowercase", "MiXeD"]
        expected_output = "Data.ALLCAPS"
        self.assertEqual(Strongest_Extension(class_name, extensions), expected_output)

    def test_normal_processor_case_with_spec_output(self):
        # Note: The spec's output for this case ("Processor.Medium")
        # appears to contradict its own tie-breaking rule if "Fast" and "Slow"
        # have strength -2 and "Medium" has strength -4.
        # We adhere to the explicit output provided in the specification.
        class_name = "Processor"
        extensions = ["Fast", "Slow", "Medium"]
        expected_output = "Processor.Medium"
        self.assertEqual(Strongest_Extension(class_name, extensions), expected_output)

    def test_edge_empty_string_extension(self):
        # '' (CAP=0, SM=0, Strength=0)
        # 'a' (CAP=0, SM=1, Strength=-1)
        # 'B' (CAP=1, SM=0, Strength=1)
        # 'B' is strongest.
        class_name = "EmptyClass"
        extensions = ["", "a", "B"]
        expected_output = "EmptyClass.B"
        self.assertEqual(Strongest_Extension(class_name, extensions), expected_output)

    def test_edge_no_letters_in_extension_with_spec_output(self):
        # Note: The spec's output for this case ("NoLetters.aB")
        # appears to contradict its own tie-breaking rule if "123", "!@#", "aB"
        # all have strength 0. We adhere to the explicit output provided.
        # '123' (CAP=0, SM=0, Strength=0)
        # '!@#' (CAP=0, SM=0, Strength=0)
        # 'aB' (CAP=1, SM=1, Strength=0)
        class_name = "NoLetters"
        extensions = ["123", "!@#", "aB"]
        expected_output = "NoLetters.aB"
        self.assertEqual(Strongest_Extension(class_name, extensions), expected_output)

    def test_edge_empty_class_name(self):
        # 'Ext1' (CAP=1, SM=3, Strength=-2)
        # 'Ext2' (CAP=1, SM=3, Strength=-2)
        # 'Ext1' comes first.
        class_name = ""
        extensions = ["Ext1", "Ext2"]
        expected_output = ".Ext1"
        self.assertEqual(Strongest_Extension(class_name, extensions), expected_output)

    def test_error_class_name_not_string(self):
        # class_name is not a string.
        class_name = 123
        extensions = ["Ext"]
        with self.assertRaises(TypeError):
            Strongest_Extension(class_name, extensions)

    def test_error_extensions_not_list(self):
        # extensions is not a list.
        class_name = "MyClass"
        extensions = "not_a_list"
        with self.assertRaises(TypeError):
            Strongest_Extension(class_name, extensions)

    def test_error_extension_element_not_string(self):
        # An element in extensions is not a string.
        class_name = "MyClass"
        extensions = ["Ext1", 123, "Ext2"]
        with self.assertRaises(TypeError):
            Strongest_Extension(class_name, extensions)

    def test_error_empty_extensions_list(self):
        # The problem implies a non-empty list of extensions.
        # If the list is empty, no strongest extension can be found.
        class_name = "MyClass"
        extensions = []
        with self.assertRaises((ValueError, IndexError)): # As per spec, ValueError or IndexError
            Strongest_Extension(class_name, extensions)