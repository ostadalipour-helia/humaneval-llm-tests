import unittest
from sut.problem_HumanEval_130 import tri

class Test_tri(unittest.TestCase):
    def test_normal_case_n3(self):
        # Normal case: n = 3
        n = 3
        expected_output = [1, 3, 2, 8]
        self.assertEqual(tri(n), expected_output)

    def test_normal_case_n4(self):
        # Normal case: n = 4
        n = 4
        expected_output = [1, 3, 2, 8, 3]
        self.assertEqual(tri(n), expected_output)

    def test_normal_case_n5(self):
        # Normal case: n = 5
        n = 5
        expected_output = [1, 3, 2, 8, 3, 15]
        self.assertEqual(tri(n), expected_output)

    def test_edge_case_n0(self):
        # Edge case: Smallest valid input for n (n = 0)
        n = 0
        expected_output = [1]
        self.assertEqual(tri(n), expected_output)

    def test_edge_case_n1(self):
        # Edge case: n = 1
        n = 1
        expected_output = [1, 3]
        self.assertEqual(tri(n), expected_output)

    def test_edge_case_n2(self):
        # Edge case: n = 2
        n = 2
        expected_output = [1, 3, 2]
        self.assertEqual(tri(n), expected_output)

    def test_error_n_negative(self):
        # Error case: n is negative
        n = -1
        with self.assertRaises(ValueError):
            tri(n)

    def test_error_n_float(self):
        # Error case: n is a float
        n = 1.5
        with self.assertRaises(TypeError):
            tri(n)

    def test_error_n_string(self):
        # Error case: n is a string
        n = 'abc'
        with self.assertRaises(TypeError):
            tri(n)