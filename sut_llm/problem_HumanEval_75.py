import math

def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # The smallest number that is a multiplication of 3 prime numbers is 2*2*2 = 8.
    # Any number less than 8 cannot be a multiplication of 3 primes.
    if a < 8:
        return False

    prime_factors = []
    temp_a = a
    d = 2
    while d * d <= temp_a:
        while temp_a % d == 0:
            prime_factors.append(d)
            temp_a //= d
        d += 1
    if temp_a > 1:
        prime_factors.append(temp_a)

    return len(prime_factors) == 3