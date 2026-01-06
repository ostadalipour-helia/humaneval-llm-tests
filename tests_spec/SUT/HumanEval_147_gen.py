import unittest
from sut.problem_HumanEval_147 import get_max_triples

class Test_get_max_triples(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(get_max_triples(5), 1)

    def test_case_2(self):
        self.assertEqual(get_max_triples(8), 11)

    def test_case_3(self):
        self.assertEqual(get_max_triples(1), 0)

    def test_case_4(self):
        self.assertEqual(get_max_triples(2), 0)

    def test_case_5(self):
        self.assertEqual(get_max_triples(3), 0)

    def test_case_6(self):
        self.assertEqual(get_max_triples(4), 1)

    def test_case_7(self):
        self.assertEqual(get_max_triples(5), 1)

    def test_case_8(self):
        self.assertEqual(get_max_triples(8), 11)

    def test_case_9(self):
        self.assertEqual(get_max_triples(1), 0)

    def test_case_10(self):
        self.assertEqual(get_max_triples(2), 0)