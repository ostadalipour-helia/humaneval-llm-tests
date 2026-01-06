import unittest
import sut.problem_HumanEval_54 as mod

class TestHybrid(unittest.TestCase):
    def test_docstring_example_1(self):
            self.assertEqual(mod.same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'), True)
    
        # Test 2: Docstring example - typical case, expected True, different order/duplicates.
        # Covers: Typical input, exact output verification.

    def test_docstring_example_2(self):
            self.assertEqual(mod.same_chars('abcd', 'dddddddabc'), True)
    
        # Test 3: Docstring example - expected False, s0 has an extra character.
        # Covers: Boundary condition (one set has an extra element), logic mutation (if 'and'/'or' were swapped in a complex condition).

    def test_docstring_example_3_s0_has_extra_char(self):
            self.assertEqual(mod.same_chars('eabcd', 'dddddddabc'), False)
    
        # Test 4: Docstring example - expected False, s1 has an extra character.
        # Covers: Boundary condition (one set has an extra element, opposite of test 3), off-by-one (in terms of set elements).

    def test_docstring_example_4_s1_has_extra_char(self):
            self.assertEqual(mod.same_chars('abcd', 'dddddddabce'), False)
    
        # Test 5: Edge case - both strings are empty.
        # Covers: Empty collections, return value testing (True).

    def test_empty_strings(self):
            self.assertEqual(mod.same_chars('', ''), True)
    
        # Test 6: Edge case - one string is empty, the other is not.
        # Covers: Empty collection vs non-empty, return value testing (False).

    def test_one_empty_string_one_non_empty(self):
            self.assertEqual(mod.same_chars('', 'a'), False)
    
        # Test 7: Edge case - single character strings, same character.
        # Covers: Single element collections, return value testing (True).

    def test_single_char_same(self):
            self.assertEqual(mod.same_chars('a', 'a'), True)
    
        # Test 8: Edge case - single character strings, different characters.
        # Covers: Single element collections, different values, return value testing (False).

    def test_single_char_different(self):
            self.assertEqual(mod.same_chars('a', 'b'), False)
    
        # Test 9: Boundary/Logic Mutation - s0 is a proper subset of s1.
        # Catches mutations like changing '==' to 'issubset' or 'issuperset' incorrectly.

    def test_s0_proper_subset_of_s1(self):
            self.assertEqual(mod.same_chars('abc', 'abce'), False)
    
        # Test 10: Boundary/Logic Mutation - s1 is a proper subset of s0.
        # Catches mutations like changing '==' to 'issubset' or 'issuperset' incorrectly (opposite direction).

    def test_s1_proper_subset_of_s0(self):
            self.assertEqual(mod.same_chars('abce', 'abc'), False)

    def test_normal_same_chars_different_order_frequency(self):
            # Normal case: Strings with same unique characters, different order and frequency.
            s0 = "eabcdzzzz"
            s1 = "dddzzzzzzzddeddabc"
            self.assertEqual(mod.same_chars(s0, s1), True)

    def test_normal_s0_extra_char(self):
            # Normal case: s0 contains an extra unique character 'e' not in s1.
            s0 = "eabcd"
            s1 = "dddddddabc"
            self.assertEqual(mod.same_chars(s0, s1), False)

    def test_normal_s1_extra_char(self):
            # Normal case: s1 contains an extra unique character 'e' not in s0.
            s0 = "abcd"
            s1 = "dddddddabce"
            self.assertEqual(mod.same_chars(s0, s1), False)

    def test_edge_both_empty(self):
            # Edge case: Both strings are empty.
            s0 = ""
            s1 = ""
            self.assertEqual(mod.same_chars(s0, s1), True)

    def test_edge_single_char_same(self):
            # Edge case: Both strings have a single, identical character.
            s0 = "a"
            s1 = "a"
            self.assertEqual(mod.same_chars(s0, s1), True)

    def test_edge_one_empty_other_not(self):
            # Edge case: One string is empty, the other is not.
            s0 = "abc"
            s1 = ""
            self.assertEqual(mod.same_chars(s0, s1), False)

    def test_edge_case_sensitive_difference(self):
            # Edge case: Strings differ only by case (case-sensitive comparison).
            s0 = "aBc"
            s1 = "AbC"
            self.assertEqual(mod.same_chars(s0, s1), False)

    def test_edge_digits_and_symbols(self):
            # Edge case: Strings containing digits and special characters.
            s0 = "123!@"
            s1 = "!@321"
            self.assertEqual(mod.same_chars(s0, s1), True)

    def test_error_s0_is_none(self):
            # Error case: s0 is not a string (None).
            s0 = None
            s1 = "abc"
            with self.assertRaises(TypeError):
                mod.same_chars(s0, s1)

    def test_error_s1_is_integer(self):
            # Error case: s1 is not a string (integer).
            s0 = "abc"
            s1 = 123
            with self.assertRaises(TypeError):
                mod.same_chars(s0, s1)

