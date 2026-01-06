import unittest
from sut.problem_HumanEval_47 import median

class Test_median(unittest.TestCase):

    def test_case_0(self):
        self.assertEqual(median([3, 1, 2, 4, 5]), ',')

    def test_case_1(self):
        self.assertEqual(median([-10, 4, 6, 10, 20, 1000]), '0')

    def test_case_2(self):
        with self.assertRaises(TypeError):
            median([1.0, 2.5, 3.0, 4.5])

    def test_case_3(self):
        with self.assertRaises(TypeError):
            median([10, 20, 30, 40, 50])

    def test_case_4(self):
        with self.assertRaises(TypeError):
            median([1, 1, 2, 3, 4, 5])

    def test_case_5(self):
        self.assertEqual(median([7]), '[')

    def test_case_6(self):
        with self.assertRaises(TypeError):
            median([10, 20])

    def test_case_7(self):
        with self.assertRaises(TypeError):
            median([5, 5, 5, 5])

    def test_case_8(self):
        self.assertEqual(median([0, 0, 0]), '0')

    def test_case_9(self):
        with self.assertRaises(TypeError):
            median([-1, -2, -3])