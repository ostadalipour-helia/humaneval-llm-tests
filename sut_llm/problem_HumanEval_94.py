import math

def is_prime(n):
    """
    Checks if a number is prime.
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Check for odd divisors from 3 up to the square root of n
    # Using math.isqrt for integer square root for efficiency
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

def sum_digits(n):
    """
    Calculates the sum of the digits of a given non-negative integer.
    """
    # For prime numbers, n will always be positive.
    return sum(int(digit) for digit in str(n))

def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7
    """
    largest_prime = -1  # Initialize with a value smaller than any possible prime (primes are >= 2)

    for num in lst:
        if is_prime(num):
            if num > largest_prime:
                largest_prime = num
    
    # According to the problem description and examples, it's implied that
    # the list will always contain at least one prime number.
    # If there was a possibility of no primes, one would need to handle
    # the case where largest_prime remains -1 (e.g., return 0 or raise an error).
    
    return sum_digits(largest_prime)