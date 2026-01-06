import unittest
from sut.problem_HumanEval_79 import decimal_to_binary

class Test_decimal_to_binary(unittest.TestCase):

    def test_normal_positive_15(self):
        """
        Test case for a typical positive integer: 15.
        Expected output: "db1111db"
        """
        result = decimal_to_binary(15)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "db1111db")
        self.assertTrue(result.startswith("db"))
        self.assertTrue(result.endswith("db"))
        self.assertEqual(result[2:-2], "1111")
        self.assertTrue(all(c in '01' for c in result[2:-2]))

    def test_normal_power_of_two_32(self):
        """
        Test case for a power of two: 32.
        Expected output: "db100000db"
        """
        result = decimal_to_binary(32)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "db100000db")
        self.assertTrue(result.startswith("db"))
        self.assertTrue(result.endswith("db"))
        self.assertEqual(result[2:-2], "100000")
        self.assertTrue(all(c in '01' for c in result[2:-2]))

    def test_normal_positive_10(self):
        """
        Test case for another typical positive integer: 10.
        Expected output: "db1010db"
        """
        result = decimal_to_binary(10)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "db1010db")
        self.assertTrue(result.startswith("db"))
        self.assertTrue(result.endswith("db"))
        self.assertEqual(result[2:-2], "1010")
        self.assertTrue(all(c in '01' for c in result[2:-2]))

    def test_edge_zero(self):
        """
        Test case for the smallest non-negative integer: 0.
        Expected output: "db0db"
        """
        result = decimal_to_binary(0)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "db0db")
        self.assertTrue(result.startswith("db"))
        self.assertTrue(result.endswith("db"))
        self.assertEqual(result[2:-2], "0")
        self.assertTrue(all(c in '01' for c in result[2:-2]))

    def test_edge_one(self):
        """
        Test case for the integer one: 1.
        Expected output: "db1db"
        """
        result = decimal_to_binary(1)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "db1db")
        self.assertTrue(result.startswith("db"))
        self.assertTrue(result.endswith("db"))
        self.assertEqual(result[2:-2], "1")
        self.assertTrue(all(c in '01' for c in result[2:-2]))

    def test_edge_two(self):
        """
        Test case for the integer two: 2.
        Expected output: "db10db"
        """
        result = decimal_to_binary(2)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "db10db")
        self.assertTrue(result.startswith("db"))
        self.assertTrue(result.endswith("db"))
        self.assertEqual(result[2:-2], "10")
        self.assertTrue(all(c in '01' for c in result[2:-2]))

    def test_error_negative_integer(self):
        """
        Test case for a negative integer input (-5).
        Should raise a ValueError as per preconditions.
        """
        with self.assertRaises(ValueError):
            decimal_to_binary(-5)

    def test_error_float_input(self):
        """
        Test case for a float input (15.5).
        Should raise a TypeError as per preconditions.
        """
        with self.assertRaises(TypeError):
            decimal_to_binary(15.5)

    def test_error_string_input(self):
        """
        Test case for a string input ("abc").
        Should raise a TypeError as per preconditions.
        """
        with self.assertRaises(TypeError):
            decimal_to_binary("abc")

    def test_error_none_input(self):
        """
        Test case for a None input.
        Should raise a TypeError as per preconditions.
        """
        with self.assertRaises(TypeError):
            decimal_to_binary(None)