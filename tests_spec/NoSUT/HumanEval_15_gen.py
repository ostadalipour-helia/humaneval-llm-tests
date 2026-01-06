import unittest
from sut.problem_HumanEval_15 import string_sequence

class Test_string_sequence(unittest.TestCase):
    def test_normal_five(self):
        # A typical sequence of numbers.
        self.assertEqual(string_sequence(5), '0 1 2 3 4 5')

    def test_normal_three(self):
        # Another typical sequence.
        self.assertEqual(string_sequence(3), '0 1 2 3')

    def test_edge_zero(self):
        # The smallest valid input, sequence contains only 0.
        self.assertEqual(string_sequence(0), '0')

    def test_edge_one(self):
        # A minimal sequence with a single space delimiter.
        self.assertEqual(string_sequence(1), '0 1')

    def test_error_negative_n(self):
        # Input n is negative, which is outside the specified range [0, n].
        with self.assertRaises(ValueError):
            string_sequence(-1)

    def test_error_float_n(self):
        # Input n is not an integer.
        with self.assertRaises(TypeError):
            string_sequence(2.5)

    def test_error_string_n(self):
        # Input n is not an integer.
        with self.assertRaises(TypeError):
            string_sequence('abc')