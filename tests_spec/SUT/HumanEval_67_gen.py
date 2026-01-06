import unittest
from sut.problem_HumanEval_67 import fruit_distribution

class Test_fruit_distribution(unittest.TestCase):

    def test_normal_case_1(self):
        self.assertEqual(fruit_distribution(s="5 apples and 6 oranges", n=19), 8)

    def test_normal_case_2(self):
        self.assertEqual(fruit_distribution(s="0 apples and 1 oranges", n=3), 2)

    def test_normal_case_3(self):
        self.assertEqual(fruit_distribution(s="2 apples and 3 oranges", n=100), 95)

    def test_normal_case_4(self):
        self.assertEqual(fruit_distribution(s="100 apples and 1 oranges", n=120), 19)

    def test_edge_case_1(self):
        self.assertEqual(fruit_distribution(s="0 apples and 0 oranges", n=5), 5)

    def test_edge_case_2(self):
        self.assertEqual(fruit_distribution(s="10 apples and 20 oranges", n=30), 0)

    def test_edge_case_3(self):
        self.assertEqual(fruit_distribution(s="1 apples and 0 oranges", n=1), 0)

    def test_edge_case_4(self):
        self.assertEqual(fruit_distribution(s="999999 apples and 1 oranges", n=1000001), 1)

    def test_additional_case_1(self):
        self.assertEqual(fruit_distribution(s="5 apples and 6 oranges", n=19), 8)

    def test_additional_case_2(self):
        self.assertEqual(fruit_distribution(s="0 apples and 1 oranges", n=3), 2)