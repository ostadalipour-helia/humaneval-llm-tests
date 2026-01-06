import unittest
from sut.problem_HumanEval_72 import will_it_fly

class Test_will_it_fly(unittest.TestCase):

    def test_case_0(self):
        self.assertEqual(will_it_fly(q=[3, 2, 3], w=9), True)

    def test_case_1(self):
        self.assertEqual(will_it_fly(q=[1, 2], w=5), False)

    def test_case_2(self):
        self.assertEqual(will_it_fly(q=[3, 2, 3], w=1), False)

    def test_case_3(self):
        self.assertEqual(will_it_fly(q=[], w=5), True)

    def test_case_4(self):
        self.assertEqual(will_it_fly(q=[3], w=5), True)

    def test_case_5(self):
        self.assertEqual(will_it_fly(q=[1, 2, 1], w=4), True)

    def test_case_6(self):
        self.assertEqual(will_it_fly(q=[1, 2, 1], w=3), False)

    def test_case_7(self):
        self.assertEqual(will_it_fly(q=[0, 0], w=0), True)

    def test_case_8(self):
        self.assertEqual(will_it_fly(q=[1], w=0), False)

    def test_case_9(self):
        self.assertEqual(will_it_fly(q=[-1, 0, -1], w=-2), True)