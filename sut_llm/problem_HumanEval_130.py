def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    """
    memo = {}

    def _calculate_tri(k):
        # Check if the value for k has already been computed
        if k in memo:
            return memo[k]

        # Base cases and direct computations as per the definition
        if k == 0:
            # tri(0) is not explicitly defined in the recurrence,
            # but implied by the example tri(3) = [1, 3, 2, 8] where tri(0) = 1.
            result = 1
        elif k == 1:
            # Defined by tri(1) = 3
            result = 3
        elif k % 2 == 0:  # k is an even number
            # Defined by tri(n) = 1 + n / 2, if n is even.
            # We use int() to ensure the result is an integer, as shown in examples
            # (e.g., 1 + 2/2 = 2.0, but example shows 2).
            result = 1 + int(k / 2)
        else:  # k is an odd number
            # Defined by tri(n) = tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
            # This recursive step might call for values larger than k, which is handled
            # correctly by memoization.
            val_k_minus_1 = _calculate_tri(k - 1)
            val_k_minus_2 = _calculate_tri(k - 2)
            val_k_plus_1 = _calculate_tri(k + 1)
            result = val_k_minus_1 + val_k_minus_2 + val_k_plus_1

        # Store the computed result in the memoization table before returning
        memo[k] = result
        return result

    # Generate the list of the first n + 1 Tribonacci numbers
    tribonacci_sequence = []
    for i in range(n + 1):
        tribonacci_sequence.append(_calculate_tri(i))

    return tribonacci_sequence