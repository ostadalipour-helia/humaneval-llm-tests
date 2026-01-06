import unittest
from sut.problem_HumanEval_156 import int_to_mini_roman

class Test_int_to_mini_roman(unittest.TestCase):

    def test_normal_case_19(self):
        self.assertEqual(int_to_mini_roman(19), 'xix')

    def test_normal_case_152(self):
        self.assertEqual(int_to_mini_roman(152), 'clii')

    def test_normal_case_426(self):
        self.assertEqual(int_to_mini_roman(426), 'cdxxvi')

    def test_edge_case_min_input(self):
        self.assertEqual(int_to_mini_roman(1), 'i')

    def test_edge_case_max_input(self):
        self.assertEqual(int_to_mini_roman(1000), 'm')

    def test_edge_case_subtractive_4(self):
        self.assertEqual(int_to_mini_roman(4), 'iv')

    def test_edge_case_subtractive_9(self):
        self.assertEqual(int_to_mini_roman(9), 'ix')

    def test_edge_case_base_50(self):
        self.assertEqual(int_to_mini_roman(50), 'l')

    def test_edge_case_subtractive_99(self):
        self.assertEqual(int_to_mini_roman(99), 'xcix')

    def test_edge_case_base_500(self):
        self.assertEqual(int_to_mini_roman(500), 'd')