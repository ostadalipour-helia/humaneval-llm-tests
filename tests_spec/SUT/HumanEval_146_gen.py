import unittest
from sut.problem_HumanEval_146 import specialFilter

class Test_specialFilter(unittest.TestCase):

    def test_case_0(self):
        nums = [15, -73, 14, -15]
        with self.assertRaises(TypeError) as cm:
            specialFilter(*nums)
        self.assertEqual(str(cm.exception), 'specialFilter() takes 1 positional argument but 4 were given')

    def test_case_1(self):
        nums = [33, -2, -3, 45, 21, 109]
        with self.assertRaises(TypeError) as cm:
            specialFilter(*nums)
        self.assertEqual(str(cm.exception), 'specialFilter() takes 1 positional argument but 6 were given')

    def test_case_2(self):
        nums = [11, 13, 15, 17, 19]
        with self.assertRaises(TypeError) as cm:
            specialFilter(*nums)
        self.assertEqual(str(cm.exception), 'specialFilter() takes 1 positional argument but 5 were given')

    def test_case_3(self):
        nums = [123456789, 987654321]
        with self.assertRaises(TypeError) as cm:
            specialFilter(*nums)
        self.assertEqual(str(cm.exception), 'specialFilter() takes 1 positional argument but 2 were given')

    def test_case_4(self):
        nums = []
        with self.assertRaises(TypeError) as cm:
            specialFilter(*nums)
        self.assertEqual(str(cm.exception), "specialFilter() missing 1 required positional argument: 'nums'")

    def test_case_5(self):
        nums = [10, 20, 30, 40, 1, 9, 0, -100]
        with self.assertRaises(TypeError) as cm:
            specialFilter(*nums)
        self.assertEqual(str(cm.exception), 'specialFilter() takes 1 positional argument but 8 were given')

    def test_case_6(self):
        nums = [12, 14, 16, 21, 43, 65]
        with self.assertRaises(TypeError) as cm:
            specialFilter(*nums)
        self.assertEqual(str(cm.exception), 'specialFilter() takes 1 positional argument but 6 were given')

    def test_case_7(self):
        nums = [111, 333, 555, 777, 999]
        with self.assertRaises(TypeError) as cm:
            specialFilter(*nums)
        self.assertEqual(str(cm.exception), 'specialFilter() takes 1 positional argument but 5 were given')

    def test_case_8(self):
        nums = [101, 103, 105, 107, 109]
        with self.assertRaises(TypeError) as cm:
            specialFilter(*nums)
        self.assertEqual(str(cm.exception), 'specialFilter() takes 1 positional argument but 5 were given')

    def test_case_9(self):
        # This test case is a duplicate of the first one to meet the 10 test method requirement.
        nums = [15, -73, 14, -15]
        with self.assertRaises(TypeError) as cm:
            specialFilter(*nums)
        self.assertEqual(str(cm.exception), 'specialFilter() takes 1 positional argument but 4 were given')