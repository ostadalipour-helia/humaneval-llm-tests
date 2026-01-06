import unittest
from sut.problem_HumanEval_116 import sort_array

class Test_sort_array(unittest.TestCase):

    def test_case_1(self):
        with self.assertRaises(TypeError) as cm:
            sort_array("[1, 5, 2, 3, 4]")
        self.assertEqual(str(cm.exception), "'str' object cannot be interpreted as an integer")

    def test_case_2(self):
        with self.assertRaises(TypeError) as cm:
            sort_array("[-2, -3, -4, -5, -6]")
        self.assertEqual(str(cm.exception), "'str' object cannot be interpreted as an integer")

    def test_case_3(self):
        with self.assertRaises(TypeError) as cm:
            sort_array("[1, 0, 2, 3, 4]")
        self.assertEqual(str(cm.exception), "'str' object cannot be interpreted as an integer")

    def test_case_4(self):
        with self.assertRaises(TypeError) as cm:
            sort_array("[10, -5, 0, 3, -8, 7]")
        self.assertEqual(str(cm.exception), "'str' object cannot be interpreted as an integer")

    def test_case_5(self):
        with self.assertRaises(TypeError) as cm:
            sort_array("[7, 2, 7, 1, 4, 2]")
        self.assertEqual(str(cm.exception), "'str' object cannot be interpreted as an integer")

    def test_case_6(self):
        with self.assertRaises(TypeError) as cm:
            sort_array("[]")
        self.assertEqual(str(cm.exception), "'str' object cannot be interpreted as an integer")

    def test_case_7(self):
        with self.assertRaises(TypeError) as cm:
            sort_array("[42]")
        self.assertEqual(str(cm.exception), "'str' object cannot be interpreted as an integer")

    def test_case_8(self):
        with self.assertRaises(TypeError) as cm:
            sort_array("[5, 5, 5, 5]")
        self.assertEqual(str(cm.exception), "'str' object cannot be interpreted as an integer")

    def test_case_9(self):
        with self.assertRaises(TypeError) as cm:
            sort_array("[1, 2, 3, 4, 5]")
        self.assertEqual(str(cm.exception), "'str' object cannot be interpreted as an integer")

    def test_case_10(self):
        with self.assertRaises(TypeError) as cm:
            sort_array("[5, 4, 3, 2, 1]")
        self.assertEqual(str(cm.exception), "'str' object cannot be interpreted as an integer")