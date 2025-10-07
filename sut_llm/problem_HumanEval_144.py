def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    # Parse the first fraction x
    num_x_str, den_x_str = x.split('/')
    num_x = int(num_x_str)
    den_x = int(den_x_str)

    # Parse the second fraction n
    num_n_str, den_n_str = n.split('/')
    num_n = int(num_n_str)
    den_n = int(den_n_str)

    # Multiply the numerators and denominators
    # (num_x / den_x) * (num_n / den_n) = (num_x * num_n) / (den_x * den_n)
    result_numerator = num_x * num_n
    result_denominator = den_x * den_n

    # Check if the resulting fraction is a whole number.
    # A fraction A/B is a whole number if A is perfectly divisible by B.
    return result_numerator % result_denominator == 0