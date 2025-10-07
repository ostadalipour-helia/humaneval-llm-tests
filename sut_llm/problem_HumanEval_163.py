def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    result = []

    # Determine the actual start and end of the range, ensuring ascending order
    start = min(a, b)
    end = max(a, b)

    # Iterate through the numbers in the determined range (inclusive of 'end')
    for num in range(start, end + 1):
        # According to the examples, "even digits" refers to single-digit
        # even numbers (i.e., 2, 4, 6, 8).
        # Numbers like 10, 12, 14 are even but not single digits,
        # and are excluded as per generate_integers(10, 14) => [].
        # Since 'a' and 'b' are positive, 'num' will always be >= 1.
        if num % 2 == 0 and num <= 9:
            result.append(num)

    return result