import unittest
from sut.problem_HumanEval_54 import same_chars

class TestSameChars(unittest.TestCase):

    # Test 1: Docstring example - typical case, expected True.
    # Covers: Typical input, exact output verification.
    def test_docstring_example_1(self):
        self.assertEqual(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'), True)

    # Test 2: Docstring example - typical case, expected True, different order/duplicates.
    # Covers: Typical input, exact output verification.
    def test_docstring_example_2(self):
        self.assertEqual(same_chars('abcd', 'dddddddabc'), True)

    # Test 3: Docstring example - expected False, s0 has an extra character.
    # Covers: Boundary condition (one set has an extra element), logic mutation (if 'and'/'or' were swapped in a complex condition).
    def test_docstring_example_3_s0_has_extra_char(self):
        self.assertEqual(same_chars('eabcd', 'dddddddabc'), False)

    # Test 4: Docstring example - expected False, s1 has an extra character.
    # Covers: Boundary condition (one set has an extra element, opposite of test 3), off-by-one (in terms of set elements).
    def test_docstring_example_4_s1_has_extra_char(self):
        self.assertEqual(same_chars('abcd', 'dddddddabce'), False)

    # Test 5: Edge case - both strings are empty.
    # Covers: Empty collections, return value testing (True).
    def test_empty_strings(self):
        self.assertEqual(same_chars('', ''), True)

    # Test 6: Edge case - one string is empty, the other is not.
    # Covers: Empty collection vs non-empty, return value testing (False).
    def test_one_empty_string_one_non_empty(self):
        self.assertEqual(same_chars('', 'a'), False)

    # Test 7: Edge case - single character strings, same character.
    # Covers: Single element collections, return value testing (True).
    def test_single_char_same(self):
        self.assertEqual(same_chars('a', 'a'), True)

    # Test 8: Edge case - single character strings, different characters.
    # Covers: Single element collections, different values, return value testing (False).
    def test_single_char_different(self):
        self.assertEqual(same_chars('a', 'b'), False)

    # Test 9: Boundary/Logic Mutation - s0 is a proper subset of s1.
    # Catches mutations like changing '==' to 'issubset' or 'issuperset' incorrectly.
    def test_s0_proper_subset_of_s1(self):
        self.assertEqual(same_chars('abc', 'abce'), False)

    # Test 10: Boundary/Logic Mutation - s1 is a proper subset of s0.
    # Catches mutations like changing '==' to 'issubset' or 'issuperset' incorrectly (opposite direction).
    def test_s1_proper_subset_of_s0(self):
        self.assertEqual(same_chars('abce', 'abc'), False)