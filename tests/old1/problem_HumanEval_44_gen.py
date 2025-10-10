import unittest
from sut.problem_HumanEval_44 import change_base

class TestChangeBase(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(change_base(8, 3), '22')

    def test_example_2(self):
        self.assertEqual(change_base(8, 2), '1000')

    def test_example_3(self):
        self.assertEqual(change_base(7, 2), '111')

    def test_zero_to_base_2(self):
        self.assertEqual(change_base(0, 2), '0')

    def test_zero_to_base_9(self):
        self.assertEqual(change_base(0, 9), '0')

    def test_one_to_base_2(self):
        self.assertEqual(change_base(1, 2), '1')

    def test_one_to_base_7(self):
        self.assertEqual(change_base(1, 7), '1')

    def test_decimal_10_to_binary(self):
        self.assertEqual(change_base(10, 2), '1010')

    def test_decimal_15_to_base_4(self):
        self.assertEqual(change_base(15, 4), '33')

    def test_decimal_25_to_base_5(self):
        self.assertEqual(change_base(25, 5), '100')