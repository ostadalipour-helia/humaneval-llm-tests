import unittest
from sut.problem_HumanEval_136 import largest_smallest_integers

class Test_largest_smallest_integers(unittest.TestCase):

    def test_case_1(self):
        with self.assertRaises(TypeError) as cm:
            largest_smallest_integers([1, 2, 3, -1, -2, -3])
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_2(self):
        with self.assertRaises(TypeError) as cm:
            largest_smallest_integers([-10, -5, -1, 1, 5, 10])
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_3(self):
        with self.assertRaises(TypeError) as cm:
            largest_smallest_integers([2, 4, 1, 3, 5, 7])
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_4(self):
        with self.assertRaises(TypeError) as cm:
            largest_smallest_integers([-1, -5, -10, -2])
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_5(self):
        with self.assertRaises(TypeError) as cm:
            largest_smallest_integers([])
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_6(self):
        with self.assertRaises(TypeError) as cm:
            largest_smallest_integers([0])
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_7(self):
        with self.assertRaises(TypeError) as cm:
            largest_smallest_integers([0, 0, 0])
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_8(self):
        with self.assertRaises(TypeError) as cm:
            largest_smallest_integers([-1])
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_9(self):
        with self.assertRaises(TypeError) as cm:
            largest_smallest_integers([1])
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")

    def test_case_10(self):
        with self.assertRaises(TypeError) as cm:
            largest_smallest_integers([-5, 0, 5])
        self.assertEqual(str(cm.exception), "'<' not supported between instances of 'str' and 'int'")