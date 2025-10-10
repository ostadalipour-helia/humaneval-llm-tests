import unittest
from sut.problem_HumanEval_81 import numerical_letter_grade

class TestNumericalLetterGrade(unittest.TestCase):

    def test_example_from_docstring(self):
        # Verifies the example provided in the docstring, which clarifies the interpretation of GPA ranges.
        # This test is crucial for establishing the correct logic for boundary conditions (e.g., 3.0 -> 'B', 1.7 -> 'C-').
        grades = [4.0, 3, 1.7, 2, 3.5]
        expected_grades = ['A+', 'B', 'C-', 'C', 'A-']
        self.assertListEqual(numerical_letter_grade(grades), expected_grades)

    def test_empty_list(self):
        # Edge case: Tests the function's behavior with an empty list of GPAs.
        # Ensures the function handles empty input gracefully, returning an empty list.
        grades = []
        expected_grades = []
        self.assertListEqual(numerical_letter_grade(grades), expected_grades)

    def test_single_gpa_a_plus(self):
        # Edge case and Boundary Test: Tests a single GPA that hits the highest exact boundary (4.0).
        # Verifies the 'A+' grade is correctly assigned.
        grades = [4.0]
        expected_grades = ['A+']
        self.assertListEqual(numerical_letter_grade(grades), expected_grades)

    def test_single_gpa_e(self):
        # Edge case and Boundary Test: Tests a single GPA that hits the lowest exact boundary (0.0).
        # Verifies the 'E' grade is correctly assigned.
        grades = [0.0]
        expected_grades = ['E']
        self.assertListEqual(numerical_letter_grade(grades), expected_grades)

    def test_all_grade_upper_boundaries(self):
        # Boundary Test: Tests GPAs that are exactly the upper limit of each grade range (e.g., 3.7 for A-, 3.0 for B).
        # This is critical for catching off-by-one errors if comparison operators (>, >=) are misused.
        grades = [4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0]
        expected_grades = ['A+', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'E']
        self.assertListEqual(numerical_letter_grade(grades), expected_grades)

    def test_all_grade_lower_boundaries_plus_epsilon(self):
        # Boundary Test: Tests GPAs just above the lower limit of each grade range (e.g., 3.7 + epsilon for A).
        # This ensures strict inequality ('>') is correctly applied and differentiates from inclusive boundaries.
        epsilon = 1e-12 # A very small number to test just above the boundary
        grades = [3.7 + epsilon, 3.3 + epsilon, 3.0 + epsilon, 2.7 + epsilon,
                  2.3 + epsilon, 2.0 + epsilon, 1.7 + epsilon, 1.3 + epsilon,
                  1.0 + epsilon, 0.7 + epsilon, 0.0 + epsilon]
        expected_grades = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-']
        self.assertListEqual(numerical_letter_grade(grades), expected_grades)

    def test_typical_mixed_grades(self):
        # Typical Input Test: A mix of GPAs that fall into various grade ranges, not necessarily on boundaries.
        # Verifies correct grading for common, non-edge-case inputs.
        grades = [3.9, 2.5, 1.5, 0.5, 3.1]
        expected_grades = ['A', 'B-', 'C-', 'D-', 'B+']
        self.assertListEqual(numerical_letter_grade(grades), expected_grades)

    def test_all_same_grade_value(self):
        # Edge Case: Tests a list where all GPAs are identical, verifying consistent grading.
        # Catches potential issues with loop logic or state management.
        grades = [2.8, 2.8, 2.8]
        expected_grades = ['B', 'B', 'B']
        self.assertListEqual(numerical_letter_grade(grades), expected_grades)

    def test_extreme_values_near_zero_and_max(self):
        # Extreme Input Test: Includes very small positive GPAs and GPAs just below the highest grade.
        # Ensures robustness for values close to critical thresholds.
        grades = [0.001, 3.999, 0.701, 1.001]
        expected_grades = ['D-', 'A', 'D', 'D+']
        self.assertListEqual(numerical_letter_grade(grades), expected_grades)

    def test_mixed_grades_with_duplicates(self):
        # Typical Input Test: A mix of GPAs including duplicates, covering various ranges.
        # Ensures each GPA is processed independently and correctly.
        grades = [3.5, 2.1, 1.8, 3.5, 0.8]
        expected_grades = ['A-', 'C+', 'C', 'A-', 'D']
        self.assertListEqual(numerical_letter_grade(grades), expected_grades)