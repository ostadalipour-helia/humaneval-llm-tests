import unittest
from sut.problem_HumanEval_46 import fib4

class Test_fib4(unittest.TestCase):

    def test_case_0(self):
        with self.assertRaises(TypeError) as cm:
            fib4("n = 5")
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_1(self):
        with self.assertRaises(TypeError) as cm:
            fib4("n = 6")
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_2(self):
        with self.assertRaises(TypeError) as cm:
            fib4("n = 7")
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_3(self):
        with self.assertRaises(TypeError) as cm:
            fib4("n = 4")
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_4(self):
        with self.assertRaises(TypeError) as cm:
            fib4("n = 0")
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_5(self):
        with self.assertRaises(TypeError) as cm:
            fib4("n = 1")
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_6(self):
        with self.assertRaises(TypeError) as cm:
            fib4("n = 2")
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_7(self):
        with self.assertRaises(TypeError) as cm:
            fib4("n = 3")
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_8(self):
        with self.assertRaises(TypeError) as cm:
            fib4("n = 5")
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_9(self):
        with self.assertRaises(TypeError) as cm:
            fib4("n = 6")
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")