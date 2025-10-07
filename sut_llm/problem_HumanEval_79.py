def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    """
    # Convert the decimal number to its binary representation.
    # The built-in bin() function returns a string prefixed with "0b".
    binary_str_with_prefix = bin(decimal)

    # Remove the "0b" prefix.
    # For example, bin(15) is "0b1111", so we slice from index 2.
    binary_str = binary_str_with_prefix[2:]

    # Add the "db" prefix and suffix as required.
    formatted_binary_str = "db" + binary_str + "db"

    return formatted_binary_str