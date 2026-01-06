import unittest
from sut.problem_HumanEval_78 import hex_key

class Test_hex_key(unittest.TestCase):

    def test_case_0(self):
        self.assertEqual(hex_key("AB"), 1)

    def test_case_1(self):
        self.assertEqual(hex_key("1077E"), 2)

    def test_case_2(self):
        self.assertEqual(hex_key("ABED1A33"), 4)

    def test_case_3(self):
        self.assertEqual(hex_key("123456789ABCDEF0"), 6)

    def test_case_4(self):
        self.assertEqual(hex_key("2020"), 2)

    def test_case_5(self):
        self.assertEqual(hex_key(""), 0)

    def test_case_6(self):
        self.assertEqual(hex_key("01468ACEF"), 0)

    def test_case_7(self):
        self.assertEqual(hex_key("2357BD"), 6)

    def test_case_8(self):
        self.assertEqual(hex_key("2"), 1)

    def test_case_9(self):
        self.assertEqual(hex_key("0"), 0)