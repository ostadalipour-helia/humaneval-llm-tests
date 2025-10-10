import unittest
from sut_llm.problem_HumanEval_25 import factorize

class TestFactorize(unittest.TestCase):

    def test_example_eight(self):
        self.assertEqual(factorize(8), [2, 2, 2])

    def test_example_twenty_five(self):
        self.assertEqual(factorize(25), [5, 5])

    def test_example_seventy(self):
        self.assertEqual(factorize(70), [2, 5, 7])

    def test_prime_two(self):
        self.assertEqual(factorize(2), [2])

    def test_prime_thirteen(self):
        self.assertEqual(factorize(13), [13])

    def test_composite_twelve(self):
        self.assertEqual(factorize(12), [2, 2, 3])

    def test_composite_thirty(self):
        self.assertEqual(factorize(30), [2, 3, 5])

    def test_power_of_two(self):
        self.assertEqual(factorize(32), [2, 2, 2, 2, 2])

    def test_power_of_three(self):
        self.assertEqual(factorize(81), [3, 3, 3, 3])

    def test_edge_one(self):
        self.assertEqual(factorize(1), [])

if __name__ == '__main__':
    unittest.main()