def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # split the encoded string into groups. Each of length 3.
    # This splitting logic is identical to encode_cyclic as the group sizes are preserved.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]

    # Reverse the cycling for each group.
    # If a group had 3 elements, it was cycled from 'abc' to 'bca'.
    # To reverse 'bca' back to 'abc', we move the last character ('a') to the front.
    # If a group had fewer than 3 elements, it was not cycled, so it remains unchanged.
    decoded_groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]

    # Join the decoded groups back into a single string.
    return "".join(decoded_groups)