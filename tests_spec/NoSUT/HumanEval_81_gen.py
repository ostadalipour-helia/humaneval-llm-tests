import unittest
from sut.problem_HumanEval_81 import numerical_letter_grade

class Test_numerical_letter_grade(unittest.TestCase):
    def test_normal_case_1(self):
        grades = [4.0, 3.0, 1.7, 2.0, 3.5]
        expected_output = ["A+", "B", "C-", "C", "A-"]
        self.assertEqual(numerical_letter_grade(grades), expected_output)

    def test_normal_case_2(self):
        grades = [3.8, 2.5, 1.1, 0.8]
        expected_output = ["A", "B-", "D+", "D"]
        self.assertEqual(numerical_letter_grade(grades), expected_output)

    def test_normal_case_3(self):
        grades = [3.1, 2.1, 0.5]
        expected_output = ["B+", "C+", "D-"]
        self.assertEqual(numerical_letter_grade(grades), expected_output)

    def test_edge_empty_list(self):
        grades = []
        expected_output = []
        self.assertEqual(numerical_letter_grade(grades), expected_output)

    def test_edge_single_gpa_max(self):
        grades = [4.0]
        expected_output = ["A+"]
        self.assertEqual(numerical_letter_grade(grades), expected_output)

    def test_edge_single_gpa_min(self):
        grades = [0.0]
        expected_output = ["E"]
        self.assertEqual(numerical_letter_grade(grades), expected_output)

    def test_edge_boundary_values_d_grades(self):
        # Test boundaries for D-, D, D+
        grades = [0.01, 0.7, 0.71, 1.0, 1.01, 1.3, 1.31]
        expected_output = ["D-", "D-", "D", "D", "D+", "D+", "C-"]
        self.assertEqual(numerical_letter_grade(grades), expected_output)

    def test_edge_boundary_values_a_grades(self):
        # Test boundaries for A-, A, A+
        grades = [3.7, 3.71, 3.99, 4.0, 4.1, 5.0]
        expected_output = ["A-", "A", "A", "A+", "A+", "A+"]
        self.assertEqual(numerical_letter_grade(grades), expected_output)

    def test_error_grades_not_list_none(self):
        with self.assertRaises(TypeError):
            numerical_letter_grade(None)

    def test_error_grades_not_list_string(self):
        with self.assertRaises(TypeError):
            numerical_letter_grade("not a list")

    def test_error_list_contains_non_numeric(self):
        with self.assertRaises(TypeError):
            numerical_letter_grade([4.0, "invalid", 3.0])

    def test_error_list_contains_negative_gpa(self):
        with self.assertRaises(ValueError):
            numerical_letter_grade([4.0, -1.0, 3.0])