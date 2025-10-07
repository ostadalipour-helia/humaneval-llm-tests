def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product_of_odd_digits = 1
    found_odd_digit = False

    # Convert the integer to a string to iterate through its digits
    s_n = str(n)

    for char_digit in s_n:
        digit = int(char_digit)
        if digit % 2 != 0:  # Check if the digit is odd
            product_of_odd_digits *= digit
            found_odd_digit = True

    if found_odd_digit:
        return product_of_odd_digits
    else:
        return 0