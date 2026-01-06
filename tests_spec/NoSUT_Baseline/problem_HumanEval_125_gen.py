import unittest
import sut.problem_HumanEval_125 as mod

class TestHybrid(unittest.TestCase):
    def test_whitespace_split_typical(self):
            # CRITICAL: Typical input, Return Value Testing (list)
            # SPECIFIC: Typical/expected inputs
            self.assertListEqual(mod.split_words("Hello world!"), ["Hello", "world!"])

    def test_comma_split_typical(self):
            # CRITICAL: Typical input, Return Value Testing (list)
            # SPECIFIC: Typical/expected inputs
            self.assertListEqual(mod.split_words("Hello,world!"), ["Hello", "world!"])

    def test_odd_order_count_typical(self):
            # CRITICAL: Typical input, Return Value Testing (integer)
            # SPECIFIC: Typical/expected inputs
            self.assertEqual(mod.split_words("abcdef"), 3) # b=1, d=3, f=5 are odd

    def test_whitespace_split_multiple_spaces_and_trim(self):
            # CRITICAL: Boundary Testing (multiple spaces), Off-by-One Errors (leading/trailing/extra spaces)
            # SPECIFIC: Boundary conditions, Extreme/unusual inputs
            self.assertListEqual(mod.split_words("  leading  middle   trailing  "), ["leading", "middle", "trailing"])

    def test_edge_empty_string(self):
            # CRITICAL: Edge Cases (empty collection), Return Value Testing (default/computed 0)
            # SPECIFIC: Edge cases (empty)
            self.assertEqual(mod.split_words(""), 0)

    def test_edge_single_word_no_split(self):
            # CRITICAL: Edge Cases (single element collection), Return Value Testing (computed value)
            # SPECIFIC: Edge cases (single element)
            self.assertEqual(mod.split_words("Python"), 3) # 't'=19, 'h'=7, 'n'=13 are odd

    def test_logic_priority_whitespace_over_comma(self):
            # CRITICAL: Logic Mutations (ensures whitespace check precedes comma check)
            # SPECIFIC: Extreme/unusual inputs (mixed delimiters)
            self.assertListEqual(mod.split_words("Hello, world!"), ["Hello,", "world!"])

    def test_extreme_non_alphabetic_for_count(self):
            # CRITICAL: Edge Cases (string with only special characters/numbers), Sign and Zero Testing (result 0)
            # SPECIFIC: Extreme/unusual inputs
            self.assertEqual(mod.split_words("!@#$123"), 0)

    def test_boundary_odd_order_count_all_even_letters(self):
            # CRITICAL: Boundary Testing (0 odd-ordered letters), Off-by-One Errors (letters just missing odd order)
            # SPECIFIC: Boundary conditions
            self.assertEqual(mod.split_words("acegik"), 0) # a=0, c=2, e=4, g=6, i=8, k=10 are all even

    def test_normal_whitespace_split(self):
            # Normal case: input with whitespace, should split by whitespace
            self.assertEqual(mod.split_words("Hello world!"), ["Hello", "world!"])

    def test_normal_comma_split(self):
            # Normal case: input with commas, no whitespace, should split by comma
            self.assertEqual(mod.split_words("one,two,three"), ["one", "two", "three"])

    def test_normal_integer_count(self):
            # Normal case: input with no whitespace or commas, should count odd-indexed lowercase letters
            self.assertEqual(mod.split_words("abcdef"), 3) # b(1), d(3), f(5)

    def test_edge_empty_string_count(self):
            # Edge case: empty string, no whitespace or commas, count should be 0
            self.assertEqual(mod.split_words(""), 0)

    def test_edge_only_whitespace(self):
            # Edge case: string with only whitespace, should split into an empty list
            self.assertEqual(mod.split_words("   "), [])

    def test_edge_whitespace_leading_trailing_multiple(self):
            # Edge case: whitespace split with leading/trailing/multiple spaces
            self.assertEqual(mod.split_words("  hello  world  "), ["hello", "world"])

    def test_edge_single_odd_char_count(self):
            # Edge case: single character, odd alphabetical order
            self.assertEqual(mod.split_words("b"), 1) # b is 1st (odd)

    def test_edge_integer_count_xyz(self):
            # Edge case: integer count with mixed odd/even alphabetical order
            self.assertEqual(mod.split_words("xyz"), 2) # x(23), z(25) are odd

    def test_error_none_input(self):
            # Error case: input is None, should raise TypeError
            with self.assertRaises(TypeError):
                mod.split_words(None)

    def test_error_int_input(self):
            # Error case: input is an integer, should raise TypeError
            with self.assertRaises(TypeError):
                mod.split_words(123)

