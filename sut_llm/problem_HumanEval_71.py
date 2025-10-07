import math

def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    '''
    # Check if all sides are positive
    if a <= 0 or b <= 0 or c <= 0:
        return -1

    # Check triangle inequality theorem
    # The sum of the lengths of any two sides of a triangle must be greater than the length of the third side.
    if not (a + b > c and a + c > b and b + c > a):
        return -1

    # If it's a valid triangle, calculate the area using Heron's formula
    # Calculate the semi-perimeter
    s = (a + b + c) / 2

    # Calculate the area
    # The term inside the square root should always be non-negative for a valid triangle.
    # If it were negative, it would imply the triangle inequality failed, which we've already checked.
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    # Round the area to 2 decimal points
    return round(area, 2)