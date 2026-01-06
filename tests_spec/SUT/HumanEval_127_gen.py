import unittest
from sut.problem_HumanEval_127 import intersection

class Test_intersection(unittest.TestCase):

    def test_case_0(self):
        self.assertEqual(intersection(interval1=[1, 3], interval2=[2, 4]), 'NO')

    def test_case_1(self):
        self.assertEqual(intersection(interval1=[-3, -1], interval2=[-5, 5]), 'YES')

    def test_case_2(self):
        self.assertEqual(intersection(interval1=[1, 10], interval2=[5, 15]), 'YES')

    def test_case_3(self):
        self.assertEqual(intersection(interval1=[7, 11], interval2=[8, 12]), 'YES')

    def test_case_4(self):
        self.assertEqual(intersection(interval1=[7, 11], interval2=[9, 13]), 'YES')

    def test_case_5(self):
        self.assertEqual(intersection(interval1=[1, 2], interval2=[2, 3]), 'NO')

    def test_case_6(self):
        self.assertEqual(intersection(interval1=[1, 2], interval2=[3, 4]), 'NO')

    def test_case_7(self):
        self.assertEqual(intersection(interval1=[1, 5], interval2=[1, 5]), 'NO')

    def test_case_8(self):
        self.assertEqual(intersection(interval1=[-10, 10], interval2=[-5, 5]), 'NO')

    def test_case_9(self):
        self.assertEqual(intersection(interval1=[-1, 1], interval2=[0, 4]), 'NO')