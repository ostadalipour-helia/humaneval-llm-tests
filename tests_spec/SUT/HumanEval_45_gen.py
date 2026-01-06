import unittest
from sut.problem_HumanEval_45 import triangle_area

class Test_triangle_area(unittest.TestCase):

    def test_case_0(self):
        with self.assertRaises(TypeError) as cm:
            triangle_area(a=5)
        self.assertEqual(str(cm.exception), "triangle_area() missing 1 required positional argument: 'h'")

    def test_case_1(self):
        with self.assertRaises(TypeError) as cm:
            triangle_area(a=10.0)
        self.assertEqual(str(cm.exception), "triangle_area() missing 1 required positional argument: 'h'")

    def test_case_2(self):
        with self.assertRaises(TypeError) as cm:
            triangle_area(a=7)
        self.assertEqual(str(cm.exception), "triangle_area() missing 1 required positional argument: 'h'")

    def test_case_3(self):
        with self.assertRaises(TypeError) as cm:
            triangle_area(a=1)
        self.assertEqual(str(cm.exception), "triangle_area() missing 1 required positional argument: 'h'")

    def test_case_4(self):
        with self.assertRaises(TypeError) as cm:
            triangle_area(a=0.1)
        self.assertEqual(str(cm.exception), "triangle_area() missing 1 required positional argument: 'h'")

    def test_case_5(self):
        with self.assertRaises(TypeError) as cm:
            triangle_area(a=1000000)
        self.assertEqual(str(cm.exception), "triangle_area() missing 1 required positional argument: 'h'")

    def test_case_6(self):
        with self.assertRaises(TypeError) as cm:
            triangle_area(a=5)
        self.assertEqual(str(cm.exception), "triangle_area() missing 1 required positional argument: 'h'")

    def test_case_7(self):
        with self.assertRaises(TypeError) as cm:
            triangle_area(a=10.0)
        self.assertEqual(str(cm.exception), "triangle_area() missing 1 required positional argument: 'h'")

    def test_case_8(self):
        with self.assertRaises(TypeError) as cm:
            triangle_area(a=7)
        self.assertEqual(str(cm.exception), "triangle_area() missing 1 required positional argument: 'h'")

    def test_case_9(self):
        with self.assertRaises(TypeError) as cm:
            triangle_area(a=1)
        self.assertEqual(str(cm.exception), "triangle_area() missing 1 required positional argument: 'h'")