import unittest
from sut.problem_HumanEval_34 import unique

class Test_unique(unittest.TestCase):

    def test_normal_case_with_duplicates(self):
        args = [5, 3, 5, 2, 3, 3, 9, 0, 123]
        with self.assertRaises(TypeError) as cm:
            unique(*args)
        self.assertEqual(str(cm.exception), 'unique() takes 1 positional argument but 9 were given')

    def test_normal_case_already_unique_sorted(self):
        args = [1, 2, 3, 4]
        with self.assertRaises(TypeError) as cm:
            unique(*args)
        self.assertEqual(str(cm.exception), 'unique() takes 1 positional argument but 4 were given')

    def test_normal_case_with_negatives(self):
        args = [10, -5, 0, 7, -5]
        with self.assertRaises(TypeError) as cm:
            unique(*args)
        self.assertEqual(str(cm.exception), 'unique() takes 1 positional argument but 5 were given')

    def test_edge_case_empty_list_as_no_args(self):
        with self.assertRaises(TypeError) as cm:
            unique()
        self.assertEqual(str(cm.exception), "unique() missing 1 required positional argument: 'l'")

    def test_edge_case_single_element_as_arg(self):
        # This corresponds to calling unique(*[7]), which is unique(7)
        with self.assertRaises(TypeError) as cm:
            unique(7)
        self.assertEqual(str(cm.exception), "'int' object is not iterable")

    def test_edge_case_all_identical_elements(self):
        args = [4, 4, 4, 4]
        with self.assertRaises(TypeError) as cm:
            unique(*args)
        self.assertEqual(str(cm.exception), 'unique() takes 1 positional argument but 4 were given')

    def test_edge_case_with_strings(self):
        args = ["b", "a", "c", "b"]
        with self.assertRaises(TypeError) as cm:
            unique(*args)
        self.assertEqual(str(cm.exception), 'unique() takes 1 positional argument but 4 were given')

    def test_additional_case_1(self):
        args = [5, 3, 5, 2, 3, 3, 9, 0, 123]
        with self.assertRaises(TypeError) as cm:
            unique(*args)
        self.assertEqual(str(cm.exception), 'unique() takes 1 positional argument but 9 were given')

    def test_additional_case_2(self):
        args = [1, 2, 3, 4]
        with self.assertRaises(TypeError) as cm:
            unique(*args)
        self.assertEqual(str(cm.exception), 'unique() takes 1 positional argument but 4 were given')

    def test_additional_case_3(self):
        args = [10, -5, 0, 7, -5]
        with self.assertRaises(TypeError) as cm:
            unique(*args)
        self.assertEqual(str(cm.exception), 'unique() takes 1 positional argument but 5 were given')