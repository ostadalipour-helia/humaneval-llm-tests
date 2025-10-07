import unittest
from sut_llm.problem_HumanEval_27 import flip_case

class TestFlipCase(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(flip_case('Hello'), 'hELLO')

    def test_empty_string(self):
        self.assertEqual(flip_case(''), '')

    def test_all_lowercase(self):
        self.assertEqual(flip_case('python'), 'PYTHON')

    def test_all_uppercase(self):
        self.assertEqual(flip_case('UNITTEST'), 'unittest')

    def test_mixed_case_with_spaces(self):
        self.assertEqual(flip_case('PyThOn Is FuN'), 'pYtHoN iS fUn')

    def test_string_with_numbers(self):
        self.assertEqual(flip_case('Python3.9'), 'pYTHON3.9')

    def test_string_with_special_chars(self):
        self.assertEqual(flip_case('!@#$Hello_World!@#$'), '!@#$hELLO_wORLD!@#$')

    def test_single_lowercase_char(self):
        self.assertEqual(flip_case('a'), 'A')

    def test_single_uppercase_char(self):
        self.assertEqual(flip_case('Z'), 'z')

    def test_long_mixed_string(self):
        self.assertEqual(flip_case('This Is A LoNg StRiNg WiTh NuMbErS 123 AnD SpEcIaL ChArS !@#'), 'tHIS iS a lOnG sTrInG wItH nUmBeRs 123 aNd sPeCiAl cHaRs !@#')