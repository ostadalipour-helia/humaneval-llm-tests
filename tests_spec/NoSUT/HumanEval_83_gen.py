import unittest
from sut.problem_HumanEval_83 import starts_one_ends

class Test_starts_one_ends(unittest.TestCase):
    def test_edge_n_1(self):
        # Edge case: n = 1
        # Expected output: 1 (Only '1' is a 1-digit number that starts or ends with 1)
        self.assertEqual(starts_one_ends(1), 1)

    def test_normal_n_2(self):
        # Normal case: n = 2
        # Expected output: 18 (18 * 10^(2-2) = 18 * 10^0 = 18)
        self.assertEqual(starts_one_ends(2), 18)

    def test_normal_n_3(self):
        # Normal case: n = 3
        # Expected output: 180 (18 * 10^(3-2) = 18 * 10^1 = 180)
        self.assertEqual(starts_one_ends(3), 180)

    def test_normal_n_4(self):
        # Normal case: n = 4
        # Expected output: 1800 (18 * 10^(4-2) = 18 * 10^2 = 1800)
        self.assertEqual(starts_one_ends(4), 1800)

    def test_normal_n_5(self):
        # Normal case: n = 5
        # Expected output: 18000 (18 * 10^(5-2) = 18 * 10^3 = 18000)
        self.assertEqual(starts_one_ends(5), 18000)

    def test_error_n_zero(self):
        # Error case: n = 0 (n must be positive)
        with self.assertRaises(ValueError):
            starts_one_ends(0)

    def test_error_n_negative(self):
        # Error case: n = -5 (n must be positive)
        with self.assertRaises(ValueError):
            starts_one_ends(-5)

    def test_error_n_float(self):
        # Error case: n = 1.5 (n must be an integer)
        with self.assertRaises(TypeError):
            starts_one_ends(1.5)

    def test_error_n_string(self):
        # Error case: n = "abc" (n must be an integer)
        with self.assertRaises(TypeError):
            starts_one_ends("abc")

    def test_error_n_none(self):
        # Error case: n = None (n must be an integer)
        with self.assertRaises(TypeError):
            starts_one_ends(None)