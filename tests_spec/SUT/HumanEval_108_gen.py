import unittest
from sut.problem_HumanEval_108 import count_nums

class Test_count_nums(unittest.TestCase):

    def test_normal_case_1(self):
        arr = [1, 1, 2]
        with self.assertRaises(TypeError):
            count_nums(arr)

    def test_normal_case_2(self):
        arr = [-1, 11, -11]
        with self.assertRaises(TypeError):
            count_nums(arr)

    def test_normal_case_3(self):
        arr = [10, -10, 5]
        with self.assertRaises(TypeError):
            count_nums(arr)

    def test_normal_case_4(self):
        arr = [123, -45, 6]
        with self.assertRaises(TypeError):
            count_nums(arr)

    def test_edge_case_empty(self):
        arr = []
        with self.assertRaises(TypeError):
            count_nums(arr)

    def test_edge_case_zero(self):
        arr = [0]
        with self.assertRaises(TypeError):
            count_nums(arr)

    def test_edge_case_all_negative(self):
        arr = [-1, -2, -3]
        with self.assertRaises(TypeError):
            count_nums(arr)

    def test_edge_case_mixed_with_zero(self):
        arr = [100, -100, 0]
        with self.assertRaises(TypeError):
            count_nums(arr)

    def test_edge_case_large_positive(self):
        arr = [999999999]
        with self.assertRaises(TypeError):
            count_nums(arr)

    def test_edge_case_large_negative(self):
        arr = [-999999999]
        with self.assertRaises(TypeError):
            count_nums(arr)