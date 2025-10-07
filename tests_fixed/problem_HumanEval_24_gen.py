import unittest
from sut_llm.problem_HumanEval_24 import largest_divisor

class TestLargestDivisor(unittest.TestCase):

    def test_docstring_example(self):
        self.assertEqual(largest_divisor(15), 5)

    def test_simple_composite(self):
        self.assertEqual(largest_divisor(10), 5)

    def test_prime_number(self):
        self.assertEqual(largest_divisor(7), 1)

    def test_smallest_prime(self):
        self.assertEqual(largest_divisor(2), 1)

    def test_smallest_composite_power_of_two(self):
        self.assertEqual(largest_divisor(4), 2)

    def test_perfect_square(self):
        self.assertEqual(largest_divisor(25), 5)

    def test_larger_composite_many_factors(self):
        self.assertEqual(largest_divisor(30), 15)

    def test_another_prime(self):
        self.assertEqual(largest_divisor(13), 1)

    def test_larger_power_of_two(self):
        self.assertEqual(largest_divisor(16), 8)

    def test_another_composite(self):
        self.assertEqual(largest_divisor(42), 21)

if __name__ == '__main__':
    unittest.main()