def minPath(grid, k):
    """
    Given a grid with N rows and N columns (N >= 2) and a positive integer k, 
    each cell of the grid contains a value. Every integer in the range [1, N * N]
    inclusive appears exactly once on the cells of the grid.

    You have to find the minimum path of length k in the grid. You can start
    from any cell, and in each step you can move to any of the neighbor cells,
    in other words, you can go to cells which share an edge with you current
    cell.
    Please note that a path of length k means visiting exactly k cells (not
    necessarily distinct).
    You CANNOT go off the grid.
    A path A (of length k) is considered less than a path B (of length k) if
    after making the ordered lists of the values on the cells that A and B go
    through (let's call them lst_A and lst_B), lst_A is lexicographically less
    than lst_B, in other words, there exist an integer index i (1 <= i <= k)
    such that lst_A[i] < lst_B[i] and for any j (1 <= j < i) we have
    lst_A[j] = lst_B[j].
    It is guaranteed that the answer is unique.
    Return an ordered list of the values on the cells that the minimum path go through.

    Examples:

        Input: grid = [ [1,2,3], [4,5,6], [7,8,9]], k = 3
        Output: [1, 2, 1]

        Input: grid = [ [5,9,3], [4,1,6], [7,8,2]], k = 1
        Output: [1]
    """
    N = len(grid)
    
    # Initialize min_path_so_far with values guaranteed to be larger than any possible path.
    # The maximum possible value in the grid is N*N. So N*N + 1 is a safe "infinity" value.
    min_path_so_far = [(N * N) + 1] * k 

    # Directions for moving to neighbor cells: up, down, left, right
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def dfs(r, c, current_path):
        nonlocal min_path_so_far

        # Pruning check: If current_path is already lexicographically greater than 
        # the current best path found so far (min_path_so_far) up to its current length,
        # then this branch cannot lead to a better path, so we stop exploring it.
        # Python's list comparison `>` handles lexicographical comparison.
        # We compare `current_path` with the prefix of `min_path_so_far` of the same length.
        if current_path > min_path_so_far[:len(current_path)]:
            return

        # Base case: A path of length k has been formed.
        if len(current_path) == k:
            # If this path is lexicographically smaller than the current minimum, update.
            # Python's list comparison `<` handles lexicographical comparison for full paths.