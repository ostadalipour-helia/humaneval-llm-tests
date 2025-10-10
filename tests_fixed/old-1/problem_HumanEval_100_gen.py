import unittest
from sut_llm.problem_HumanEval_100 import make_a_pile

class TestMakeAPile(unittest.TestCase):

    def test_n_is_1(self):
        self.assertEqual(make_a_pile(1), [1])

    def test_n_is_2(self):
        self.assertEqual(make_a_pile(2), [2, 4])

    def test_n_is_3_from_docstring(self):
        self.assertEqual(make_a_pile(3), [3, 5, 7])

    def test_n_is_4(self):
        self.assertEqual(make_a_pile(4), [4, 6, 8, 10])

    def test_n_is_5_odd(self):
        self.assertEqual(make_a_pile(5), [5, 7, 9, 11, 13])

    def test_n_is_6_even(self):
        self.assertEqual(make_a_pile(6), [6, 8, 10, 12, 14, 16])

    def test_n_is_7_odd(self):
        self.assertEqual(make_a_pile(7), [7, 9, 11, 13, 15, 17, 19])

    def test_n_is_8_even(self):
        self.assertEqual(make_a_pile(8), [8, 10, 12, 14, 16, 18, 20, 22])

    def test_n_is_9_odd_larger(self):
        self.assertEqual(make_a_pile(9), [9, 11, 13, 15, 17, 19, 21, 23, 25])

    def test_n_is_10_even_larger(self):
        self.assertEqual(make_a_pile(10), [10, 12, 14, 16, 18, 20, 22, 24, 26, 28])