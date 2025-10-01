import unittest
from sut.problem_HumanEval_79 import decimal_to_binary

class TestDecimalToBinary(unittest.TestCase):

    def test_example_15(self):
        self.assertEqual(decimal_to_binary(15), "db1111db")

    def test_example_32(self):
        self.assertEqual(decimal_to_binary(32), "db100000db")

    def test_zero(self):
        self.assertEqual(decimal_to_binary(0), "db0db")

    def test_one(self):
        self.assertEqual(decimal_to_binary(1), "db1db")

    def test_two(self):
        self.assertEqual(decimal_to_binary(2), "db10db")

    def test_seven(self):
        self.assertEqual(decimal_to_binary(7), "db111db")

    def test_eight(self):
        self.assertEqual(decimal_to_binary(8), "db1000db")

    def test_twenty_five(self):
        self.assertEqual(decimal_to_binary(25), "db11001db")

    def test_sixty_three(self):
        self.assertEqual(decimal_to_binary(63), "db111111db")

    def test_forty_two(self):
        self.assertEqual(decimal_to_binary(42), "db101010db")

if __name__ == '__main__':
    unittest.main()