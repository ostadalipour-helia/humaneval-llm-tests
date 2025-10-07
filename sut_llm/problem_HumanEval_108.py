def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    count = 0
    for num in arr:
        digit_sum = 0
        s_num = str(num)

        if num >= 0:
            # For positive numbers and zero, sum all digits as positive
            for digit_char in s_num:
                digit_sum += int(digit_char)
        else:  # num is negative
            # The first digit (after the minus sign) is treated as negative
            # e.g., for -123, s_num[1] is '1', so we add -int('1')
            digit_sum += -int(s_num[1])
            # The rest of the digits are treated as positive
            # e.g., for -123, s_num[2:] is "23", so we add int('2') and int('3')
            for digit_char in s_num[2:]:
                digit_sum += int(digit_char)
        
        if digit_sum > 0:
            count += 1
            
    return count