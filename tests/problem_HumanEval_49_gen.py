import unittest
from sut.problem_HumanEval_49 import modp

class TestModp(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(modp(3, 5), 3)

    def test_example_2(self):
        self.assertEqual(modp(1101, 101), 2)

    def test_example_3_zero_n(self):
        self.assertEqual(modp(0, 101), 1)

    def test_example_4(self):
        self.assertEqual(modp(3, 11), 8)

    def test_example_5_large_n_mod_p(self):
        self.assertEqual(modp(100, 101), 1)

    def test_n_is_one(self):
        self.assertEqual(modp(1, 5), 2)

    def test_n_is_four_small_p(self):
        self.assertEqual(modp(4, 5), 1)

    def test_modulo_two(self):
        self.assertEqual(modp(5, 2), 0)

    def test_larger_n_and_p(self):
        self.assertEqual(modp(6, 7), 1)

    def test_n_is_ten_small_p(self):
        self.assertEqual(modp(10, 3), 1)

if __name__ == '__main__':
    unittest.main()