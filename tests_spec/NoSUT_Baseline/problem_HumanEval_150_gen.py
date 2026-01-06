import unittest
import sut.problem_HumanEval_150 as mod

class TestHybrid(unittest.TestCase):
    def test_smallest_prime(self):
            # Boundary: n=2, smallest prime number
            # Should return x
            self.assertEqual(mod.x_or_y(2, 10, 20), 10)

    def test_one_not_prime(self):
            # Edge Case: n=1, not a prime number
            # Should return y
            self.assertEqual(mod.x_or_y(1, 5, 10), 10)

    def test_smallest_composite(self):
            # Boundary: n=4, smallest composite number
            # Should return y
            self.assertEqual(mod.x_or_y(4, 50, 60), 60)

    def test_example_prime(self):
            # Typical Input: n=7, a prime number (from docstring example)
            # Should return x
            self.assertEqual(mod.x_or_y(7, 34, 12), 34)

    def test_example_composite(self):
            # Typical Input: n=15, a composite number (from docstring example)
            # Should return y
            self.assertEqual(mod.x_or_y(15, 8, 5), 5)

    def test_next_prime(self):
            # Boundary/Typical: n=3, the next prime after 2
            # Should return x
            self.assertEqual(mod.x_or_y(3, 100, 200), 100)

    def test_large_prime(self):
            # Extreme Input: n=97, a larger prime number
            # Should return x
            self.assertEqual(mod.x_or_y(97, 'prime', 'composite'), 'prime')

    def test_large_composite(self):
            # Extreme Input: n=100, a larger composite number
            # Should return y
            self.assertEqual(mod.x_or_y(100, 'yes', 'no'), 'no')

    def test_normal_prime_int(self):
            # 7 is a prime number, so x (34) is returned.
            n, x, y = 7, 34, 12
            self.assertEqual(mod.x_or_y(n, x, y), 34)

    def test_normal_composite_int(self):
            # 15 is not a prime number (15 = 3 * 5), so y (5) is returned.
            n, x, y = 15, 8, 5
            self.assertEqual(mod.x_or_y(n, x, y), 5)

    def test_normal_prime_string(self):
            # 13 is a prime number, so x ('hello') is returned. x and y can be strings.
            n, x, y = 13, "hello", "world"
            self.assertEqual(mod.x_or_y(n, x, y), "hello")

    def test_edge_n_is_one(self):
            # 1 is not considered a prime number, so y (200) is returned.
            n, x, y = 1, 100, 200
            self.assertEqual(mod.x_or_y(n, x, y), 200)

    def test_edge_n_is_two(self):
            # 2 is the smallest prime number, so x (10) is returned.
            n, x, y = 2, 10, 20
            self.assertEqual(mod.x_or_y(n, x, y), 10)

    def test_edge_n_is_four(self):
            # 4 is the smallest composite number, so y (20) is returned.
            n, x, y = 4, 10, 20
            self.assertEqual(mod.x_or_y(n, x, y), 20)

    def test_edge_prime_float(self):
            # 29 is a prime number, so x (5.5) is returned. x and y can be floats.
            n, x, y = 29, 5.5, 10.1
            self.assertEqual(mod.x_or_y(n, x, y), 5.5)

    def test_error_n_not_int_float(self):
            # n must be an integer according to preconditions.
            n, x, y = 7.5, 10, 20
            with self.assertRaises(TypeError):
                mod.x_or_y(n, x, y)

