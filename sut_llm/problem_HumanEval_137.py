def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """
    def _parse_to_float(value):
        if isinstance(value, (int, float)):
            return float(value)
        elif isinstance(value, str):
            # Replace ',' with '.' for consistent float conversion
            s_value = value.replace(',', '.')
            try:
                return float(s_value)
            except ValueError:
                # Handle cases where string might not be a valid number,
                # though problem description implies valid inputs.
                # For robustness, could raise an error or return a sentinel.
                # For this problem, we assume valid number strings.
                pass
        return None # Should not happen with valid inputs

    float_a = _parse_to_float(a)
    float_b = _parse_to_float(b)

    if float_a is None or float_b is None:
        # This implies an issue with parsing, or unexpected input type
        # Based on problem statement, we assume valid number inputs.
        return None

    if float_a > float_b:
        return a
    elif float_b > float_a:
        return b
    else:
        return None