import unittest
from sut.problem_HumanEval_161 import solve

class Test_solve(unittest.TestCase):

    def test_normal_case_all_lowercase(self):
        self.assertEqual(solve("ab"), 'AB')

    def test_normal_case_mixed_chars(self):
        self.assertEqual(solve("#a@C"), '#A@c')

    def test_normal_case_sentence(self):
        self.assertEqual(solve("Hello World!"), 'hELLO wORLD!')

    def test_edge_case_no_letters(self):
        self.assertEqual(solve("1234"), '4321')

    def test_edge_case_empty_string(self):
        self.assertEqual(solve(""), '')

    def test_edge_case_single_uppercase(self):
        self.assertEqual(solve("A"), 'a')

    def test_edge_case_single_lowercase(self):
        self.assertEqual(solve("z"), 'Z')

    def test_edge_case_single_non_letter(self):
        self.assertEqual(solve("!"), '!')

    def test_edge_case_mixed_case_and_space(self):
        self.assertEqual(solve("aB cD"), 'Ab Cd')

    def test_another_no_letters_case(self):
        self.assertEqual(solve("!@#$"), "$#@!")