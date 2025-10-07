def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 0

    # Initialize the four previous values needed to compute fib4(4)
    # a holds fib4(i-4)
    # b holds fib4(i-3)
    # c holds fib4(i-2)
    # d holds fib4(i-1)
    
    # For i=4, these correspond to fib4(0), fib4(1), fib4(2), fib4(3)
    a = 0  # fib4(0)
    b = 0  # fib4(1)
    c = 2  # fib4(2)
    d = 0  # fib4(3)

    # Iterate from 4 up to n
    for _ in range(4, n + 1):
        next_fib = d + c + b + a
        # Shift values for the next iteration
        a = b
        b = c
        c = d
        d = next_fib
    
    return d