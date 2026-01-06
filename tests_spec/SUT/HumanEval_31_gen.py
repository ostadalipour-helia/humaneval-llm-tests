import unittest
from sut.problem_HumanEval_31 import is_prime

class Test_is_prime(unittest.TestCase):

    def test_case_0(self):
        with self.assertRaises(TypeError) as cm:
            is_prime("n = 101")
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_1(self):
        with self.assertRaises(TypeError) as cm:
            is_prime("n = 11")
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_2(self):
        with self.assertRaises(TypeError) as cm:
            is_prime("n = 13441")
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_3(self):
        with self.assertRaises(TypeError) as cm:
            is_prime("n = 61")
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_4(self):
        with self.assertRaises(TypeError) as cm:
            is_prime("n = 6")
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_5(self):
        with self.assertRaises(TypeError) as cm:
            is_prime("n = 4")
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_6(self):
        with self.assertRaises(TypeError) as cm:
            is_prime("n = 1")
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_7(self):
        with self.assertRaises(TypeError) as cm:
            is_prime("n = 2")
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_8(self):
        with self.assertRaises(TypeError) as cm:
            is_prime("n = 0")
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_9(self):
        with self.assertRaises(TypeError) as cm:
            is_prime("n = -5")
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")