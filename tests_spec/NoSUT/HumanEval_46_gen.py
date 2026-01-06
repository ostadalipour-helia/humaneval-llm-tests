import unittest
from sut.problem_HumanEval_46 import fib4

class Test_fib4(unittest.TestCase):
    def test_fib4_n0_edge(self):
        """Test case for n = 0, an edge case."""
        self.assertEqual(fib4(0), 0)

    def test_fib4_n1_edge(self):
        """Test case for n = 1, an edge case."""
        self.assertEqual(fib4(1), 0)

    def test_fib4_n2_edge(self):
        """Test case for n = 2, an edge case."""
        self.assertEqual(fib4(2), 2)

    def test_fib4_n3_edge(self):
        """Test case for n = 3, an edge case."""
        self.assertEqual(fib4(3), 0)

    def test_fib4_n4_normal(self):
        """Test case for n = 4, a normal case."""
        self.assertEqual(fib4(4), 2)

    def test_fib4_n5_normal(self):
        """Test case for n = 5, a normal case."""
        self.assertEqual(fib4(5), 4)

    def test_fib4_n6_normal(self):
        """Test case for n = 6, a normal case."""
        self.assertEqual(fib4(6), 8)

    def test_fib4_n7_normal(self):
        """Test case for n = 7, a normal case."""
        self.assertEqual(fib4(7), 14)

    def test_fib4_non_integer_input(self):
        """Test case for non-integer input, expecting TypeError."""
        with self.assertRaises(TypeError):
            fib4(3.5)
        with self.assertRaises(TypeError):
            fib4("abc")
        with self.assertRaises(TypeError):
            fib4([1])

    def test_fib4_negative_input(self):
        """Test case for negative integer input, expecting ValueError."""
        with self.assertRaises(ValueError):
            fib4(-1)
        with self.assertRaises(ValueError):
            fib4(-5)