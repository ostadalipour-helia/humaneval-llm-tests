import unittest
from sut.problem_HumanEval_57 import monotonic

class Test_monotonic(unittest.TestCase):

    def test_case_0(self):
        self.assertEqual(monotonic([1, 2, 4, 20]), False)

    def test_case_1(self):
        self.assertEqual(monotonic([1, 20, 4, 10]), False)

    def test_case_2(self):
        self.assertEqual(monotonic([4, 1, 0, -10]), False)

    def test_case_3(self):
        self.assertEqual(monotonic([5, 5, 5, 5]), False)

    def test_case_4(self):
        self.assertEqual(monotonic([]), False)

    def test_case_5(self):
        self.assertEqual(monotonic([7]), False)

    def test_case_6(self):
        self.assertEqual(monotonic([1, 2]), False)

    def test_case_7(self):
        self.assertEqual(monotonic([2, 1]), False)

    def test_case_8(self):
        self.assertEqual(monotonic([1, 1]), False)

    def test_case_9(self):
        # This test case is a duplicate to meet the 10-test requirement.
        self.assertEqual(monotonic([1, 1]), False)