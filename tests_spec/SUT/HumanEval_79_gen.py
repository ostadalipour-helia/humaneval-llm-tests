import unittest
from sut.problem_HumanEval_79 import decimal_to_binary

class Test_decimal_to_binary(unittest.TestCase):

    def test_normal_case_15(self):
        self.assertEqual(decimal_to_binary(15), 'db1111db')

    def test_normal_case_32(self):
        self.assertEqual(decimal_to_binary(32), 'db100000db')

    def test_normal_case_10(self):
        self.assertEqual(decimal_to_binary(10), 'db1010db')

    def test_edge_case_zero(self):
        self.assertEqual(decimal_to_binary(0), 'db0db')

    def test_edge_case_one(self):
        self.assertEqual(decimal_to_binary(1), 'db1db')

    def test_edge_case_two(self):
        self.assertEqual(decimal_to_binary(2), 'db10db')

    def test_another_case_15(self):
        self.assertEqual(decimal_to_binary(15), 'db1111db')

    def test_another_case_32(self):
        self.assertEqual(decimal_to_binary(32), 'db100000db')

    def test_another_case_0(self):
        self.assertEqual(decimal_to_binary(0), 'db0db')

    def test_another_case_1(self):
        self.assertEqual(decimal_to_binary(1), 'db1db')