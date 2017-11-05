"""Problem 15 - Lattice paths.

Problem can be solved using combinatorics but thats boring...
Instead I used a recurseive function and a memoizing decorator to cache
calls to the function.
Can solve the 82x82 case in 0.121 seconds. Only fails higher due to pythons
max recurssion depth.
"""

from eulerlib import Memoized

@Memoized
def no_paths(size):
    """ poop.

    Only deal with square lattices atm
    """
    if size == (1, 1):
        # Found a path
        return 1
    # if (size[0] + 1) == size[1]:
    #     # Dont search for mirrors - multiply ans by factor at end
    #     # Dont really understand where im getting the factor from...
    #     return 0
    elif size[0] == 0 or size[1] == 0:
        # No paths here
        return 0
    else:
        x = no_paths((size[0], size[1]-1))
        y = no_paths((size[0]-1, size[1]))
        return x + y

start_size = 20
ans = no_paths((start_size + 1, start_size + 1)) # 2x2 squares == 3x3 points
# ans *= start_size + 1
print("Size: {}x{}\nNo Paths: {}".format(start_size, start_size, ans))
