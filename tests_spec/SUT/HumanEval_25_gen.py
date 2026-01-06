import unittest
from sut.problem_HumanEval_25 import factorize

class Test_factorize(unittest.TestCase):

    def test_factorize_8(self):
        with self.assertRaises(TypeError) as cm:
            factorize("8")
        self.assertEqual(str(cm.exception), 'must be real number, not str')

    def test_factorize_25(self):
        with self.assertRaises(TypeError) as cm:
            factorize("25")
        self.assertEqual(str(cm.exception), 'must be real number, not str')

    def test_factorize_70(self):
        with self.assertRaises(TypeError) as cm:
            factorize("70")
        self.assertEqual(str(cm.exception), 'must be real number, not str')

    def test_factorize_12(self):
        with self.assertRaises(TypeError) as cm:
            factorize("12")
        self.assertEqual(str(cm.exception), 'must be real number, not str')

    def test_factorize_60(self):
        with self.assertRaises(TypeError) as cm:
            factorize("60")
        self.assertEqual(str(cm.exception), 'must be real number, not str')

    def test_factorize_1(self):
        with self.assertRaises(TypeError) as cm:
            factorize("1")
        self.assertEqual(str(cm.exception), 'must be real number, not str')

    def test_factorize_2(self):
        with self.assertRaises(TypeError) as cm:
            factorize("2")
        self.assertEqual(str(cm.exception), 'must be real number, not str')

    def test_factorize_17(self):
        with self.assertRaises(TypeError) as cm:
            factorize("17")
        self.assertEqual(str(cm.exception), 'must be real number, not str')

    def test_factorize_4(self):
        with self.assertRaises(TypeError) as cm:
            factorize("4")
        self.assertEqual(str(cm.exception), 'must be real number, not str')

    def test_factorize_997(self):
        with self.assertRaises(TypeError) as cm:
            factorize("997")
        self.assertEqual(str(cm.exception), 'must be real number, not str')