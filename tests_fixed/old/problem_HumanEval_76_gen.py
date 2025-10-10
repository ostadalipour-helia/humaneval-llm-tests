import unittest
from sut_llm.problem_HumanEval_76 import is_simple_power

class TestIsSimplePower(unittest.TestCase):

    def test_example_1_4(self):
        self.assertTrue(is_simple_power(1, 4))

    def test_example_2_2(self):
        self.assertTrue(is_simple_power(2, 2))

    def test_example_8_2(self):
        self.assertTrue(is_simple_power(8, 2))

    def test_example_3_2(self):
        self.assertFalse(is_simple_power(3, 2))

    def test_example_3_1(self):
        self.assertFalse(is_simple_power(3, 1))

    def test_example_5_3(self):
        self.assertFalse(is_simple_power(5, 3))

    def test_large_power(self):
        self.assertTrue(is_simple_power(64, 4))

    def test_another_large_power(self):
        self.assertTrue(is_simple_power(100, 10))

    def test_x_is_one_n_is_zero(self):
        self.assertTrue(is_simple_power(1, 0))

    def test_x_is_zero_n_is_zero(self):
        self.assertTrue(is_simple_power(0, 0))

if __name__ == '__main__':
    unittest.main()