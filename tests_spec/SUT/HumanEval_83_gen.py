import unittest
from sut.problem_HumanEval_83 import starts_one_ends

class Test_starts_one_ends(unittest.TestCase):

    def test_computed_case_1(self):
        with self.assertRaises(TypeError) as cm:
            starts_one_ends("2")
        self.assertEqual(str(cm.exception), "unsupported operand type(s) for -: 'str' and 'int'")

    def test_computed_case_2(self):
        with self.assertRaises(TypeError) as cm:
            starts_one_ends("3")
        self.assertEqual(str(cm.exception), "unsupported operand type(s) for -: 'str' and 'int'")

    def test_computed_case_3(self):
        with self.assertRaises(TypeError) as cm:
            starts_one_ends("1")
        self.assertEqual(str(cm.exception), "unsupported operand type(s) for -: 'str' and 'int'")

    def test_computed_case_1_repeat_1(self):
        with self.assertRaises(TypeError) as cm:
            starts_one_ends("2")
        self.assertEqual(str(cm.exception), "unsupported operand type(s) for -: 'str' and 'int'")

    def test_computed_case_2_repeat_1(self):
        with self.assertRaises(TypeError) as cm:
            starts_one_ends("3")
        self.assertEqual(str(cm.exception), "unsupported operand type(s) for -: 'str' and 'int'")

    def test_computed_case_3_repeat_1(self):
        with self.assertRaises(TypeError) as cm:
            starts_one_ends("1")
        self.assertEqual(str(cm.exception), "unsupported operand type(s) for -: 'str' and 'int'")

    def test_computed_case_1_repeat_2(self):
        with self.assertRaises(TypeError) as cm:
            starts_one_ends("2")
        self.assertEqual(str(cm.exception), "unsupported operand type(s) for -: 'str' and 'int'")

    def test_computed_case_2_repeat_2(self):
        with self.assertRaises(TypeError) as cm:
            starts_one_ends("3")
        self.assertEqual(str(cm.exception), "unsupported operand type(s) for -: 'str' and 'int'")

    def test_computed_case_3_repeat_2(self):
        with self.assertRaises(TypeError) as cm:
            starts_one_ends("1")
        self.assertEqual(str(cm.exception), "unsupported operand type(s) for -: 'str' and 'int'")

    def test_computed_case_1_repeat_3(self):
        with self.assertRaises(TypeError) as cm:
            starts_one_ends("2")
        self.assertEqual(str(cm.exception), "unsupported operand type(s) for -: 'str' and 'int'")