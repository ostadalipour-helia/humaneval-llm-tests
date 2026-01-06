import unittest
from sut.problem_HumanEval_21 import rescale_to_unit

class Test_rescale_to_unit(unittest.TestCase):

    def test_case_0(self):
        self.assertEqual(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]), [0.0, 0.25, 0.5, 0.75, 1.0])

    def test_case_1(self):
        self.assertEqual(rescale_to_unit([-10.0, 0.0, 10.0]), [0.0, 0.5, 1.0])

    def test_case_2(self):
        self.assertEqual(rescale_to_unit([5.0, 4.0, 3.0, 2.0, 1.0]), [1.0, 0.75, 0.5, 0.25, 0.0])

    def test_case_3(self):
        self.assertEqual(rescale_to_unit([10.0, 20.0]), [0.0, 1.0])

    def test_case_4(self):
        with self.assertRaises(ZeroDivisionError):
            rescale_to_unit([5.0, 5.0, 5.0])

    def test_case_5(self):
        self.assertEqual(rescale_to_unit([0.0, 0.5, 1.0]), [0.0, 0.5, 1.0])

    def test_case_6(self):
        with self.assertRaises(ZeroDivisionError):
            rescale_to_unit([1.234, 1.234, 1.234, 1.234])

    def test_case_7(self):
        with self.assertRaises(ZeroDivisionError):
            rescale_to_unit([5.0, 5.0, 5.0])

    def test_case_8(self):
        self.assertEqual(rescale_to_unit([0.0, 0.5, 1.0]), [0.0, 0.5, 1.0])

    def test_case_9(self):
        with self.assertRaises(ZeroDivisionError):
            rescale_to_unit([1.234, 1.234, 1.234, 1.234])