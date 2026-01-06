import unittest
from sut.problem_HumanEval_145 import order_by_points

class Test_order_by_points(unittest.TestCase):

    def test_case_0(self):
        nums = [1, 11, -1, -11, -12]
        with self.assertRaises(TypeError) as cm:
            order_by_points(nums)
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_1(self):
        nums = [10, 20, 30]
        with self.assertRaises(TypeError) as cm:
            order_by_points(nums)
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_2(self):
        nums = [12, 21, 3, 100]
        with self.assertRaises(TypeError) as cm:
            order_by_points(nums)
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_3(self):
        nums = [5, 15, 25]
        with self.assertRaises(TypeError) as cm:
            order_by_points(nums)
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_4(self):
        nums = []
        with self.assertRaises(TypeError) as cm:
            order_by_points(nums)
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_5(self):
        nums = [7]
        with self.assertRaises(TypeError) as cm:
            order_by_points(nums)
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_6(self):
        nums = [1, 10, 100]
        with self.assertRaises(TypeError) as cm:
            order_by_points(nums)
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_7(self):
        nums = [1, 11, 1, -11]
        with self.assertRaises(TypeError) as cm:
            order_by_points(nums)
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_8(self):
        nums = [0, 10, -1]
        with self.assertRaises(TypeError) as cm:
            order_by_points(nums)
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_9(self):
        nums = [-9, -18, -27]
        with self.assertRaises(TypeError) as cm:
            order_by_points(nums)
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")