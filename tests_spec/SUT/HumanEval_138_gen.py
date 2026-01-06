import unittest
from sut.problem_HumanEval_138 import is_equal_to_sum_even

class Test_is_equal_to_sum_even(unittest.TestCase):

    def test_n_is_8(self):
        with self.assertRaises(TypeError) as cm:
            is_equal_to_sum_even(8)
        self.assertEqual(str(cm.exception), 'not all arguments converted during string formatting')

    def test_n_is_10(self):
        with self.assertRaises(TypeError) as cm:
            is_equal_to_sum_even(10)
        self.assertEqual(str(cm.exception), 'not all arguments converted during string formatting')

    def test_n_is_12(self):
        with self.assertRaises(TypeError) as cm:
            is_equal_to_sum_even(12)
        self.assertEqual(str(cm.exception), 'not all arguments converted during string formatting')

    def test_n_is_20(self):
        with self.assertRaises(TypeError) as cm:
            is_equal_to_sum_even(20)
        self.assertEqual(str(cm.exception), 'not all arguments converted during string formatting')

    def test_n_is_4(self):
        with self.assertRaises(TypeError) as cm:
            is_equal_to_sum_even(4)
        self.assertEqual(str(cm.exception), 'not all arguments converted during string formatting')

    def test_n_is_6(self):
        with self.assertRaises(TypeError) as cm:
            is_equal_to_sum_even(6)
        self.assertEqual(str(cm.exception), 'not all arguments converted during string formatting')

    def test_n_is_7(self):
        with self.assertRaises(TypeError) as cm:
            is_equal_to_sum_even(7)
        self.assertEqual(str(cm.exception), 'not all arguments converted during string formatting')

    def test_n_is_9(self):
        with self.assertRaises(TypeError) as cm:
            is_equal_to_sum_even(9)
        self.assertEqual(str(cm.exception), 'not all arguments converted during string formatting')

    def test_n_is_0(self):
        with self.assertRaises(TypeError) as cm:
            is_equal_to_sum_even(0)
        self.assertEqual(str(cm.exception), 'not all arguments converted during string formatting')

    def test_n_is_minus_2(self):
        with self.assertRaises(TypeError) as cm:
            is_equal_to_sum_even(-2)
        self.assertEqual(str(cm.exception), 'not all arguments converted during string formatting')