def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    """
    
    # Step 1: Calculate the sum of the decimal digits of N
    sum_of_digits = 0
    # Convert N to a string to iterate through its digits
    for digit_char in str(N):
        sum_of_digits += int(digit_char)
        
    # Step 2: Convert the sum of digits to its binary representation
    # The built-in bin() function returns a string prefixed with "0b"
    # We need to slice the string to remove this prefix
    binary_sum_string = bin(sum_of_digits)[2:]
    
    return binary_sum_string