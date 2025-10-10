import unittest
from sut_llm.problem_HumanEval_78 import hex_key

class TestHexKey(unittest.TestCase):

    def test_example_ab(self):
        self.assertEqual(hex_key("AB"), 1)

    def test_example_1077e(self):
        self.assertEqual(hex_key("1077E"), 2)

    def test_example_abed1a33(self):
        self.assertEqual(hex_key("ABED1A33"), 4)

    def test_example_long_string(self):
        self.assertEqual(hex_key("123456789ABCDEF0"), 6)

    def test_example_2020(self):
        self.assertEqual(hex_key("2020"), 2)

    def test_empty_string(self):
        self.assertEqual(hex_key(""), 0)

    def test_no_prime_digits(self):
        self.assertEqual(hex_key("14689ACEF0"), 0)

    def test_all_prime_digits(self):
        self.assertEqual(hex_key("2357BD"), 6)

    def test_repeated_prime_digit(self):
        self.assertEqual(hex_key("DDDD"), 4)

    def test_mixed_long_string(self):
        self.assertEqual(hex_key("FADE23BEEF7D"), 6)

if __name__ == '__main__':
    unittest.main()