import math

def is_prime(num: int) -> bool:
    """
    Checks if a number is prime.
    """
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    # Check for odd divisors from 3 up to sqrt(num)
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def fib_generator():
    """
    Generates Fibonacci numbers starting from F3 (2).
    Standard Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...
    This generator yields: 2, 3, 5, 8, 13, ...
    """
    a, b = 1, 2  # a corresponds to F2, b corresponds to F3
    while True:
        yield b
        a, b = b, a + b

def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")

    count = 0
    fib_gen = fib_generator()

    while True:
        fib_num = next(fib_gen)
        if is_prime(fib_num):
            count += 1
            if count == n:
                return fib_num