def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0

    # Convert the number to its absolute value to handle negative inputs
    # and then to a string to iterate through its digits.
    s_num = str(abs(num))

    for digit_char in s_num:
        digit = int(digit_char)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return (even_count, odd_count)