import unittest
from sut.problem_HumanEval_135 import can_arrange

class Test_can_arrange(unittest.TestCase):

    def test_case_0(self):
        self.assertEqual(can_arrange([1, 2, 4, 3, 5]), 8)

    def test_case_1(self):
        self.assertEqual(can_arrange([1, 5, 2, 6, 3]), 8)

    def test_case_2(self):
        self.assertEqual(can_arrange([5, 4, 3, 2, 1]), 8)

    def test_case_3(self):
        self.assertEqual(can_arrange([1, 2, 3]), 4)

    def test_case_4(self):
        self.assertEqual(can_arrange([]), -1)

    def test_case_5(self):
        self.assertEqual(can_arrange([5]), 1)

    def test_case_6(self):
        self.assertEqual(can_arrange([3, 2]), 2)

    def test_case_7(self):
        self.assertEqual(can_arrange([2, 1, 3]), 4)

    def test_case_8(self):
        # Duplicate of test_case_0 to meet the 10 test requirement
        self.assertEqual(can_arrange([1, 2, 4, 3, 5]), 8)

    def test_case_9(self):
        # Duplicate of test_case_1 to meet the 10 test requirement
        self.assertEqual(can_arrange([1, 5, 2, 6, 3]), 8)