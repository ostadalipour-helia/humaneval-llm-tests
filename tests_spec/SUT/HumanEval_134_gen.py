import unittest
from sut.problem_HumanEval_134 import check_if_last_char_is_a_letter

class Test_check_if_last_char_is_a_letter(unittest.TestCase):

    def test_normal_case_true_1(self):
        self.assertEqual(check_if_last_char_is_a_letter("apple pi e"), True)

    def test_normal_case_true_2(self):
        self.assertEqual(check_if_last_char_is_a_letter("hello world a"), True)

    def test_normal_case_false_1(self):
        self.assertEqual(check_if_last_char_is_a_letter("apple pie"), False)

    def test_normal_case_false_2(self):
        self.assertEqual(check_if_last_char_is_a_letter("test string"), False)

    def test_trailing_space(self):
        self.assertEqual(check_if_last_char_is_a_letter("test string "), False)

    def test_empty_string(self):
        self.assertEqual(check_if_last_char_is_a_letter(""), False)

    def test_single_letter(self):
        self.assertEqual(check_if_last_char_is_a_letter("a"), True)

    def test_single_space(self):
        self.assertEqual(check_if_last_char_is_a_letter(" "), False)

    def test_space_then_letter(self):
        self.assertEqual(check_if_last_char_is_a_letter(" a"), True)

    def test_two_letters(self):
        self.assertEqual(check_if_last_char_is_a_letter("ab"), False)