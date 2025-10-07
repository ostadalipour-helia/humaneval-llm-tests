def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Iterate downwards from n-1 to 1.
    # The first number found that divides n evenly will be the largest
    # divisor smaller than n.
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    
    # This part of the code should theoretically only be reached if n <= 1.
    # For n > 1, at least 1 will always be a divisor, so the loop will find it.
    # The problem statement and example imply n will be an integer greater than 1.
    # If n=1, there are no integers smaller than n that divide n,
    # and the loop range(0, 0, -1) would be empty.
    # In such a case, the function would implicitly return None.
    # However, assuming n > 1 based on the problem's context.