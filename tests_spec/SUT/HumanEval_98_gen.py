import unittest
from sut.problem_HumanEval_98 import count_upper

class Test_count_upper(unittest.TestCase):

    def test_normal_case_1(self):
        self.assertEqual(count_upper('aBCdEf'), 1)

    def test_normal_case_2(self):
        self.assertEqual(count_upper('abcdefg'), 0)

    def test_normal_case_3(self):
        self.assertEqual(count_upper('dBBE'), 0)

    def test_normal_case_4(self):
        self.assertEqual(count_upper('AEIOU'), 3)

    def test_normal_case_5(self):
        self.assertEqual(count_upper('Python'), 0)

    def test_normal_case_6(self):
        self.assertEqual(count_upper('HELLOworld'), 1)

    def test_edge_case_empty_string(self):
        self.assertEqual(count_upper(''), 0)

    def test_edge_case_single_upper_vowel(self):
        self.assertEqual(count_upper('A'), 1)

    def test_edge_case_single_lower_vowel(self):
        self.assertEqual(count_upper('a'), 0)

    def test_edge_case_single_upper_consonant(self):
        self.assertEqual(count_upper('B'), 0)