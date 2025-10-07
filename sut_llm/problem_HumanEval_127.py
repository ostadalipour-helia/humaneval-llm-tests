import math

def is_prime(n):
    """
    Checks if a given number n is a prime number.
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Check for factors from 3 up to sqrt(n), only odd numbers
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    """You are given two intervals,
    where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
    The given intervals are closed which means that the interval (start, end)
    includes both start and end.
    For each given interval, it is assumed that its start is less or equal its end.
    Your task is to determine whether the length of intersection of these two 
    intervals is a prime number.
    Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
    which its length is 1, which not a prime number.
    If the length of the intersection is a prime number, return "YES",
    otherwise, return "NO".
    If the two intervals don't intersect, return "NO".


    [input/output] samples:
    intersection((1, 2), (2, 3)) ==> "NO"
    intersection((-1, 1), (0, 4)) ==> "NO"
    intersection((-3, -1), (-5, 5)) ==> "YES"
    """
    s1, e1 = interval1
    s2, e2 = interval2

    # Calculate the start and end of the intersection
    intersection_start = max(s1, s2)
    intersection_end = min(e1, e2)

    # Determine the length of the intersection
    # Based on the example "intersection of (1,3), (2,4) is (2,3) which its length is 1",
    # the length is calculated as (end - start), not (end - start + 1).
    if intersection_start > intersection_end:
        # If intersection_start is greater than intersection_end,
        # the intervals do not overlap or the intersection is empty.
        # In this case, the length of the intersection is 0.
        length = 0
    else:
        length = intersection_end - intersection_start

    # Check if the calculated length is a prime number
    if is_prime(length):
        return "YES"
    else:
        return "NO"