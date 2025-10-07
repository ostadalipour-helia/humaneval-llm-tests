def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # This problem is a variation of Kadane's algorithm for finding the maximum subarray sum.
    # We adapt it to find the minimum subarray sum.

    # Initialize min_so_far and current_min with the first element of the array.
    # This handles the case of a single-element array and correctly sets
    # initial values assuming 'nums' is guaranteed to be non-empty
    # (as implied by the problem statement requiring a "non-empty sub-array").
    min_so_far = nums[0]
    current_min = nums[0]

    # Iterate through the rest of the elements starting from the second one.
    for x in nums[1:]:
        # For each element 'x', we decide whether to extend the current minimum
        # sub-array (current_min + x) or start a new sub-array with 'x'.
        # If 'x' itself is smaller than 'current_min + x', it means starting
        # a new sub-array from 'x' yields a smaller sum than extending the previous one.
        current_min = min(x, current_min + x)
        
        # Update the overall minimum sum found so far.
        min_so_far = min(min_so_far, current_min)

    return min_so_far