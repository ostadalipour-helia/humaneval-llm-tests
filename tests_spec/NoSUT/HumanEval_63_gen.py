import unittest
from sut.problem_HumanEval_63 import fibfib

class Test_fibfib(unittest.TestCase):
    def test_normal_n5(self):
        """
        Test case for n = 5, expected output 4.
        Description: Typical case for n > 2
        """
        self.assertEqual(fibfib(5), 4)

    def test_normal_n8(self):
        """
        Test case for n = 8, expected output 24.
        Description: Another typical case for n > 2
        """
        self.assertEqual(fibfib(8), 24)

    def test_normal_n3(self):
        """
        Test case for n = 3, expected output 1.
        Description: First recursive step: fibfib(3) = fibfib(2) + fibfib(1) + fibfib(0) = 1 + 0 + 0 = 1
        """
        self.assertEqual(fibfib(3), 1)

    def test_normal_n4(self):
        """
        Test case for n = 4, expected output 2.
        Description: Second recursive step: fibfib(4) = fibfib(3) + fibfib(2) + fibfib(1) = 1 + 1 + 0 = 2
        """
        self.assertEqual(fibfib(4), 2)

    def test_edge_n0(self):
        """
        Test case for n = 0, expected output 0.
        Description: Base case: n = 0
        """
        self.assertEqual(fibfib(0), 0)

    def test_edge_n1(self):
        """
        Test case for n = 1, expected output 0.
        Description: Base case: n = 1
        """
        self.assertEqual(fibfib(1), 0)

    def test_edge_n2(self):
        """
        Test case for n = 2, expected output 1.
        Description: Base case: n = 2
        """
        self.assertEqual(fibfib(2), 1)

    def test_error_negative_n(self):
        """
        Test case for n = -1, expecting a ValueError.
        Description: Input n is negative.
        """
        with self.assertRaises(ValueError):
            fibfib(-1)

    def test_error_non_integer_string(self):
        """
        Test case for n = "abc", expecting a TypeError.
        Description: Input n is not an integer.
        """
        with self.assertRaises(TypeError):
            fibfib("abc")

    def test_error_non_integer_float(self):
        """
        Test case for n = 3.5, expecting a TypeError.
        Description: Input n is a float.
        """
        with self.assertRaises(TypeError):
            fibfib(3.5)