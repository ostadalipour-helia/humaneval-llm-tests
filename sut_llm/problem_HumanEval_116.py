def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    def count_set_bits(n):
        # Converts the number to its binary string representation (e.g., 5 -> '0b101').
        # Then counts the occurrences of '1' in that string.
        # This handles both positive and negative numbers by counting '1's
        # in the part after '-0b' or '0b'.
        return bin(n).count('1')

    # Sort the array using a custom key.
    # The key is a tuple: (number of ones, original decimal value).
    # Python's default tuple sorting will first compare by the first element,
    # and if they are equal, then compare by the second element.
    # This matches the specified sorting criteria:
    # 1. Ascending order of number of ones.
    # 2. For similar number of ones, sort based on decimal value (ascending).
    return sorted(arr, key=lambda x: (count_set_bits(x), x))