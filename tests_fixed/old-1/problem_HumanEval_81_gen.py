import unittest
from sut_llm.problem_HumanEval_81 import numerical_letter_grade

class TestNumericalLetterGrade(unittest.TestCase):

    def test_01_example_case(self):
        grades = [4.0, 3, 1.7, 2, 3.5]
        expected = ['A+', 'B', 'C-', 'C', 'A-']
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_02_all_a_grades_and_boundaries(self):
        # 4.0 (A+), 3.9 (A), 3.7 (A-), 3.5 (A-), 3.31 (A-)
        grades = [4.0, 3.9, 3.7, 3.5, 3.31]
        expected = ['A+', 'A', 'A-', 'A-', 'A-']
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_03_all_b_grades_and_boundaries(self):
        # 3.3 (B+), 3.1 (B+), 3.0 (B), 2.8 (B), 2.71 (B)
        grades = [3.3, 3.1, 3.0, 2.8, 2.71]
        expected = ['B+', 'B+', 'B', 'B', 'B']
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_04_all_c_grades_and_boundaries(self):
        # 2.7 (B-), 2.5 (B-), 2.3 (C+), 2.1 (C+), 2.0 (C), 1.8 (C), 1.71 (C)
        grades = [2.7, 2.5, 2.3, 2.1, 2.0, 1.8, 1.71]
        expected = ['B-', 'B-', 'C+', 'C+', 'C', 'C', 'C']
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_05_all_d_grades_and_boundaries(self):
        # 1.7 (C-), 1.5 (C-), 1.3 (D+), 1.1 (D+), 1.0 (D), 0.8 (D), 0.71 (D)
        grades = [1.7, 1.5, 1.3, 1.1, 1.0, 0.8, 0.71]
        expected = ['C-', 'C-', 'D+', 'D+', 'D', 'D', 'D']
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_06_all_e_and_d_minus_grades_and_boundaries(self):
        # 0.7 (D-), 0.5 (D-), 0.1 (D-), 0.0 (E)
        grades = [0.7, 0.5, 0.1, 0.0]
        expected = ['D-', 'D-', 'D-', 'E']
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_07_empty_list(self):
        grades = []
        expected = []
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_08_single_grade_a_plus(self):
        grades = [4.0]
        expected = ['A+']
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_09_single_grade_e(self):
        grades = [0.0]
        expected = ['E']
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_10_comprehensive_mixed_grades(self):
        # Covering all grade categories with various values
        grades = [4.0, 3.8, 3.4, 3.1, 2.8, 2.4, 2.1, 1.8, 1.4, 1.1, 0.8, 0.1, 0.0]
        expected = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'E']
        self.assertEqual(numerical_letter_grade(grades), expected)