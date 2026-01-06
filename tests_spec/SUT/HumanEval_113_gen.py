import unittest
from sut.problem_HumanEval_113 import odd_count

class Test_odd_count(unittest.TestCase):

    def test_case_1(self):
        with self.assertRaises(ValueError) as cm:
            odd_count("['1234567']")
        self.assertEqual(str(cm.exception), "invalid literal for int() with base 10: '['")

    def test_case_2(self):
        with self.assertRaises(ValueError) as cm:
            odd_count("['3', '11111111']")
        self.assertEqual(str(cm.exception), "invalid literal for int() with base 10: '['")

    def test_case_3(self):
        with self.assertRaises(ValueError) as cm:
            odd_count("['02468', '13579']")
        self.assertEqual(str(cm.exception), "invalid literal for int() with base 10: '['")

    def test_case_4(self):
        with self.assertRaises(ValueError) as cm:
            odd_count("[]")
        self.assertEqual(str(cm.exception), "invalid literal for int() with base 10: '['")

    def test_case_5(self):
        with self.assertRaises(ValueError) as cm:
            odd_count("['']")
        self.assertEqual(str(cm.exception), "invalid literal for int() with base 10: '['")

    def test_case_6(self):
        with self.assertRaises(ValueError) as cm:
            odd_count("['7']")
        self.assertEqual(str(cm.exception), "invalid literal for int() with base 10: '['")

    def test_case_7(self):
        with self.assertRaises(ValueError) as cm:
            odd_count("['8']")
        self.assertEqual(str(cm.exception), "invalid literal for int() with base 10: '['")

    def test_case_8_duplicate(self):
        with self.assertRaises(ValueError) as cm:
            odd_count("['1234567']")
        self.assertEqual(str(cm.exception), "invalid literal for int() with base 10: '['")

    def test_case_9_duplicate(self):
        with self.assertRaises(ValueError) as cm:
            odd_count("['3', '11111111']")
        self.assertEqual(str(cm.exception), "invalid literal for int() with base 10: '['")

    def test_case_10_duplicate(self):
        with self.assertRaises(ValueError) as cm:
            odd_count("['02468', '13579']")
        self.assertEqual(str(cm.exception), "invalid literal for int() with base 10: '['")