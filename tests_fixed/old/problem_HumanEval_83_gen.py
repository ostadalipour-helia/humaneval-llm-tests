import unittest
from sut_llm.problem_HumanEval_83 import starts_one_ends

class TestStartsOneEnds(unittest.TestCase):

    def test_n_equals_1(self):
        self.assertEqual(starts_one_ends(1), 1)

    def test_n_equals_2(self):
        self.assertEqual(starts_one_ends(2), 18)

    def test_n_equals_3(self):
        self.assertEqual(starts_one_ends(3), 180)

    def test_n_equals_4(self):
        self.assertEqual(starts_one_ends(4), 1800)

    def test_n_equals_5(self):
        self.assertEqual(starts_one_ends(5), 18000)

    def test_n_equals_6(self):
        self.assertEqual(starts_one_ends(6), 180000)

    def test_n_equals_7(self):
        self.assertEqual(starts_one_ends(7), 1800000)

    def test_n_equals_8(self):
        self.assertEqual(starts_one_ends(8), 18000000)

    def test_n_equals_9(self):
        self.assertEqual(starts_one_ends(9), 180000000)

    def test_n_equals_10(self):
        self.assertEqual(starts_one_ends(10), 1800000000)