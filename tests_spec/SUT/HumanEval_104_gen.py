import unittest
from sut.problem_HumanEval_104 import unique_digits

class Test_unique_digits(unittest.TestCase):

    def test_case_0(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])

    def test_case_1(self):
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])

    def test_case_2(self):
        self.assertEqual(unique_digits([1, 3, 5, 7, 9]), [1, 3, 5, 7, 9])

    def test_case_3(self):
        self.assertEqual(unique_digits([135, 246, 791, 802]), [135, 791])

    def test_case_4(self):
        self.assertEqual(unique_digits([]), [])

    def test_case_5(self):
        self.assertEqual(unique_digits([1]), [1])

    def test_case_6(self):
        self.assertEqual(unique_digits([2]), [])

    def test_case_7(self):
        self.assertEqual(unique_digits([11111]), [11111])

    def test_case_8(self):
        self.assertEqual(unique_digits([22222]), [])

    def test_case_9(self):
        self.assertEqual(unique_digits([15, 1, 33, 15]), [1, 15, 15, 33])