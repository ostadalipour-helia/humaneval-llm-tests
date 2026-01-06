import unittest
from sut.problem_HumanEval_159 import eat

class Test_eat(unittest.TestCase):

    def test_case_1(self):
        # Normal case: Enough carrots are available to satisfy the need.
        self.assertEqual(eat(number=5, need=6, remaining=10), [11, 4])

    def test_case_2(self):
        # Normal case: Enough carrots are available, with some left over.
        self.assertEqual(eat(number=4, need=8, remaining=9), [12, 1])

    def test_case_3(self):
        # Normal case: Initial eaten carrots is zero, enough remaining.
        self.assertEqual(eat(number=0, need=5, remaining=10), [5, 5])

    def test_case_4(self):
        # Edge case: Exactly enough carrots are available to satisfy the need, leaving zero.
        self.assertEqual(eat(number=1, need=10, remaining=10), [11, 0])

    def test_case_5(self):
        # Edge case: Not enough carrots are available; all remaining carrots are eaten, leaving zero.
        self.assertEqual(eat(number=2, need=11, remaining=5), [7, 0])

    def test_case_6(self):
        # Edge case: All input parameters are zero.
        self.assertEqual(eat(number=0, need=0, remaining=0), [0, 0])

    def test_case_7(self):
        # Edge case: All input parameters are at their maximum allowed value, exactly enough remaining.
        self.assertEqual(eat(number=1000, need=1000, remaining=1000), [2000, 0])

    def test_case_8(self):
        # Edge case: The rabbit needs to eat zero additional carrots.
        self.assertEqual(eat(number=10, need=0, remaining=5), [10, 5])

    def test_case_9(self):
        # Edge case: There are zero remaining carrots.
        self.assertEqual(eat(number=10, need=5, remaining=0), [10, 0])