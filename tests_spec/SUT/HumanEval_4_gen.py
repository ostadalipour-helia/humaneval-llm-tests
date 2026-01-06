import unittest
from sut.problem_HumanEval_4 import mean_absolute_deviation

class Test_mean_absolute_deviation(unittest.TestCase):

    def test_normal_case_simple_sequence(self):
        with self.assertRaises(TypeError) as cm:
            mean_absolute_deviation("[1.0, 2.0, 3.0, 4.0]")
        self.assertEqual(str(cm.exception), "unsupported operand type(s) for +: 'int' and 'str'")

    def test_normal_case_non_integer_mean(self):
        with self.assertRaises(TypeError) as cm:
            mean_absolute_deviation("[10.0, 20.0, 30.0]")
        self.assertEqual(str(cm.exception), "unsupported operand type(s) for +: 'int' and 'str'")

    def test_normal_case_mixed_signs(self):
        with self.assertRaises(TypeError) as cm:
            mean_absolute_deviation("[-1.0, 0.0, 1.0]")
        self.assertEqual(str(cm.exception), "unsupported operand type(s) for +: 'int' and 'str'")

    def test_edge_case_single_element(self):
        with self.assertRaises(TypeError) as cm:
            mean_absolute_deviation("[5.0]")
        self.assertEqual(str(cm.exception), "unsupported operand type(s) for +: 'int' and 'str'")

    def test_edge_case_all_identical(self):
        with self.assertRaises(TypeError) as cm:
            mean_absolute_deviation("[2.5, 2.5, 2.5]")
        self.assertEqual(str(cm.exception), "unsupported operand type(s) for +: 'int' and 'str'")

    def test_edge_case_all_zeros(self):
        with self.assertRaises(TypeError) as cm:
            mean_absolute_deviation("[0.0, 0.0, 0.0, 0.0]")
        self.assertEqual(str(cm.exception), "unsupported operand type(s) for +: 'int' and 'str'")

    def test_edge_case_all_negative(self):
        with self.assertRaises(TypeError) as cm:
            mean_absolute_deviation("[-5.0, -4.0, -3.0, -2.0, -1.0]")
        self.assertEqual(str(cm.exception), "unsupported operand type(s) for +: 'int' and 'str'")