import unittest
from sut_llm.problem_HumanEval_32 import find_zero

class TestFindZero(unittest.TestCase):

    def test_linear_example(self):
        # f(x) = 1 + 2x, expected root = -0.5
        self.assertAlmostEqual(find_zero([1, 2]), -0.5, places=2)

    def test_linear_positive_root(self):
        # f(x) = -5 + x, expected root = 5.0
        self.assertAlmostEqual(find_zero([-5, 1]), 5.0, places=2)

    def test_linear_negative_root(self):
        # f(x) = 3 + x, expected root = -3.0
        self.assertAlmostEqual(find_zero([3, 1]), -3.0, places=2)

    def test_linear_zero_root(self):
        # f(x) = x, expected root = 0.0
        self.assertAlmostEqual(find_zero([0, 1]), 0.0, places=2)

    def test_cubic_example(self):
        # f(x) = -6 + 11x - 6x^2 + x^3, roots are 1, 2, 3. Example returns 1.0
        self.assertAlmostEqual(find_zero([-6, 11, -6, 1]), 1.0, places=2)

    def test_cubic_zero_root(self):
        # f(x) = x^3, expected root = 0.0
        self.assertAlmostEqual(find_zero([0, 0, 0, 1]), 0.0, places=2)

    def test_cubic_negative_root(self):
        # f(x) = 1 + x^3, expected root = -1.0
        self.assertAlmostEqual(find_zero([1, 0, 0, 1]), -1.0, places=2)

    def test_cubic_positive_root(self):
        # f(x) = -27 + x^3, expected root = 3.0
        self.assertAlmostEqual(find_zero([-27, 0, 0, 1]), 3.0, places=2)

    def test_quintic_zero_root(self):
        # f(x) = x^5, expected root = 0.0
        self.assertAlmostEqual(find_zero([0, 0, 0, 0, 0, 1]), 0.0, places=2)

    def test_quintic_negative_root(self):
        # f(x) = 32 + x^5, expected root = -2.0
        self.assertAlmostEqual(find_zero([32, 0, 0, 0, 0, 1]), -2.0, places=2)