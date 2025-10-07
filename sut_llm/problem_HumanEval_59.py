def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    largest_factor = 1

    # Handle factor 2
    if n % 2 == 0:
        largest_factor = 2
        while n % 2 == 0:
            n //= 2

    # Handle odd factors starting from 3
    # We only need to check up to sqrt(n) because if n has a prime factor larger than sqrt(n),
    # it must also have a prime factor smaller than sqrt(n) which would have been divided out.
    # After dividing by all smaller factors, if n is still > 1, then the remaining n is prime.
    i = 3
    while i * i <= n:
        if n % i == 0:
            largest_factor = i
            while n % i == 0:
                n //= i
        i += 2  # Increment by 2 to check only odd numbers

    # If n is still greater than 2 after all divisions, it means the remaining n is a prime factor
    # and it's the largest one. This handles cases where the largest prime factor is
    # greater than the square root of the original n (e.g., if n was 29 * 3, after dividing by 3, n becomes 29).
    if n > 2:
        largest_factor = n

    return largest_factor