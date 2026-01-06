import unittest
from sut.problem_HumanEval_163 import generate_integers

class Test_generate_integers(unittest.TestCase):

    def test_case_0(self):
        with self.assertRaises(TypeError) as cm:
            generate_integers((2, 8))
        self.assertEqual(str(cm.exception), "generate_integers() missing 1 required positional argument: 'b'")

    def test_case_1(self):
        with self.assertRaises(TypeError) as cm:
            generate_integers((8, 2))
        self.assertEqual(str(cm.exception), "generate_integers() missing 1 required positional argument: 'b'")

    def test_case_2(self):
        with self.assertRaises(TypeError) as cm:
            generate_integers((1, 9))
        self.assertEqual(str(cm.exception), "generate_integers() missing 1 required positional argument: 'b'")

    def test_case_3(self):
        with self.assertRaises(TypeError) as cm:
            generate_integers((3, 7))
        self.assertEqual(str(cm.exception), "generate_integers() missing 1 required positional argument: 'b'")

    def test_case_4(self):
        with self.assertRaises(TypeError) as cm:
            generate_integers((2, 2))
        self.assertEqual(str(cm.exception), "generate_integers() missing 1 required positional argument: 'b'")

    def test_case_5(self):
        with self.assertRaises(TypeError) as cm:
            generate_integers((10, 14))
        self.assertEqual(str(cm.exception), "generate_integers() missing 1 required positional argument: 'b'")

    def test_case_6(self):
        with self.assertRaises(TypeError) as cm:
            generate_integers((1, 1))
        self.assertEqual(str(cm.exception), "generate_integers() missing 1 required positional argument: 'b'")

    def test_case_7(self):
        with self.assertRaises(TypeError) as cm:
            generate_integers((1, 2))
        self.assertEqual(str(cm.exception), "generate_integers() missing 1 required positional argument: 'b'")

    def test_case_8(self):
        with self.assertRaises(TypeError) as cm:
            generate_integers((9, 1))
        self.assertEqual(str(cm.exception), "generate_integers() missing 1 required positional argument: 'b'")

    def test_case_9(self):
        with self.assertRaises(TypeError) as cm:
            generate_integers((1, 100))
        self.assertEqual(str(cm.exception), "generate_integers() missing 1 required positional argument: 'b'")