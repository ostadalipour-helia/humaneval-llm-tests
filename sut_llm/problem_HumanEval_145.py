def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """

    def sum_digits(n):
        """Helper function to calculate the sum of digits of a number."""
        s = 0
        n_abs = abs(n)  # Take absolute value to sum digits regardless of sign
        # Convert to string to iterate over digits
        for digit_char in str(n_abs):
            s += int(digit_char)
        return s

    if not nums:
        return []

    # Create a list of tuples (original_index, number)
    # This allows us to use the original index as a tie-breaker during sorting.
    indexed_nums = list(enumerate(nums))

    # Sort the indexed_nums. The key for sorting is a tuple:
    # 1. The sum of digits of the number (primary sorting criteria, ascending).
    # 2. The original index of the number (secondary sorting criteria, for tie-breaking, ascending).
    # Python's tuple comparison handles this naturally: it compares the first elements,
    # if they are equal, it compares the second elements, and so on.
    sorted_indexed_nums = sorted(indexed_nums, key=lambda item: (sum_digits(item[1]), item[0]))

    # Extract only the numbers from the sorted list of (index, number) tuples
    result = [num for index, num in sorted_indexed_nums]

    return result