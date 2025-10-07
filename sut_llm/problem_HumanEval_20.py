from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    n = len(numbers)
    
    # Initialize with the first pair and its difference.
    # The problem statement guarantees the list has at least two elements.
    closest_pair = (numbers[0], numbers[1])
    min_diff = abs(numbers[0] - numbers[1])

    # Iterate through all unique pairs of numbers
    for i in range(n):
        for j in range(i + 1, n):
            num1 = numbers[i]
            num2 = numbers[j]
            current_diff = abs(num1 - num2)

            if current_diff < min_diff:
                min_diff = current_diff
                closest_pair = (num1, num2)
            # If current_diff == min_diff, we keep the existing closest_pair
            # as the problem statement does not specify tie-breaking.

    # Ensure the returned pair is in (smaller number, larger number) order
    return (min(closest_pair), max(closest_pair))