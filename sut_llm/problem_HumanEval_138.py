def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # For n to be a sum of exactly 4 positive even numbers:
    # 1. The sum of 4 positive even numbers must be an even number.
    #    So, n must be even.
    # 2. The smallest possible sum of 4 positive even numbers is when each number is 2 (the smallest positive even number).
    #    2 + 2 + 2 + 2 = 8.
    #    So, n must be at least 8.

    # If n is less than 8, it cannot be formed by summing 4 positive even numbers.
    if n < 8:
        return False
    
    # If n is odd, it cannot be formed by summing 4 even numbers.
    if n % 2 != 0:
        return False
    
    # If n is an even number and n >= 8, it is always possible.
    # For example, we can always choose:
    # e1 = 2
    # e2 = 2
    # e3 = 2
    # e4 = n - 6
    # Since n is even, n-6 is also even.
    # Since n >= 8, n-6 >= 2, so e4 is a positive even number.
    # Thus, e1, e2, e3, e4 are all positive even numbers that sum to n.
    return True