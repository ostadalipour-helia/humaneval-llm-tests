import unittest
from sut.problem_HumanEval_131 import digits

class Test_digits(unittest.TestCase):

    def test_case_1(self):
        with self.assertRaises(ValueError) as cm:
            digits(1)
        self.assertEqual(str(cm.exception), "invalid literal for int() with base 10: 'n'")

    def test_case_235(self):
        with self.assertRaises(ValueError) as cm:
            digits(235)
        self.assertEqual(str(cm.exception), "invalid literal for int() with base 10: 'n'")

    def test_case_137(self):
        with self.assertRaises(ValueError) as cm:
            digits(137)
        self.assertEqual(str(cm.exception), "invalid literal for int() with base 10: 'n'")

    def test_case_12345(self):
        with self.assertRaises(ValueError) as cm:
            digits(12345)
        self.assertEqual(str(cm.exception), "invalid literal for int() with base 10: 'n'")

    def test_case_4(self):
        with self.assertRaises(ValueError) as cm:
            digits(4)
        self.assertEqual(str(cm.exception), "invalid literal for int() with base 10: 'n'")

    def test_case_246(self):
        with self.assertRaises(ValueError) as cm:
            digits(246)
        self.assertEqual(str(cm.exception), "invalid literal for int() with base 10: 'n'")

    def test_case_10(self):
        with self.assertRaises(ValueError) as cm:
            digits(10)
        self.assertEqual(str(cm.exception), "invalid literal for int() with base 10: 'n'")

    def test_case_9(self):
        with self.assertRaises(ValueError) as cm:
            digits(9)
        self.assertEqual(str(cm.exception), "invalid literal for int() with base 10: 'n'")

    def test_case_2(self):
        with self.assertRaises(ValueError) as cm:
            digits(2)
        self.assertEqual(str(cm.exception), "invalid literal for int() with base 10: 'n'")

    def test_case_1000000000000000000(self):
        with self.assertRaises(ValueError) as cm:
            digits(1000000000000000000)
        self.assertEqual(str(cm.exception), "invalid literal for int() with base 10: 'n'")