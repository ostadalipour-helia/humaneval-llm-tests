import unittest
from sut_llm.problem_HumanEval_31 import is_prime

class TestIsPrime(unittest.TestCase):

    def test_is_prime_small_composite_six(self):
        self.assertFalse(is_prime(6))

    def test_is_prime_small_prime_one_hundred_one(self):
        self.assertTrue(is_prime(101))

    def test_is_prime_small_prime_eleven(self):
        self.assertTrue(is_prime(11))

    def test_is_prime_large_prime_thirteen_thousand_four_hundred_forty_one(self):
        self.assertTrue(is_prime(13441))

    def test_is_prime_small_prime_sixty_one(self):
        self.assertTrue(is_prime(61))

    def test_is_prime_small_composite_four(self):
        self.assertFalse(is_prime(4))

    def test_is_prime_edge_case_one(self):
        self.assertFalse(is_prime(1))

    def test_is_prime_smallest_prime_two(self):
        self.assertTrue(is_prime(2))

    def test_is_prime_edge_case_zero(self):
        self.assertFalse(is_prime(0))

    def test_is_prime_another_composite_nine(self):
        self.assertFalse(is_prime(9))

if __name__ == '__main__':
    unittest.main()