import unittest
from sut.problem_HumanEval_155 import even_odd_count

class Test_even_odd_count(unittest.TestCase):

    def test_normal_case_1(self):
        self.assertEqual(even_odd_count(123), (1, 2))

    def test_normal_case_2(self):
        self.assertEqual(even_odd_count(45678), (3, 2))

    def test_normal_case_3(self):
        self.assertEqual(even_odd_count(100), (2, 1))

    def test_edge_case_negative(self):
        self.assertEqual(even_odd_count(-12), (1, 1))

    def test_edge_case_zero(self):
        self.assertEqual(even_odd_count(0), (1, 0))

    def test_edge_case_single_odd(self):
        self.assertEqual(even_odd_count(5), (0, 1))

    def test_edge_case_single_even(self):
        self.assertEqual(even_odd_count(8), (1, 0))

    def test_edge_case_all_even(self):
        self.assertEqual(even_odd_count(246), (3, 0))

    def test_edge_case_all_odd(self):
        self.assertEqual(even_odd_count(135), (0, 3))

    def test_edge_case_large_negative(self):
        self.assertEqual(even_odd_count(-987654321), (4, 5))

if __name__ == '__main__':
    unittest.main()