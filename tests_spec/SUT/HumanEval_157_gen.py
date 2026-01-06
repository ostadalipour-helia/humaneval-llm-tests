import unittest
from sut.problem_HumanEval_157 import right_angle_triangle

class Test_right_angle_triangle(unittest.TestCase):

    def test_case_1(self):
        with self.assertRaises(TypeError) as cm:
            right_angle_triangle((3, 4, 5))
        self.assertEqual(str(cm.exception), "right_angle_triangle() missing 2 required positional arguments: 'b' and 'c'")

    def test_case_2(self):
        with self.assertRaises(TypeError) as cm:
            right_angle_triangle((5, 12, 13))
        self.assertEqual(str(cm.exception), "right_angle_triangle() missing 2 required positional arguments: 'b' and 'c'")

    def test_case_3(self):
        with self.assertRaises(TypeError) as cm:
            right_angle_triangle((1, 2, 3))
        self.assertEqual(str(cm.exception), "right_angle_triangle() missing 2 required positional arguments: 'b' and 'c'")

    def test_case_4(self):
        with self.assertRaises(TypeError) as cm:
            right_angle_triangle((2, 3, 4))
        self.assertEqual(str(cm.exception), "right_angle_triangle() missing 2 required positional arguments: 'b' and 'c'")

    def test_case_5(self):
        with self.assertRaises(TypeError) as cm:
            right_angle_triangle((0.6, 0.8, 1.0))
        self.assertEqual(str(cm.exception), "right_angle_triangle() missing 2 required positional arguments: 'b' and 'c'")

    def test_case_6(self):
        with self.assertRaises(TypeError) as cm:
            right_angle_triangle((7, 24, 25))
        self.assertEqual(str(cm.exception), "right_angle_triangle() missing 2 required positional arguments: 'b' and 'c'")

    def test_case_7(self):
        with self.assertRaises(TypeError) as cm:
            right_angle_triangle((3.000000000000001, 4, 5))
        self.assertEqual(str(cm.exception), "right_angle_triangle() missing 2 required positional arguments: 'b' and 'c'")

    def test_case_8(self):
        with self.assertRaises(TypeError) as cm:
            right_angle_triangle((4, 3, 5))
        self.assertEqual(str(cm.exception), "right_angle_triangle() missing 2 required positional arguments: 'b' and 'c'")

    def test_case_9(self):
        with self.assertRaises(TypeError) as cm:
            right_angle_triangle((3, 4, 5))
        self.assertEqual(str(cm.exception), "right_angle_triangle() missing 2 required positional arguments: 'b' and 'c'")

    def test_case_10(self):
        with self.assertRaises(TypeError) as cm:
            right_angle_triangle((5, 12, 13))
        self.assertEqual(str(cm.exception), "right_angle_triangle() missing 2 required positional arguments: 'b' and 'c'")