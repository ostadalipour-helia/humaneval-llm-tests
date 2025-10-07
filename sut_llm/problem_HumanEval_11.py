from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    result_chars = []
    for bit_a, bit_b in zip(a, b):
        if bit_a == bit_b:
            result_chars.append('0')
        else:
            result_chars.append('1')
    return "".join(result_chars)