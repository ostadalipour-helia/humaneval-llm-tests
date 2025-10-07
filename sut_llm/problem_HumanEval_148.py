def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''
    planets_order = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    if planet1 not in planets_order or planet2 not in planets_order:
        return ()

    index1 = planets_order.index(planet1)
    index2 = planets_order.index(planet2)

    # Determine the start and end indices for slicing, ensuring they are ordered
    start_slice_index = min(index1, index2) + 1
    end_slice_index = max(index1, index2)

    # Slice the list to get planets between the two specified planets
    # The slice is exclusive of the end_slice_index, which is what we want
    # as the planets must be *between* planet1 and planet2.
    result_planets = planets_order[start_slice_index:end_slice_index]

    return tuple(result_planets)