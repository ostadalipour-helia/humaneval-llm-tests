import unittest
from sut.problem_HumanEval_100 import make_a_pile

class Test_make_a_pile(unittest.TestCase):

    def test_normal_case_odd_3(self):
        self.assertListEqual(make_a_pile(3), [3, 5, 7])

    def test_normal_case_even_4(self):
        self.assertListEqual(make_a_pile(4), [4, 6, 8, 10])

    def test_normal_case_odd_5(self):
        self.assertListEqual(make_a_pile(5), [5, 7, 9, 11, 13])

    def test_edge_case_1(self):
        self.assertListEqual(make_a_pile(1), [1])

    def test_edge_case_2(self):
        self.assertListEqual(make_a_pile(2), [2, 4])

    def test_properties_for_input_3(self):
        n = 3
        result = make_a_pile(n)
        self.assertEqual(len(result), n)
        self.assertEqual(result[0], n)
        for i in range(n - 1):
            self.assertEqual(result[i+1], result[i] + 2)
        for item in result:
            self.assertEqual(item % 2, n % 2)

    def test_properties_for_input_4(self):
        n = 4
        result = make_a_pile(n)
        self.assertEqual(len(result), n)
        self.assertEqual(result[0], n)
        for i in range(n - 1):
            self.assertEqual(result[i+1], result[i] + 2)
        for item in result:
            self.assertEqual(item % 2, n % 2)

    def test_properties_for_input_5(self):
        n = 5
        result = make_a_pile(n)
        self.assertEqual(len(result), n)
        self.assertEqual(result[0], n)
        for i in range(n - 1):
            self.assertEqual(result[i+1], result[i] + 2)
        for item in result:
            self.assertEqual(item % 2, n % 2)

    def test_properties_for_input_1(self):
        n = 1
        result = make_a_pile(n)
        self.assertEqual(len(result), n)
        self.assertEqual(result[0], n)
        self.assertEqual(result[0] % 2, n % 2)

    def test_properties_for_input_2(self):
        n = 2
        result = make_a_pile(n)
        self.assertEqual(len(result), n)
        self.assertEqual(result[0], n)
        for i in range(n - 1):
            self.assertEqual(result[i+1], result[i] + 2)
        for item in result:
            self.assertEqual(item % 2, n % 2)