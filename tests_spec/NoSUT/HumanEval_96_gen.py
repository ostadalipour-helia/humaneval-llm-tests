import unittest
from sut.problem_HumanEval_96 import count_up_to

class Test_count_up_to(unittest.TestCase):
    def test_normal_case_five(self):
        self.assertEqual(count_up_to(5), [2, 3])

    def test_normal_case_eleven(self):
        self.assertEqual(count_up_to(11), [2, 3, 5, 7])

    def test_normal_case_twenty(self):
        self.assertEqual(count_up_to(20), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_edge_case_zero(self):
        self.assertEqual(count_up_to(0), [])

    def test_edge_case_one(self):
        self.assertEqual(count_up_to(1), [])

    def test_edge_case_two(self):
        self.assertEqual(count_up_to(2), [])

    def test_edge_case_three(self):
        self.assertEqual(count_up_to(3), [2])

    def test_edge_case_four(self):
        self.assertEqual(count_up_to(4), [2, 3])

    def test_error_negative_input(self):
        with self.assertRaisesRegex(ValueError, "Input 'n' must be non-negative."):
            count_up_to(-1)

    def test_error_float_input(self):
        with self.assertRaisesRegex(TypeError, "Input 'n' must be an integer."):
            count_up_to(3.5)

    def test_error_string_input(self):
        with self.assertRaisesRegex(TypeError, "Input 'n' must be an integer."):
            count_up_to("abc")