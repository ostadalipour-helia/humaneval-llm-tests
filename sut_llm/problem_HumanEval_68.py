def pluck(arr):
    smallest_even_value = float('inf')
    smallest_even_index = -1

    for index, value in enumerate(arr):
        if value % 2 == 0:
            if value < smallest_even_value:
                smallest_even_value = value
                smallest_even_index = index
            # If value == smallest_even_value, we do not update
            # smallest_even_index because we are iterating from left to right,
            # so the current smallest_even_index already holds the smallest index.

    if smallest_even_value == float('inf'):
        return []
    else:
        return [smallest_even_value, smallest_even_index]