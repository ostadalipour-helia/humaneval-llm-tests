import unittest
from sut_llm.problem_HumanEval_76 import is_simple_power

class TestIsSimplePower(unittest.TestCase):

    def test_basic_power_true(self):
        # Typical input where x is a simple power of n (2^3 = 8)
        self.assertEqual(is_simple_power(8, 2), True)

    def test_basic_power_false(self):
        # Typical input where x is not a simple power of n
        self.assertEqual(is_simple_power(3, 2), False)

    def test_boundary_x_is_one_n_greater_than_one(self):
        # Boundary condition: x = 1 (n^0 = 1 for any n > 0)
        self.assertEqual(is_simple_power(1, 7), True)

    def test_boundary_x_equals_n_n_greater_than_one(self):
        # Boundary condition: x = n (n^1 = n)
        self.assertEqual(is_simple_power(5, 5), True)

    def test_edge_n_is_one_x_is_one(self):
        # Edge case: n = 1, x = 1 (1^k = 1 for any k >= 0)
        self.assertEqual(is_simple_power(1, 1), True)

    def test_edge_n_is_one_x_greater_than_one(self):
        # Edge case: n = 1, x > 1 (1^k is always 1, so x > 1 cannot be a power of 1)
        self.assertEqual(is_simple_power(10, 1), False)

    def test_off_by_one_below_power(self):
        # Off-by-one error check: x is just below a power of n (2^3=8, 2^4=16)
        self.assertEqual(is_simple_power(15, 2), False)

    def test_extreme_large_power(self):
        # Extreme input: a large number that is a power of n (2^16 = 65536)
        self.assertEqual(is_simple_power(65536, 2), True)

    def test_extreme_n_is_zero_x_is_one(self):
        # Extreme input: n = 0, x = 1 (0^0 = 1)
        self.assertEqual(is_simple_power(1, 0), True)

    def test_x_is_zero_n_positive(self):
        # Sign and Zero testing: x = 0, n > 0 (n^k is never 0 for n > 0)
        self.assertEqual(is_simple_power(0, 5), False)

    def test_special_n_cases(self):
        # Covers line 31: return False (when n is 0 and x is not 0 or 1)
        self.assertFalse(is_simple_power(5, 0))
        # Covers line 43: return x == -1 (when n is -1 and x is -1)
        self.assertTrue(is_simple_power(-1, -1))
        # Covers line 43: return x == -1 (when n is -1 and x is not -1)
        self.assertFalse(is_simple_power(-5, -1))

    def test_negative_x_and_x_equals_n(self):
        # Covers line 51: return False (when x < 0 and n > 0)
        self.assertFalse(is_simple_power(-8, 2))
        # Covers line 57: return True (when temp_x becomes equal to n)
        self.assertTrue(is_simple_power(7, 7))
        # Another case for line 57: when x is a power of n and eventually temp_x == n
        self.assertTrue(is_simple_power(4, -2)) # 4 // -2 = -2, then temp_x == n

if __name__ == '__main__':
    unittest.main()