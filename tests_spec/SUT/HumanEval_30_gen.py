import unittest
from sut.problem_HumanEval_30 import get_positive

class Test_get_positive(unittest.TestCase):

    def test_mixed_positive_and_negative_integers(self):
        l = [-1, 2, -4, 5, 6]
        with self.assertRaises(TypeError):
            get_positive(l)

    def test_mixed_with_positive_negative_zero(self):
        l = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
        with self.assertRaises(TypeError):
            get_positive(l)

    def test_empty_list(self):
        l = []
        with self.assertRaises(TypeError):
            get_positive(l)

    def test_all_positive_numbers(self):
        l = [1, 2, 3, 4]
        with self.assertRaises(TypeError):
            get_positive(l)

    def test_all_negative_numbers(self):
        l = [-1, -2, -3, -4]
        with self.assertRaises(TypeError):
            get_positive(l)

    def test_all_zeros(self):
        l = [0, 0, 0]
        with self.assertRaises(TypeError):
            get_positive(l)

    def test_mix_of_positive_negative_zero(self):
        l = [0, 1, -1, 0, 2, -2]
        with self.assertRaises(TypeError):
            get_positive(l)

    def test_floating_point_numbers(self):
        l = [1.5, -2.0, 3.14, 0.0, 0.5]
        with self.assertRaises(TypeError):
            get_positive(l)

    def test_input_is_none(self):
        l = None
        with self.assertRaises(TypeError):
            get_positive(l)

    def test_input_is_string(self):
        l = 'not_a_list'
        with self.assertRaises(TypeError):
            get_positive(l)