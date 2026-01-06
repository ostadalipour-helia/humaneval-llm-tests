import unittest
from sut.problem_HumanEval_114 import minSubArraySum

class Test_minSubArraySum(unittest.TestCase):

    def test_normal_case_1(self):
        with self.assertRaises(TypeError) as cm:
            minSubArraySum([2, 3, 4, 1, 2, 4])
        self.assertEqual(str(cm.exception), "bad operand type for unary -: 'str'")

    def test_normal_case_2(self):
        with self.assertRaises(TypeError) as cm:
            minSubArraySum([-1, -2, -3])
        self.assertEqual(str(cm.exception), "bad operand type for unary -: 'str'")

    def test_normal_case_3(self):
        with self.assertRaises(TypeError) as cm:
            minSubArraySum([1, -2, 3, -4, 5])
        self.assertEqual(str(cm.exception), "bad operand type for unary -: 'str'")

    def test_normal_case_4(self):
        with self.assertRaises(TypeError) as cm:
            minSubArraySum([10, -1, -2, 5, -3, 8])
        self.assertEqual(str(cm.exception), "bad operand type for unary -: 'str'")

    def test_normal_case_5(self):
        with self.assertRaises(TypeError) as cm:
            minSubArraySum([5, 4, 3, 2, 1])
        self.assertEqual(str(cm.exception), "bad operand type for unary -: 'str'")

    def test_edge_case_1(self):
        with self.assertRaises(TypeError) as cm:
            minSubArraySum([7])
        self.assertEqual(str(cm.exception), "bad operand type for unary -: 'str'")

    def test_edge_case_2(self):
        with self.assertRaises(TypeError) as cm:
            minSubArraySum([-5])
        self.assertEqual(str(cm.exception), "bad operand type for unary -: 'str'")

    def test_edge_case_3(self):
        with self.assertRaises(TypeError) as cm:
            minSubArraySum([0, 0, 0])
        self.assertEqual(str(cm.exception), "bad operand type for unary -: 'str'")

    def test_edge_case_4(self):
        with self.assertRaises(TypeError) as cm:
            minSubArraySum([100, -1, -2, -3, 200])
        self.assertEqual(str(cm.exception), "bad operand type for unary -: 'str'")

    def test_edge_case_5(self):
        with self.assertRaises(TypeError) as cm:
            minSubArraySum([-10, 5, -20, 1])
        self.assertEqual(str(cm.exception), "bad operand type for unary -: 'str'")