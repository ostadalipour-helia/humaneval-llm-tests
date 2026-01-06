import unittest
from sut.problem_HumanEval_92 import any_int

class Test_any_int(unittest.TestCase):

    def test_case_1(self):
        with self.assertRaises(TypeError) as cm:
            any_int(5, 2, 7)
        self.assertEqual(str(cm.exception), "any_int() missing 2 required positional arguments: 'y' and 'z'")

    def test_case_2(self):
        with self.assertRaises(TypeError) as cm:
            any_int(3, -2, 1)
        self.assertEqual(str(cm.exception), "any_int() missing 2 required positional arguments: 'y' and 'z'")

    def test_case_3(self):
        with self.assertRaises(TypeError) as cm:
            any_int(10, 5, 5)
        self.assertEqual(str(cm.exception), "any_int() missing 2 required positional arguments: 'y' and 'z'")

    def test_case_4(self):
        with self.assertRaises(TypeError) as cm:
            any_int(3, 2, 2)
        self.assertEqual(str(cm.exception), "any_int() missing 2 required positional arguments: 'y' and 'z'")

    def test_case_5(self):
        with self.assertRaises(TypeError) as cm:
            any_int(1, 2, 4)
        self.assertEqual(str(cm.exception), "any_int() missing 2 required positional arguments: 'y' and 'z'")

    def test_case_6(self):
        with self.assertRaises(TypeError) as cm:
            any_int(0, 0, 0)
        self.assertEqual(str(cm.exception), "any_int() missing 2 required positional arguments: 'y' and 'z'")

    def test_case_7(self):
        with self.assertRaises(TypeError) as cm:
            any_int(0, 5, 5)
        self.assertEqual(str(cm.exception), "any_int() missing 2 required positional arguments: 'y' and 'z'")

    def test_case_8(self):
        with self.assertRaises(TypeError) as cm:
            any_int(-5, -2, -7)
        self.assertEqual(str(cm.exception), "any_int() missing 2 required positional arguments: 'y' and 'z'")

    def test_case_9(self):
        with self.assertRaises(TypeError) as cm:
            any_int(3.6, -2.2, 2)
        self.assertEqual(str(cm.exception), "any_int() missing 2 required positional arguments: 'y' and 'z'")

    def test_case_10(self):
        with self.assertRaises(TypeError) as cm:
            any_int(3.0, 2, 5)
        self.assertEqual(str(cm.exception), "any_int() missing 2 required positional arguments: 'y' and 'z'")