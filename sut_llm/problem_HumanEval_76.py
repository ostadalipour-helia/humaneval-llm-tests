def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
    # Case 1: x = 1
    # Any non-zero n raised to the power of 0 is 1.
    # Conventionally, 0**0 = 1. So if x is 1, it's always a simple power.
    if x == 1:
        return True

    # Case 2: x = 0
    # If x is 0, n must also be 0 (0**k = 0 for k > 0).
    # If n is not 0, n**k can never be 0 for any integer k.
    if x == 0:
        return n == 0

    # From here, x is not 0 and not 1.

    # Case 3: n = 0
    # If n is 0, 0**k can only be 0 (if k > 0) or 1 (if k = 0).
    # Since x is not 0 or 1, it cannot be a power of 0.
    if n == 0:
        return False

    # Case 4: n = 1
    # If n is 1, 1**k is always 1 for any integer k.
    # Since x is not 1, it cannot be a power of 1.
    if n == 1:
        return False

    # Case 5: n = -1
    # If n is -1, (-1)**k can only be 1 (for even k) or -1 (for odd k).
    # Since x is not 1, it can only be -1 to be a power of -1.
    if n == -1:
        return x == -1

    # Case 6: General case (x is not 0 or 1, n is not 0, 1, or -1)
    # We use a division approach. If x is a power of n, then repeatedly dividing
    # x by n should eventually lead to 1, with no remainder at any step.
    
    # If x < 0 and n > 0, it's impossible for n**k = x (as positive n raised to any int power is positive).
    if x < 0 and n > 0:
        return False

    temp_x = x
    while True:
        # If temp_x is 1, we successfully divided it down to 1.
        if temp_x == 1:
            return True
        # If temp_x is n, it means it's n**1.
        if temp_x == n:
            return True
        # If temp_x is not divisible by n, it's not a power of n.
        if temp_x % n != 0:
            return False
        # If abs(temp_x) is less than abs(n) and not 1, it means we've overshot
        # or cannot reach 1 by dividing.
        # Example: is_simple_power(5, 3) -> temp_x=5, n=3. 5%3 != 0 -> False
        # Example: is_simple_power(2, -2) -> temp_x=2, n=-2. 2%-2==0, temp_x = -1. -1%-2 != 0 -> False
        if abs(temp_x) < abs(n) and temp_x != 1 and temp_x != n:
             return False

        temp_x //= n