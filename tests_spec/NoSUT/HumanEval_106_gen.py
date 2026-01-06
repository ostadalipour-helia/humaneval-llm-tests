import unittest
from sut.problem_HumanEval_106 import f

class Test_f(unittest.TestCase):
    def test_normal_n5(self):
        self.assertEqual(f(5), [1, 2, 6, 24, 15])

    def test_normal_n1(self):
        self.assertEqual(f(1), [1])

    def test_normal_n2(self):
        self.assertEqual(f(2), [1, 2])

    def test_normal_n4(self):
        self.assertEqual(f(4), [1, 2, 6, 24])

    def test_edge_n0(self):
        self.assertEqual(f(0), [])

    def test_error_negative_n(self):
        with self.assertRaises(ValueError):
            f(-1)

    def test_error_float_n(self):
        with self.assertRaises(TypeError):
            f(3.5)

    def test_error_string_n(self):
        with self.assertRaises(TypeError):
            f("abc")