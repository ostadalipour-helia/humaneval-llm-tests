def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    result = []
    # The derivative of a term c_i * x^i is i * c_i * x^(i-1).
    # The constant term xs[0] (c_0 * x^0) differentiates to 0.
    # So we start processing from xs[1] (c_1 * x^1).
    # For each original coefficient xs[i] (where i is the power of x),
    # the new coefficient will be i * xs[i], and it corresponds to x^(i-1).
    # Thus, it will be placed at index (i-1) in the result list.
    for i in range(1, len(xs)):
        result.append(i * xs[i])
    return result