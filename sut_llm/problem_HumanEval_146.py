def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for num in nums:
        if num > 10:
            # Convert the absolute value of the number to a string to easily access digits
            s_num = str(abs(num))
            
            # Get the first and last digits as integers
            first_digit = int(s_num[0])
            last_digit = int(s_num[-1])
            
            # Check if both first and last digits are odd
            if first_digit % 2 != 0 and last_digit % 2 != 0:
                count += 1
    return count