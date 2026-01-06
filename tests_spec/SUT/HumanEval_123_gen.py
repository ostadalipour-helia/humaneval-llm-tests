import unittest
from sut.problem_HumanEval_123 import get_odd_collatz

class Test_get_odd_collatz(unittest.TestCase):

    def test_case_1(self):
        with self.assertRaises(TypeError) as cm:
            get_odd_collatz("n = 5")
        self.assertEqual(str(cm.exception), 'not all arguments converted during string formatting')

    def test_case_2(self):
        with self.assertRaises(TypeError) as cm:
            get_odd_collatz("n = 6")
        self.assertEqual(str(cm.exception), 'not all arguments converted during string formatting')

    def test_case_3(self):
        with self.assertRaises(TypeError) as cm:
            get_odd_collatz("n = 7")
        self.assertEqual(str(cm.exception), 'not all arguments converted during string formatting')

    def test_case_4(self):
        with self.assertRaises(TypeError) as cm:
            get_odd_collatz("n = 1")
        self.assertEqual(str(cm.exception), 'not all arguments converted during string formatting')

    def test_case_5(self):
        with self.assertRaises(TypeError) as cm:
            get_odd_collatz("n = 2")
        self.assertEqual(str(cm.exception), 'not all arguments converted during string formatting')

    def test_case_6(self):
        with self.assertRaises(TypeError) as cm:
            get_odd_collatz("n = 5")
        self.assertEqual(str(cm.exception), 'not all arguments converted during string formatting')

    def test_case_7(self):
        with self.assertRaises(TypeError) as cm:
            get_odd_collatz("n = 6")
        self.assertEqual(str(cm.exception), 'not all arguments converted during string formatting')

    def test_case_8(self):
        with self.assertRaises(TypeError) as cm:
            get_odd_collatz("n = 7")
        self.assertEqual(str(cm.exception), 'not all arguments converted during string formatting')

    def test_case_9(self):
        with self.assertRaises(TypeError) as cm:
            get_odd_collatz("n = 1")
        self.assertEqual(str(cm.exception), 'not all arguments converted during string formatting')

    def test_case_10(self):
        with self.assertRaises(TypeError) as cm:
            get_odd_collatz("n = 2")
        self.assertEqual(str(cm.exception), 'not all arguments converted during string formatting')