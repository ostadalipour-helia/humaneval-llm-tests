import math

def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """

    # We need to find triples (a[i], a[j], a[k]) such that (a[i] + a[j] + a[k]) % 3 == 0.
    # This is equivalent to ( (a[i] % 3) + (a[j] % 3) + (a[k] % 3) ) % 3 == 0.

    # Let's analyze the pattern of a[i] % 3 based on i (1-based index) % 3:
    # a[i] = i*i - i + 1

    # Case 1: i % 3 == 0
    #   a[i] % 3 = (0*0 - 0 + 1) % 3 = 1 % 3 = 1

    # Case 2: i % 3 == 1
    #   a[i] % 3 = (1*1 - 1 + 1) % 3 = 1 % 3 = 1

    # Case 3: i % 3 == 2
    #   a[i] % 3 = (2*2 - 2 + 1) % 3 = (4 - 2 + 1) % 3 = 3 % 3 = 0

    # So, a[i] % 3 is 0 if i % 3 == 2, and 1 otherwise (i.e., if i % 3 == 0 or i % 3 == 1).
    # This means the elements of array 'a' can only have remainders 0 or 1 when divided by 3.
    # They can never have a remainder of 2.

    # For the sum (a[i]%3 + a[j]%3 + a[k]%3) % 3 to be 0, given that
    # each a[x]%3 can only be 0 or 1, there are only two possibilities for the remainders:
    # 1. All three elements a[i], a[j], a[k] are congruent to 0 mod 3. (0 + 0 + 0 = 0)
    # 2. All three elements a[i], a[j], a[k] are congruent to 1 mod 3. (1 + 1 + 1 = 3, which is 0 mod 3)

    # We need to count how many elements in 'a' fall into each category (0 mod 3 or 1 mod 3).
    count_mod_0 = 0
    count_mod_1 = 0

    for i in range(1, n + 1):  # i is 1-based, from 1 to n
        if i % 3 == 2:
            count_mod_0 += 1
        else:  # i % 3 is 0 or 1
            count_mod_1 += 1

    # Now, calculate the number of ways to choose 3 elements from each category.
    # The 'i < j < k' condition is handled by using combinations, as any set of 3 distinct
    # indices will have a unique ascending order.
    
    # Number of triples where all three elements are 0 mod 3
    # math.comb(n, k) calculates "n choose k"
    triples_mod_0 = math.comb(count_mod_0, 3)

    # Number of triples where all three elements are 1 mod 3
    triples_mod_1 = math.comb(count_mod_1, 3)
    
    # The total number of valid triples is the sum of these two counts.
    return triples_mod_0 + triples_mod_1