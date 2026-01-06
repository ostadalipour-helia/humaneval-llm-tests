import unittest
import sut.problem_HumanEval_76 as mod

class TestHybrid(unittest.TestCase):
    def test_basic_power_true(self):
            # Typical input where x is a simple power of n (2^3 = 8)
            self.assertEqual(mod.is_simple_power(8, 2), True)

    def test_basic_power_false(self):
            # Typical input where x is not a simple power of n
            self.assertEqual(mod.is_simple_power(3, 2), False)

    def test_boundary_x_is_one_n_greater_than_one(self):
            # Boundary condition: x = 1 (n^0 = 1 for any n > 0)
            self.assertEqual(mod.is_simple_power(1, 7), True)

    def test_boundary_x_equals_n_n_greater_than_one(self):
            # Boundary condition: x = n (n^1 = n)
            self.assertEqual(mod.is_simple_power(5, 5), True)

    def test_edge_n_is_one_x_is_one(self):
            # Edge case: n = 1, x = 1 (1^k = 1 for any k >= 0)
            self.assertEqual(mod.is_simple_power(1, 1), True)

    def test_edge_n_is_one_x_greater_than_one(self):
            # Edge case: n = 1, x > 1 (1^k is always 1, so x > 1 cannot be a power of 1)
            self.assertEqual(mod.is_simple_power(10, 1), False)

    def test_off_by_one_below_power(self):
            # Off-by-one error check: x is just below a power of n (2^3=8, 2^4=16)
            self.assertEqual(mod.is_simple_power(15, 2), False)

    def test_extreme_large_power(self):
            # Extreme input: a large number that is a power of n (2^16 = 65536)
            self.assertEqual(mod.is_simple_power(65536, 2), True)

    def test_extreme_n_is_zero_x_is_one(self):
            # Extreme input: n = 0, x = 1 (0^0 = 1)
            self.assertEqual(mod.is_simple_power(1, 0), True)

    def test_x_is_zero_n_positive(self):
            # Sign and Zero testing: x = 0, n > 0 (n^k is never 0 for n > 0)
            self.assertEqual(mod.is_simple_power(0, 5), False)
    
    if __name__ == '__main__':
        unittest.main()

    def test_x_is_one_any_n_true(self):
            # x=1, n=4, output: true (4^0 = 1)
            self.assertTrue(mod.is_simple_power(1, 4))

    def test_base_equals_power_true(self):
            # x=2, n=2, output: true (2^1 = 2)
            self.assertTrue(mod.is_simple_power(2, 2))

    def test_normal_power_true(self):
            # x=8, n=2, output: true (2^3 = 8)
            self.assertTrue(mod.is_simple_power(8, 2))

    def test_normal_not_power_false(self):
            # x=3, n=2, output: false (3 is not a power of 2)
            self.assertFalse(mod.is_simple_power(3, 2))

    def test_large_power_true(self):
            # x=27, n=3, output: true (3^3 = 27)
            self.assertTrue(mod.is_simple_power(27, 3))
    
        # Edge cases

    def test_x_is_one_n_is_one_true(self):
            # x=1, n=1, output: true (1^0 = 1)
            self.assertTrue(mod.is_simple_power(1, 1))

    def test_x_not_one_n_is_one_false(self):
            # x=3, n=1, output: false (1^k is always 1)
            self.assertFalse(mod.is_simple_power(3, 1))

    def test_prime_not_power_false(self):
            # x=7, n=2, output: false (7 is a prime number and not a power of 2)
            self.assertFalse(mod.is_simple_power(7, 2))

    def test_higher_power_true(self):
            # x=16, n=2, output: true (2^4 = 16)
            self.assertTrue(mod.is_simple_power(16, 2))
    
        # Error conditions (assuming ValueError for out-of-range integers, TypeError for wrong types)

