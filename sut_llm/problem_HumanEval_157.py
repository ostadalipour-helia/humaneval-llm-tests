def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    # Side lengths must be positive.
    if a <= 0 or b <= 0 or c <= 0:
        return False

    # Sort the sides to easily identify the potential hypotenuse (longest side).
    # Let x, y be the shorter sides and z be the longest side.
    sides = sorted([a, b, c])
    x, y, z = sides[0], sides[1], sides[2]

    # Use a small epsilon for floating-point comparison, as direct equality (==)
    # can be unreliable with floats due to precision issues.
    epsilon = 1e-9

    # Apply the Pythagorean theorem: x^2 + y^2 = z^2.
    # If the sides form a right-angled triangle, the sum of the squares of the two
    # shorter sides should be equal to the square of the longest side (hypotenuse).
    # The condition `x**2 + y**2 = z**2` for positive x,y,z also implies
    # the triangle inequality (x+y > z, x+z > y, y+z > x), so a separate check
    # for triangle inequality is not strictly necessary here.
    return abs(x**2 + y**2 - z**2) < epsilon