import unittest
from sut_llm.problem_HumanEval_137 import compare_one

class TestCompareOne(unittest.TestCase):

    def test_int_vs_float_b_larger(self):
        # Test case: integer vs float, float is larger
        self.assertEqual(compare_one(1, 2.5), 2.5)

    def test_int_vs_string_comma_b_larger(self):
        # Test case: integer vs string with comma float, string is larger
        self.assertEqual(compare_one(1, "2,3"), "2,3")

    def test_string_comma_vs_string_int_b_larger(self):
        # Test case: string with comma float vs string integer, string integer is larger
        self.assertEqual(compare_one("5,1", "6"), "6")

    def test_string_int_vs_int_equal(self):
        # Test case: string integer vs integer, values are equal
        self.assertIsNone(compare_one("1", 1))

    def test_float_vs_int_a_larger(self):
        # Test case: float vs integer, float is larger, ensures type preservation
        self.assertEqual(compare_one(3.0, 2), 3.0)

    def test_string_dot_vs_float_a_larger(self):
        # Test case: string with dot float vs float, string is larger, ensures type preservation
        self.assertEqual(compare_one("3.5", 3.0), "3.5")

    def test_int_vs_int_a_larger(self):
        # Test case: integer vs integer, first is larger
        self.assertEqual(compare_one(10, 5), 10)

    def test_float_vs_float_b_larger(self):
        # Test case: float vs float, second is larger
        self.assertEqual(compare_one(7.1, 7.2), 7.2)

    def test_string_comma_vs_string_comma_equal(self):
        # Test case: two strings with comma float, values are equal
        self.assertIsNone(compare_one("8,8", "8,8"))

    def test_negative_string_dot_vs_negative_float_b_larger(self):
        # Test case: negative string with dot float vs negative float, float is larger
        self.assertEqual(compare_one("-1.5", -1.0), -1.0)

if __name__ == '__main__':
    unittest.main()