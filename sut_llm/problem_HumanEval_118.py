def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """
    VOWELS = "aeiouAEIOU"
    
    def is_vowel(char):
        return char in VOWELS

    # Given the assumption that the string contains English letters only,
    # a consonant is simply any letter that is not a vowel.
    def is_consonant(char):
        return not is_vowel(char)

    n = len(word)

    # Iterate from the second to last character (index n-2) down to the second character (index 1).
    # This range ensures that for any character word[i], both word[i-1] and word[i+1] exist.
    for i in range(n - 2, 0, -1):
        current_char = word[i]
        
        if is_vowel(current_char):
            left_char = word[i-1]
            right_char = word[i+1]
            
            if is_consonant(left_char) and is_consonant(right_char):
                return current_char
                
    return ""