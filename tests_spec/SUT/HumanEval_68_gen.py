import unittest
from sut.problem_HumanEval_68 import pluck
import ast

class Test_pluck(unittest.TestCase):

    def test_case_01(self):
        # This test case corresponds to the pre-calculated output for input "[4, 2, 3]"
        # The pre-calculated output indicates a TypeError, likely due to passing a string instead of a list.
        # The implementation's use of '%' on string characters causes this error.
        with self.assertRaises(TypeError) as cm:
            pluck("[4, 2, 3]")
        self.assertIsInstance(cm.exception, TypeError)

    def test_case_02(self):
        # This test case corresponds to the pre-calculated output for input "[1, 2, 3]"
        with self.assertRaises(TypeError) as cm:
            pluck("[1, 2, 3]")
        self.assertIsInstance(cm.exception, TypeError)

    def test_case_03(self):
        # This test case corresponds to the pre-calculated output for input "[5, 0, 3, 0, 4, 2]"
        with self.assertRaises(TypeError) as cm:
            pluck("[5, 0, 3, 0, 4, 2]")
        self.assertIsInstance(cm.exception, TypeError)

    def test_case_04(self):
        # This test case corresponds to the pre-calculated output for input "[10, 8, 6, 4, 2]"
        with self.assertRaises(TypeError) as cm:
            pluck("[10, 8, 6, 4, 2]")
        self.assertIsInstance(cm.exception, TypeError)

    def test_case_05(self):
        # This test case corresponds to the pre-calculated output for input "[2, 4, 6, 8, 10]"
        with self.assertRaises(TypeError) as cm:
            pluck("[2, 4, 6, 8, 10]")
        self.assertIsInstance(cm.exception, TypeError)

    def test_case_06(self):
        # This test case corresponds to the pre-calculated output for input "[]"
        # Note: len("[]") is 2, so the function proceeds and fails on the filter.
        with self.assertRaises(TypeError) as cm:
            pluck("[]")
        self.assertIsInstance(cm.exception, TypeError)

    def test_case_07(self):
        # This test case corresponds to the pre-calculated output for input "[1, 3, 5, 7]"
        with self.assertRaises(TypeError) as cm:
            pluck("[1, 3, 5, 7]")
        self.assertIsInstance(cm.exception, TypeError)

    def test_case_08(self):
        # This test case corresponds to the pre-calculated output for input "[0]"
        with self.assertRaises(TypeError) as cm:
            pluck("[0]")
        self.assertIsInstance(cm.exception, TypeError)

    def test_case_09(self):
        # This test case corresponds to the pre-calculated output for input "[7]"
        with self.assertRaises(TypeError) as cm:
            pluck("[7]")
        self.assertIsInstance(cm.exception, TypeError)

    def test_case_10(self):
        # This test case corresponds to the pre-calculated output for input "[0, 0, 0]"
        with self.assertRaises(TypeError) as cm:
            pluck("[0, 0, 0]")
        self.assertIsInstance(cm.exception, TypeError)