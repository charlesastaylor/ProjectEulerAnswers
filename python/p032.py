"""Problem 32 - Pandigital products

Pretty slow.
"""

from itertools import permutations


def tuple_to_int(tup):
    return int(''.join(map(str, tup)))

S = set()
max_LHS = 5
for perm in permutations(range(1,10)):
    for i in range(1, max_LHS):
        for j in range(i+1, max_LHS + 1):
            multiplicand = tuple_to_int(perm[:i])
            multiplier = tuple_to_int(perm[i:j])
            answer = tuple_to_int(perm[j:])
            if multiplicand * multiplier == answer:
                S.add(answer)
                
print(sum(S))