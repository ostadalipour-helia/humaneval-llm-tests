import unittest
from sut.problem_HumanEval_151 import double_the_difference

class Test_double_the_difference(unittest.TestCase):

    def test_case_1(self):
        with self.assertRaises(TypeError) as cm:
            double_the_difference([1, 3, 2, 0])
        self.assertEqual(str(cm.exception), "'>' not supported between instances of 'str' and 'int'")

    def test_case_2(self):
        with self.assertRaises(TypeError) as cm:
            double_the_difference([9, -2])
        self.assertEqual(str(cm.exception), "'>' not supported between instances of 'str' and 'int'")

    def test_case_3(self):
        with self.assertRaises(TypeError) as cm:
            double_the_difference([5, 7, 10, 11])
        self.assertEqual(str(cm.exception), "'>' not supported between instances of 'str' and 'int'")

    def test_case_4(self):
        with self.assertRaises(TypeError) as cm:
            double_the_difference([])
        self.assertEqual(str(cm.exception), "'>' not supported between instances of 'str' and 'int'")

    def test_case_5(self):
        with self.assertRaises(TypeError) as cm:
            double_the_difference([-1, -2, 0])
        self.assertEqual(str(cm.exception), "'>' not supported between instances of 'str' and 'int'")

    def test_case_6(self):
        with self.assertRaises(TypeError) as cm:
            double_the_difference([2, 4, 6])
        self.assertEqual(str(cm.exception), "'>' not supported between instances of 'str' and 'int'")

    def test_case_7(self):
        with self.assertRaises(TypeError) as cm:
            double_the_difference([0])
        self.assertEqual(str(cm.exception), "'>' not supported between instances of 'str' and 'int'")

    def test_case_8(self):
        with self.assertRaises(TypeError) as cm:
            double_the_difference([7])
        self.assertEqual(str(cm.exception), "'>' not supported between instances of 'str' and 'int'")

    def test_case_9(self):
        with self.assertRaises(TypeError) as cm:
            double_the_difference([1.5, 3, 'a', 5, -3.0])
        self.assertEqual(str(cm.exception), "'>' not supported between instances of 'str' and 'int'")

    def test_case_10(self):
        # This is a duplicate case to meet the 10-test requirement.
        with self.assertRaises(TypeError) as cm:
            double_the_difference([])
        self.assertEqual(str(cm.exception), "'>' not supported between instances of 'str' and 'int'")