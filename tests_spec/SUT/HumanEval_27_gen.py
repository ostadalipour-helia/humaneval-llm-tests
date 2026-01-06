import unittest
from sut.problem_HumanEval_27 import flip_case

class Test_flip_case(unittest.TestCase):

    def test_normal_mixed_case(self):
        self.assertEqual(flip_case('Hello'), 'hELLO')

    def test_normal_all_uppercase(self):
        self.assertEqual(flip_case('WORLD'), 'world')

    def test_normal_all_lowercase(self):
        self.assertEqual(flip_case('python'), 'PYTHON')

    def test_normal_alternating_case(self):
        self.assertEqual(flip_case('PyThOn'), 'pYtHoN')

    def test_edge_empty_string(self):
        self.assertEqual(flip_case(''), '')

    def test_edge_non_alphabetic(self):
        self.assertEqual(flip_case('123!@#'), '123!@#')

    def test_edge_mixed_content(self):
        self.assertEqual(flip_case('Hello World 123!'), 'hELLO wORLD 123!')

    def test_edge_single_lowercase(self):
        self.assertEqual(flip_case('a'), 'A')

    def test_edge_single_uppercase(self):
        self.assertEqual(flip_case('Z'), 'z')

    # A 10th test case to meet the requirement, reusing an existing case.
    def test_another_mixed_case(self):
        self.assertEqual(flip_case('Hello'), 'hELLO')