import unittest
from sut.problem_HumanEval_81 import numerical_letter_grade

class Test_numerical_letter_grade(unittest.TestCase):

    def test_normal_case_1(self):
        self.assertEqual(numerical_letter_grade([4.0, 3.0, 1.7, 2.0, 3.5]), ['A+', 'B', 'C-', 'C', 'A-'])

    def test_normal_case_2(self):
        self.assertEqual(numerical_letter_grade([3.8, 2.5, 1.1, 0.8]), ['A', 'B-', 'D+', 'D'])

    def test_normal_case_3(self):
        self.assertEqual(numerical_letter_grade([3.1, 2.1, 0.5]), ['B+', 'C+', 'D-'])

    def test_empty_list(self):
        self.assertEqual(numerical_letter_grade([]), [])

    def test_single_element_max(self):
        self.assertEqual(numerical_letter_grade([4.0]), ['A+'])

    def test_single_element_min(self):
        self.assertEqual(numerical_letter_grade([0.0]), ['E'])

    def test_boundary_values(self):
        self.assertEqual(numerical_letter_grade([0.01, 0.7, 0.71, 3.7]), ['D-', 'D-', 'D', 'A-'])

    def test_boundary_above_max(self):
        self.assertEqual(numerical_letter_grade([4.1, 5.0]), ['A', 'A'])

    def test_boundary_just_above_3_7(self):
        self.assertEqual(numerical_letter_grade([3.71]), ['A'])

    def test_boundary_at_0_7(self):
        self.assertEqual(numerical_letter_grade([0.7]), ['D-'])