import unittest
from sut_llm.problem_HumanEval_150 import x_or_y

class TestXOrY(unittest.TestCase):

    def test_smallest_prime(self):
        # Boundary: n=2, smallest prime number
        # Should return x
        self.assertEqual(x_or_y(2, 10, 20), 10)

    def test_one_not_prime(self):
        # Edge Case: n=1, not a prime number
        # Should return y
        self.assertEqual(x_or_y(1, 5, 10), 10)

    def test_smallest_composite(self):
        # Boundary: n=4, smallest composite number
        # Should return y
        self.assertEqual(x_or_y(4, 50, 60), 60)

    def test_example_prime(self):
        # Typical Input: n=7, a prime number (from docstring example)
        # Should return x
        self.assertEqual(x_or_y(7, 34, 12), 34)

    def test_example_composite(self):
        # Typical Input: n=15, a composite number (from docstring example)
        # Should return y
        self.assertEqual(x_or_y(15, 8, 5), 5)

    def test_zero_not_prime(self):
        # Edge Case: n=0, not a prime number
        # Should return y
        self.assertEqual(x_or_y(0, -1, -2), -2)

    def test_next_prime(self):
        # Boundary/Typical: n=3, the next prime after 2
        # Should return x
        self.assertEqual(x_or_y(3, 100, 200), 100)

    def test_large_prime(self):
        # Extreme Input: n=97, a larger prime number
        # Should return x
        self.assertEqual(x_or_y(97, 'prime', 'composite'), 'prime')

    def test_large_composite(self):
        # Extreme Input: n=100, a larger composite number
        # Should return y
        self.assertEqual(x_or_y(100, 'yes', 'no'), 'no')

    def test_negative_n(self):
        # Sign/Extreme Input: n=-5, negative numbers are not prime
        # Should return y
        self.assertEqual(x_or_y(-5, 1000, 2000), 2000)

if __name__ == '__main__':
    unittest.main()