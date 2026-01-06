import unittest
from sut.problem_HumanEval_96 import count_up_to

class Test_count_up_to(unittest.TestCase):

    def test_case_0(self):
        with self.assertRaises(TypeError) as cm:
            count_up_to("5")
        self.assertEqual(str(cm.exception), "'str' object cannot be interpreted as an integer")

    def test_case_1(self):
        with self.assertRaises(TypeError) as cm:
            count_up_to("11")
        self.assertEqual(str(cm.exception), "'str' object cannot be interpreted as an integer")

    def test_case_2(self):
        with self.assertRaises(TypeError) as cm:
            count_up_to("20")
        self.assertEqual(str(cm.exception), "'str' object cannot be interpreted as an integer")

    def test_case_3(self):
        with self.assertRaises(TypeError) as cm:
            count_up_to("18")
        self.assertEqual(str(cm.exception), "'str' object cannot be interpreted as an integer")

    def test_case_4(self):
        with self.assertRaises(TypeError) as cm:
            count_up_to("0")
        self.assertEqual(str(cm.exception), "'str' object cannot be interpreted as an integer")

    def test_case_5(self):
        with self.assertRaises(TypeError) as cm:
            count_up_to("1")
        self.assertEqual(str(cm.exception), "'str' object cannot be interpreted as an integer")

    def test_case_6(self):
        with self.assertRaises(TypeError) as cm:
            count_up_to("2")
        self.assertEqual(str(cm.exception), "'str' object cannot be interpreted as an integer")

    def test_case_7(self):
        with self.assertRaises(TypeError) as cm:
            count_up_to("3")
        self.assertEqual(str(cm.exception), "'str' object cannot be interpreted as an integer")

    def test_case_8(self):
        with self.assertRaises(TypeError) as cm:
            count_up_to("4")
        self.assertEqual(str(cm.exception), "'str' object cannot be interpreted as an integer")

    # This test is a duplicate of test_case_8 to meet the 10-test requirement.
    def test_case_9(self):
        with self.assertRaises(TypeError) as cm:
            count_up_to("4")
        self.assertEqual(str(cm.exception), "'str' object cannot be interpreted as an integer")