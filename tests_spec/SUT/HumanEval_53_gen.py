import unittest
from sut.problem_HumanEval_53 import add

class Test_add(unittest.TestCase):

    def test_case_0(self):
        with self.assertRaises(TypeError) as cm:
            add(2)
        self.assertEqual(str(cm.exception), "add() missing 1 required positional argument: 'y'")

    def test_case_1(self):
        with self.assertRaises(TypeError) as cm:
            add(5)
        self.assertEqual(str(cm.exception), "add() missing 1 required positional argument: 'y'")

    def test_case_2(self):
        with self.assertRaises(TypeError) as cm:
            add(10)
        self.assertEqual(str(cm.exception), "add() missing 1 required positional argument: 'y'")

    def test_case_3(self):
        with self.assertRaises(TypeError) as cm:
            add(0)
        self.assertEqual(str(cm.exception), "add() missing 1 required positional argument: 'y'")

    def test_case_4(self):
        with self.assertRaises(TypeError) as cm:
            add(0)
        self.assertEqual(str(cm.exception), "add() missing 1 required positional argument: 'y'")

    def test_case_5(self):
        with self.assertRaises(TypeError) as cm:
            add(-2)
        self.assertEqual(str(cm.exception), "add() missing 1 required positional argument: 'y'")

    def test_case_6(self):
        with self.assertRaises(TypeError) as cm:
            add(2)
        self.assertEqual(str(cm.exception), "add() missing 1 required positional argument: 'y'")

    def test_case_7(self):
        with self.assertRaises(TypeError) as cm:
            add(-5)
        self.assertEqual(str(cm.exception), "add() missing 1 required positional argument: 'y'")

    def test_case_8(self):
        with self.assertRaises(TypeError) as cm:
            add(5)
        self.assertEqual(str(cm.exception), "add() missing 1 required positional argument: 'y'")

    def test_case_9(self):
        with self.assertRaises(TypeError) as cm:
            add(1000000000000000000)
        self.assertEqual(str(cm.exception), "add() missing 1 required positional argument: 'y'")