import unittest
from sut_llm.problem_HumanEval_117 import select_words

class TestSelectWords(unittest.TestCase):

    def test_01_docstring_example_one_match(self):
        # Test case from docstring: one word matches
        s = "Mary had a little lamb"
        n = 4
        expected_output = ["little"]
        self.assertEqual(select_words(s, n), expected_output)

    def test_02_docstring_example_multiple_matches(self):
        # Test case from docstring: multiple words match
        s = "Mary had a little lamb"
        n = 3
        expected_output = ["Mary", "lamb"]
        self.assertEqual(select_words(s, n), expected_output)

    def test_03_docstring_example_no_matches(self):
        # Test case from docstring: no words match
        s = "simple white space"
        n = 2
        expected_output = []
        self.assertEqual(select_words(s, n), expected_output)

    def test_04_docstring_example_hello_world(self):
        # Test case from docstring: "Hello world"
        s = "Hello world"
        n = 4
        expected_output = ["world"]
        self.assertEqual(select_words(s, n), expected_output)

    def test_05_docstring_example_uncle_sam(self):
        # Test case from docstring: "Uncle sam"
        s = "Uncle sam"
        n = 3
        expected_output = ["Uncle"]
        self.assertEqual(select_words(s, n), expected_output)

    def test_06_empty_string_input(self):
        # Test case: empty input string should return an empty list
        s = ""
        n = 5
        expected_output = []
        self.assertEqual(select_words(s, n), expected_output)

    def test_07_no_words_match_consonant_count(self):
        # Test case: words exist but none match the exact consonant count
        s = "apple banana cherry" # apple:3, banana:3, cherry:5
        n = 4
        expected_output = []
        self.assertEqual(select_words(s, n), expected_output)

    def test_08_words_with_y_as_consonant(self):
        # Test case: words containing 'y' which should be counted as a consonant
        s = "rhythm myth" # rhythm: r,h,y,t,h,m (6); myth: m,y,t,h (4)
        n = 4
        expected_output = ["myth"]
        self.assertEqual(select_words(s, n), expected_output)

    def test_09_case_sensitivity_and_multiple_words(self):
        # Test case: checks for case sensitivity of letters and multiple words
        s = "PYTHON is FUN" # PYTHON: P,Y,T,H,N (5); is: s (1); FUN: F,N (2)
        n = 5
        expected_output = ["PYTHON"]
        self.assertEqual(select_words(s, n), expected_output)

    def test_10_string_with_various_spaces(self):
        # Test case: string with leading/trailing/multiple spaces
        s = "  a  test  string  " # a: 0; test: t,s,t (3); string: s,t,r,n,g (5)
        n = 3
        expected_output = ["test"]
        self.assertEqual(select_words(s, n), expected_output)

if __name__ == '__main__':
    unittest.main()