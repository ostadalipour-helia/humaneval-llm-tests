import unittest
from sut_llm.problem_HumanEval_79 import decimal_to_binary

class TestDecimalToBinary(unittest.TestCase):

    def test_zero_input(self):
        """
        Test case for the input 0.
        Covers: Edge Case, Boundary, Sign/Zero.
        Expected: "db0db"
        """
        self.assertEqual(decimal_to_binary(0), "db0db")

    def test_one_input(self):
        """
        Test case for the input 1.
        Covers: Edge Case, Boundary.
        Expected: "db1db"
        """
        self.assertEqual(decimal_to_binary(1), "db1db")

    def test_two_input(self):
        """
        Test case for the input 2 (smallest power of 2 > 1).
        Covers: Boundary, Off-by-One (relative to 1 and 3).
        Expected: "db10db"
        """
        self.assertEqual(decimal_to_binary(2), "db10db")

    def test_three_input(self):
        """
        Test case for the input 3 (just below a power of 2).
        Covers: Boundary, Off-by-One (relative to 2 and 4).
        Expected: "db11db"
        """
        self.assertEqual(decimal_to_binary(3), "db11db")

    def test_fifteen_example(self):
        """
        Test case for the example input 15.
        Covers: Typical Input, Boundary (all ones, just below 16).
        Expected: "db1111db"
        """
        self.assertEqual(decimal_to_binary(15), "db1111db")

    def test_thirty_two_example(self):
        """
        Test case for the example input 32.
        Covers: Typical Input, Boundary (power of 2).
        Expected: "db100000db"
        """
        self.assertEqual(decimal_to_binary(32), "db100000db")

    def test_thirty_one_input(self):
        """
        Test case for the input 31 (just below 32).
        Covers: Off-by-One, Boundary (all ones).
        Expected: "db11111db"
        """
        self.assertEqual(decimal_to_binary(31), "db11111db")

    def test_forty_two_input(self):
        """
        Test case for an input with alternating bits.
        Covers: Extreme/Unusual Input, Logic Mutations.
        Expected: "db101010db"
        """
        self.assertEqual(decimal_to_binary(42), "db101010db")

    def test_two_hundred_fifty_five_input(self):
        """
        Test case for a larger input (2^8 - 1).
        Covers: Extreme/Unusual Input, Boundary (many ones).
        Expected: "db11111111db"
        """
        self.assertEqual(decimal_to_binary(255), "db11111111db")

    def test_two_hundred_fifty_six_input(self):
        """
        Test case for a larger input (2^8).
        Covers: Extreme/Unusual Input, Boundary (power of 2, many zeros).
        Expected: "db100000000db"
        """
        self.assertEqual(decimal_to_binary(256), "db100000000db")

if __name__ == '__main__':
    unittest.main()