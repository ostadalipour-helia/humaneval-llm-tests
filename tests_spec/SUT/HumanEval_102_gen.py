import unittest
from sut.problem_HumanEval_102 import choose_num

class Test_choose_num(unittest.TestCase):

    def test_case_0(self):
        with self.assertRaises(TypeError) as cm:
            choose_num(12)
        self.assertEqual(str(cm.exception), "choose_num() missing 1 required positional argument: 'y'")

    def test_case_1(self):
        with self.assertRaises(TypeError) as cm:
            choose_num(10)
        self.assertEqual(str(cm.exception), "choose_num() missing 1 required positional argument: 'y'")

    def test_case_2(self):
        with self.assertRaises(TypeError) as cm:
            choose_num(11)
        self.assertEqual(str(cm.exception), "choose_num() missing 1 required positional argument: 'y'")

    def test_case_3(self):
        with self.assertRaises(TypeError) as cm:
            choose_num(10)
        self.assertEqual(str(cm.exception), "choose_num() missing 1 required positional argument: 'y'")

    def test_case_4(self):
        with self.assertRaises(TypeError) as cm:
            choose_num(1)
        self.assertEqual(str(cm.exception), "choose_num() missing 1 required positional argument: 'y'")

    def test_case_5(self):
        with self.assertRaises(TypeError) as cm:
            choose_num(13)
        self.assertEqual(str(cm.exception), "choose_num() missing 1 required positional argument: 'y'")

    def test_case_6(self):
        with self.assertRaises(TypeError) as cm:
            choose_num(13)
        self.assertEqual(str(cm.exception), "choose_num() missing 1 required positional argument: 'y'")

    def test_case_7(self):
        with self.assertRaises(TypeError) as cm:
            choose_num(1)
        self.assertEqual(str(cm.exception), "choose_num() missing 1 required positional argument: 'y'")

    def test_case_8(self):
        with self.assertRaises(TypeError) as cm:
            choose_num(1)
        self.assertEqual(str(cm.exception), "choose_num() missing 1 required positional argument: 'y'")

    def test_case_9(self):
        with self.assertRaises(TypeError) as cm:
            choose_num(2)
        self.assertEqual(str(cm.exception), "choose_num() missing 1 required positional argument: 'y'")