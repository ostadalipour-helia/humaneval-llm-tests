def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    is_negative = False
    if x < 0:
        is_negative = True
        x = abs(x)

    s_x = str(x)
    n = len(s_x)

    # For x=0, s_x="0", n=1. This logic handles it correctly.
    # If n is 0, it means x was effectively an empty string, which won't happen for an integer.
    # So, n will always be >= 1.

    result_digits = ""
    if shift > n:
        # Special case: If shift > number of digits, return digits reversed.
        result_digits = s_x[::-1]
    else:
        # Perform circular right shift
        effective_shift = shift % n
        # Slice the string: take the last 'effective_shift' characters and prepend them
        # to the remaining characters.
        result_digits = s_x[-effective_shift:] + s_x[:-effective_shift]

    # Reapply the negative sign if the original number was negative
    # and the result is not "0" (to avoid "-0").
    if is_negative and result_digits != "0":
        return "-" + result_digits
    else:
        return result_digits