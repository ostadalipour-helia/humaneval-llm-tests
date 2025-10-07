def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1

    # Initialize the last three values: fibfib(0), fibfib(1), fibfib(2)
    f0, f1, f2 = 0, 0, 1

    # Iterate from n=3 up to the requested n
    for _ in range(3, n + 1):
        next_fib = f0 + f1 + f2
        f0 = f1
        f1 = f2
        f2 = next_fib
    
    return f2