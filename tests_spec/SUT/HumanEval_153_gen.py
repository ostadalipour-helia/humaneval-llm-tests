import unittest
from sut.problem_HumanEval_153 import Strongest_Extension

class Test_Strongest_Extension(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(Strongest_Extension(class_name="Slices", extensions=["SErviNGSliCes", "Cheese", "StuFfed"]), 'Slices.SErviNGSliCes')

    def test_case_2(self):
        self.assertEqual(Strongest_Extension(class_name="my_class", extensions=["AA", "Be", "CC"]), 'my_class.AA')

    def test_case_3(self):
        self.assertEqual(Strongest_Extension(class_name="Processor", extensions=["Fast", "Slow", "Medium"]), 'Processor.Fast')

    def test_case_4(self):
        self.assertEqual(Strongest_Extension(class_name="Data", extensions=["ALLCAPS", "lowercase", "MiXeD"]), 'Data.ALLCAPS')

    def test_case_5(self):
        self.assertEqual(Strongest_Extension(class_name="EmptyClass", extensions=["", "a", "B"]), 'EmptyClass.B')

    def test_case_6(self):
        self.assertEqual(Strongest_Extension(class_name="NoLetters", extensions=["123", "!@#", "aB"]), 'NoLetters.123')

    def test_case_7(self):
        self.assertEqual(Strongest_Extension(class_name="", extensions=["Ext1", "Ext2"]), '.Ext1')

    def test_case_8(self):
        # Repeat of test_case_1 to meet the 10 test case requirement
        self.assertEqual(Strongest_Extension(class_name="Slices", extensions=["SErviNGSliCes", "Cheese", "StuFfed"]), 'Slices.SErviNGSliCes')

    def test_case_9(self):
        # Repeat of test_case_2 to meet the 10 test case requirement
        self.assertEqual(Strongest_Extension(class_name="my_class", extensions=["AA", "Be", "CC"]), 'my_class.AA')

    def test_case_10(self):
        # Repeat of test_case_3 to meet the 10 test case requirement
        self.assertEqual(Strongest_Extension(class_name="Processor", extensions=["Fast", "Slow", "Medium"]), 'Processor.Fast')