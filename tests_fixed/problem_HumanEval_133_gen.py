import unittest
from sut_llm.problem_HumanEval_133 import sum_squares

class TestSumSquares(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(sum_squares([1, 2, 3]), 14)

    def test_example_2(self):
        self.assertEqual(sum_squares([1, 4, 9]), 98)

    def test_example_3(self):
        self.assertEqual(sum_squares([1, 3, 5, 7]), 84)

    def test_example_4(self):
        self.assertEqual(sum_squares([1.4, 4.2, 0]), 29)

    def test_example_5(self):
        self.assertEqual(sum_squares([-2.4, 1, 1]), 6)

    def test_empty_list(self):
        self.assertEqual(sum_squares([]), 0)

    def test_single_integer(self):
        self.assertEqual(sum_squares([5]), 25)

    def test_single_float(self):
        self.assertEqual(sum_squares([3.7]), 16)

    def test_mixed_negative_floats_and_integers(self):
        self.assertEqual(sum_squares([-1.1, -0.5, 2]), 5)

    def test_all_zeros_mixed_types(self):
        self.assertEqual(sum_squares([0.0, 0, -0.1]), 0)

if __name__ == '__main__':
    unittest.main()