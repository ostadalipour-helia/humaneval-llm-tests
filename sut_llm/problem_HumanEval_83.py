def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        # For n=1, the only 1-digit number that starts or ends with 1 is '1'.
        return 1
    else:
        # For n >= 2, we use the Principle of Inclusion-Exclusion:
        # P(A or B) = P(A) + P(B) - P(A and B)

        # A: Count of n-digit numbers that start with 1.
        # The first digit is fixed as 1. The remaining (n-1) digits can be any from 0-9.
        # So, there are 1 * 10^(n-1) such numbers.
        count_starts_with_1 = 10**(n - 1)

        # B: Count of n-digit numbers that end with 1.
        # The last digit is fixed as 1.
        # The first digit can be any from 1-9 (cannot be 0 for an n-digit number).
        # The middle (n-2) digits (if n > 2) can be any from 0-9.
        # So, there are 9 * 10^(n-2) such numbers.
        count_ends_with_1 = 9 * (10**(n - 2))

        # A and B: Count of n-digit numbers that start AND end with 1.
        # The first digit is 1, and the last digit is 1.
        # The middle (n-2) digits can be any from 0-9.
        # So, there are 1 * 10^(n-2) * 1 such numbers.
        count_starts_and_ends_with_1 = 10**(n - 2)

        # Apply Inclusion-Exclusion Principle
        total_count = count_starts_with_1 + count_ends_with_1 - count_starts_and_ends_with_1

        return total_count