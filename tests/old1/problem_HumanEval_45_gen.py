import unittest
from sut.problem_HumanEval_45 import triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_1_docstring_example(self):
        self.assertEqual(triangle_area(5, 3), 7.5)

    def test_2_positive_integers(self):
        self.assertEqual(triangle_area(10, 4), 20.0)

    def test_3_floating_point_inputs(self):
        self.assertEqual(triangle_area(2.5, 4.0), 5.0)

    def test_4_zero_base(self):
        self.assertEqual(triangle_area(0, 10), 0.0)

    def test_5_zero_height(self):
        self.assertEqual(triangle_area(10, 0), 0.0)

    def test_6_both_zero(self):
        self.assertEqual(triangle_area(0, 0), 0.0)

    def test_7_large_numbers(self):
        self.assertEqual(triangle_area(1000, 500), 250000.0)

    def test_8_small_floating_point_numbers(self):
        self.assertEqual(triangle_area(0.1, 0.2), 0.01)

    def test_9_mixed_integer_and_float(self):
        self.assertEqual(triangle_area(7, 2.5), 8.75)

    def test_10_another_mixed_integer_and_float(self):
        self.assertEqual(triangle_area(3.0, 5), 7.5)

if __name__ == '__main__':
    unittest.main()