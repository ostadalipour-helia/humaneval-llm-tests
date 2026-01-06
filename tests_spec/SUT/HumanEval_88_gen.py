import unittest
from sut.problem_HumanEval_88 import sort_array

class Test_sort_array(unittest.TestCase):

    def test_normal_case_ascending(self):
        with self.assertRaises(TypeError) as cm:
            sort_array("[2, 4, 3, 0, 1, 5]")
        self.assertIsInstance(cm.exception, TypeError)

    def test_normal_case_descending(self):
        with self.assertRaises(TypeError) as cm:
            sort_array("[2, 4, 3, 0, 1, 5, 6]")
        self.assertIsInstance(cm.exception, TypeError)

    def test_another_normal_ascending(self):
        with self.assertRaises(TypeError) as cm:
            sort_array("[10, 1, 7, 3, 5]")
        self.assertIsInstance(cm.exception, TypeError)

    def test_another_normal_descending(self):
        with self.assertRaises(TypeError) as cm:
            sort_array("[10, 1, 7, 3, 6]")
        self.assertIsInstance(cm.exception, TypeError)

    def test_empty_array(self):
        with self.assertRaises(TypeError) as cm:
            sort_array("[]")
        self.assertIsInstance(cm.exception, TypeError)

    def test_single_element_array(self):
        with self.assertRaises(TypeError) as cm:
            sort_array("[5]")
        self.assertIsInstance(cm.exception, TypeError)

    def test_two_elements_ascending(self):
        with self.assertRaises(TypeError) as cm:
            sort_array("[1, 2]")
        self.assertIsInstance(cm.exception, TypeError)

    def test_two_elements_descending(self):
        with self.assertRaises(TypeError) as cm:
            sort_array("[2, 4]")
        self.assertIsInstance(cm.exception, TypeError)

    def test_identical_elements(self):
        with self.assertRaises(TypeError) as cm:
            sort_array("[3, 3, 3]")
        self.assertIsInstance(cm.exception, TypeError)

    def test_with_zero(self):
        with self.assertRaises(TypeError) as cm:
            sort_array("[0, 10, 5]")
        self.assertIsInstance(cm.exception, TypeError)