def count_up_to(n):
    """Implement a function that takes a non-negative integer and returns an array of the prime numbers
    that are less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    """

    if n <= 2:
        return []

    primes = []

    def is_prime(num):
        """Helper function to check if a number is prime."""
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:  # All other even numbers are not prime
            return False
        
        # Check for odd divisors from 3 up to the square root of num
        # We only need to check up to sqrt(num) because if a number n has a divisor d > sqrt(n),
        # then it must also have a divisor n/d < sqrt(n).
        i = 3
        while i * i <= num:
            if num % i == 0:
                return False
            i += 2  # Only check odd divisors
        return True

    # Iterate from 2 up to n-1 and check for primality
    for number in range(2, n):
        if is_prime(number):
            primes.append(number)

    return primes