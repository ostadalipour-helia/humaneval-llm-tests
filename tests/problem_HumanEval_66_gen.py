import unittest
from sut.problem_HumanEval_66 import digitSum

class TestDigitSum(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(digitSum(""), 0)

    def test_mixed_case_two_uppercase(self):
        self.assertEqual(digitSum("abAB"), 131) # A=65, B=66

    def test_mixed_case_one_uppercase(self):
        self.assertEqual(digitSum("abcCd"), 67) # C=67

    def test_mixed_case_uppercase_at_end(self):
        self.assertEqual(digitSum("helloE"), 69) # E=69

    def test_mixed_case_non_consecutive_uppercase(self):
        self.assertEqual(digitSum("woArBld"), 131) # A=65, B=66

    def test_mixed_case_another_non_consecutive(self):
        self.assertEqual(digitSum("aAaaaXa"), 153) # A=65, X=88

    def test_all_uppercase_string(self):
        # P=80, Y=89, T=84, H=72, O=79, N=78
        self.assertEqual(digitSum("PYTHON"), 80 + 89 + 84 + 72 + 79 + 78) # 482

    def test_all_lowercase_string(self):
        self.assertEqual(digitSum("abcdefg"), 0)

    def test_string_with_numbers_and_symbols(self):
        self.assertEqual(digitSum("123!@#$"), 0)

    def test_mixed_case_with_spaces_and_symbols(self):
        # H=72, W=87
        self.assertEqual(digitSum(" Hello World! "), 72 + 87) # 159

if __name__ == '__main__':
    unittest.main()