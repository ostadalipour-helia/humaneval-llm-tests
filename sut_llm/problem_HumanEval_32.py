import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    # Bisection method for finding a root of poly(x) = 0.

    # Initial search range. For an odd-degree polynomial (guaranteed by "even number of coefficients"),
    # the function will span from negative to positive infinity (or vice versa),
    # so a sufficiently large range will always contain a root.
    low = -100000.0
    high = 100000.0
    
    # Tolerance for determining if a point is a root or if the interval is small enough.
    # 1e-6 provides good precision for floating-point calculations.
    tolerance = 1e-6 
    
    # Evaluate the polynomial at the initial bounds
    f_low = poly(xs, low)
    f_high = poly(xs, high)

    # If an endpoint is already a root (within tolerance), return it.
    if abs(f_low) < tolerance:
        return low
    if abs(f_high) < tolerance:
        return high

    # Bisection loop: iterate a fixed number of times or until convergence.
    # 100 iterations are usually more than enough to achieve high precision
    # over a large initial range.
    max_iterations = 100 
    for _ in range(max_iterations):
        mid = (low + high) / 2
        f_mid = poly(xs, mid)

        # If the mid-point is close enough to zero, we found a root
        if abs(f_mid) < tolerance:
            return mid

        # Check for convergence based on interval width.
        # If the interval is smaller than the tolerance, the midpoint is a good approximation.
        if (high - low) < tolerance:
            return mid

        # Determine which half of the interval contains the root.
        # If f_low and f_mid have opposite signs, the root is in [low, mid].
        if f_low * f_mid < 0:
            high = mid
            # f_high does not need to be explicitly updated here as `poly(high)` will be recalculated
            # if `high` becomes `low` in a subsequent step.
        # Otherwise, the root is in [mid, high].
        else:
            low = mid
            f_low = f_mid # Update f_low to reflect the polynomial value at the new lower bound.

    # If the loop finishes without finding a root within tolerance,
    # return the midpoint of the final interval as the best approximation.
    return (low + high) / 2