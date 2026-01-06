import unittest
from sut.problem_HumanEval_154 import cycpattern_check

class Test_cycpattern_check(unittest.TestCase):

    def test_normal_case_no_substring(self):
        self.assertEqual(cycpattern_check("abcd", "abd"), False)

    def test_normal_case_direct_substring(self):
        self.assertEqual(cycpattern_check("hello", "ell"), True)

    def test_normal_case_no_rotation_substring(self):
        self.assertEqual(cycpattern_check("whassup", "psus"), False)

    def test_normal_case_rotation_is_substring(self):
        self.assertEqual(cycpattern_check("abab", "baa"), True)

    def test_normal_case_another_no_rotation(self):
        self.assertEqual(cycpattern_check("efef", "eeff"), False)

    def test_normal_case_another_rotation_is_substring(self):
        self.assertEqual(cycpattern_check("himenss", "simen"), True)

    def test_edge_case_b_longer_than_a(self):
        self.assertEqual(cycpattern_check("abc", "abcd"), False)

    def test_edge_case_empty_b(self):
        self.assertEqual(cycpattern_check("test", ""), True)

    def test_edge_case_empty_a(self):
        self.assertEqual(cycpattern_check("", "abc"), False)

    def test_edge_case_both_empty(self):
        self.assertEqual(cycpattern_check("", ""), True)

if __name__ == '__main__':
    unittest.main()