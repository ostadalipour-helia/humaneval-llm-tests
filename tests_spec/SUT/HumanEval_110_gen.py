import unittest
from sut.problem_HumanEval_110 import exchange

class Test_exchange(unittest.TestCase):

    def test_normal_case_1(self):
        self.assertEqual(exchange(lst1=[1, 2, 3, 4], lst2=[1, 2, 3, 4]), 'YES')

    def test_normal_case_2(self):
        self.assertEqual(exchange(lst1=[1, 2, 3, 4], lst2=[1, 5, 3, 4]), 'NO')

    def test_normal_case_3(self):
        self.assertEqual(exchange(lst1=[2, 4, 6], lst2=[1, 3, 5]), 'YES')

    def test_normal_case_4(self):
        self.assertEqual(exchange(lst1=[1, 3, 5], lst2=[2, 4, 6]), 'YES')

    def test_edge_case_1(self):
        self.assertEqual(exchange(lst1=[1], lst2=[2]), 'YES')

    def test_edge_case_2(self):
        self.assertEqual(exchange(lst1=[1], lst2=[3]), 'NO')

    def test_edge_case_3(self):
        self.assertEqual(exchange(lst1=[2], lst2=[1]), 'YES')

    def test_edge_case_4(self):
        self.assertEqual(exchange(lst1=[1, 3], lst2=[2]), 'NO')

    def test_edge_case_5(self):
        self.assertEqual(exchange(lst1=[2, 4], lst2=[1, 3]), 'YES')

    def test_additional_case_from_spec(self):
        self.assertEqual(exchange(lst1=[1, 2, 3, 4], lst2=[1, 2, 3, 4]), 'YES')