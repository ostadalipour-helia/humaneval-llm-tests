def fruit_distribution(s,n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    for examble:
    fruit_distribution("5 apples and 6 oranges", 19) ->19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges",3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges",120) -> 120 - 100 - 1 = 19
    """
    
    # Split the string to extract the number of apples and oranges
    # The string format is "X apples and Y oranges"
    
    # First, split by " apples and " to separate apples from the rest
    parts = s.split(" apples and ")
    
    # The first part is the number of apples
    num_apples = int(parts[0])
    
    # The second part contains the number of oranges followed by " oranges"
    oranges_part = parts[1]
    
    # Now, split the oranges_part by " oranges" to get the number of oranges
    num_oranges = int(oranges_part.split(" oranges")[0])
    
    # The total number of fruits in the basket is n
    # The number of mango fruits is n - (apples + oranges)
    num_mangoes = n - (num_apples + num_oranges)
    
    return num_mangoes