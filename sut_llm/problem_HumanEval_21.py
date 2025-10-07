from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if not numbers:
        return []

    min_val = min(numbers)
    max_val = max(numbers)

    range_val = max_val - min_val

    if range_val == 0:
        # If all numbers are the same, they all become 0.0 (smallest becomes 0)
        return [0.0] * len(numbers)
    else:
        rescaled_numbers = [(num - min_val) / range_val for num in numbers]
        return rescaled_numbers