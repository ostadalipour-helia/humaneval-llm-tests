import unittest
from sut_llm.problem_HumanEval_15 import string_sequence

class TestStringSequence(unittest.TestCase):

    def test_case_0(self):
        self.assertEqual(string_sequence(0), '0')

    def test_case_1(self):
        self.assertEqual(string_sequence(1), '0 1')

    def test_case_2(self):
        self.assertEqual(string_sequence(2), '0 1 2')

    def test_case_3(self):
        self.assertEqual(string_sequence(3), '0 1 2 3')

    def test_case_4(self):
        self.assertEqual(string_sequence(5), '0 1 2 3 4 5')

    def test_case_5(self):
        self.assertEqual(string_sequence(7), '0 1 2 3 4 5 6 7')

    def test_case_6(self):
        self.assertEqual(string_sequence(9), '0 1 2 3 4 5 6 7 8 9')

    def test_case_7(self):
        self.assertEqual(string_sequence(10), '0 1 2 3 4 5 6 7 8 9 10')

    def test_case_8(self):
        self.assertEqual(string_sequence(15), '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15')

    def test_case_9(self):
        self.assertEqual(string_sequence(20), '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20')

if __name__ == '__main__':
    unittest.main()