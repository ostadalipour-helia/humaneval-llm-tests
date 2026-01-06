import unittest
from sut.problem_HumanEval_150 import x_or_y

class Test_x_or_y(unittest.TestCase):
    def test_normal_prime_int(self):
        # 7 is a prime number, so x (34) is returned.
        n, x, y = 7, 34, 12
        self.assertEqual(x_or_y(n, x, y), 34)

    def test_normal_composite_int(self):
        # 15 is not a prime number (15 = 3 * 5), so y (5) is returned.
        n, x, y = 15, 8, 5
        self.assertEqual(x_or_y(n, x, y), 5)

    def test_normal_prime_string(self):
        # 13 is a prime number, so x ('hello') is returned. x and y can be strings.
        n, x, y = 13, "hello", "world"
        self.assertEqual(x_or_y(n, x, y), "hello")

    def test_edge_n_is_one(self):
        # 1 is not considered a prime number, so y (200) is returned.
        n, x, y = 1, 100, 200
        self.assertEqual(x_or_y(n, x, y), 200)

    def test_edge_n_is_two(self):
        # 2 is the smallest prime number, so x (10) is returned.
        n, x, y = 2, 10, 20
        self.assertEqual(x_or_y(n, x, y), 10)

    def test_edge_n_is_four(self):
        # 4 is the smallest composite number, so y (20) is returned.
        n, x, y = 4, 10, 20
        self.assertEqual(x_or_y(n, x, y), 20)

    def test_edge_prime_float(self):
        # 29 is a prime number, so x (5.5) is returned. x and y can be floats.
        n, x, y = 29, 5.5, 10.1
        self.assertEqual(x_or_y(n, x, y), 5.5)

    def test_error_n_zero(self):
        # n must be a positive integer according to preconditions.
        n, x, y = 0, 10, 20
        with self.assertRaises(ValueError):
            x_or_y(n, x, y)

    def test_error_n_negative(self):
        # n must be a positive integer according to preconditions.
        n, x, y = -5, 10, 20
        with self.assertRaises(ValueError):
            x_or_y(n, x, y)

    def test_error_n_not_int_string(self):
        # n must be an integer according to preconditions.
        n, x, y = "abc", 10, 20
        with self.assertRaises(TypeError):
            x_or_y(n, x, y)

    def test_error_n_not_int_float(self):
        # n must be an integer according to preconditions.
        n, x, y = 7.5, 10, 20
        with self.assertRaises(TypeError):
            x_or_y(n, x, y)