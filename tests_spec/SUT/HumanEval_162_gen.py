import unittest
from sut.problem_HumanEval_162 import string_to_md5

class Test_string_to_md5(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(string_to_md5("Hello world"), '3e25960a79dbc69b674cd4ec67a72c62')

    def test_case_2(self):
        self.assertEqual(string_to_md5("Python"), 'a7f5f35426b927411fc9231b56382173')

    def test_case_3(self):
        self.assertEqual(string_to_md5("The quick brown fox jumps over the lazy dog"), '9e107d9d372bb6826bd81d3542a419d6')

    def test_case_4(self):
        self.assertIsNone(string_to_md5(""))

    def test_case_5(self):
        self.assertEqual(string_to_md5("a"), '0cc175b9c0f1b6a831c399e269772661')

    def test_case_6(self):
        self.assertEqual(string_to_md5(" "), '7215ee9c7d9dc229d2921a40e899ec5f')

    def test_case_7(self):
        self.assertEqual(string_to_md5("1234567890"), 'e807f1fcf82d132f9bb018ca6738a19f')

    def test_case_8(self):
        self.assertEqual(string_to_md5("!@#$%^&*()"), '05b28d17a7b6e7024b6e5d8cc43a8bf7')

    def test_case_9(self):
        self.assertEqual(string_to_md5("Hello world"), '3e25960a79dbc69b674cd4ec67a72c62')

    def test_case_10(self):
        self.assertEqual(string_to_md5("Python"), 'a7f5f35426b927411fc9231b56382173')