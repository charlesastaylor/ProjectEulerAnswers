"""Problem 67 - Maximum path sum II

Just copy pasted recursive brute force algorithm form p018 and added the 
Memoized class already written, solved in 0.127s.
The clever method hinted at in the problem description is to start at the bottom
of the trianlge and for each pair add the largest to the number above. In effect
this method works out pretty much the same as using memoization.
"""
from eulerlib import Memoized

f = open("p067_triangle.txt")
tri_s = f.read()

# Convert triangle string to list of lists of ints
tri = [[int(s) for s in row_s.split(' ')] for row_s in tri_s.split('\n')]

@Memoized
def max_path_sum(pos):
    """Poop.

    pos = (row, column)
    """
    if pos[0] == len(tri) - 1:
        return tri[pos[0]][pos[1]]
    x = max_path_sum((pos[0] + 1, pos[1]))
    y = max_path_sum((pos[0] + 1, pos[1] + 1))
    return tri[pos[0]][pos[1]] + max(x, y)

print(max_path_sum((0,0)))
