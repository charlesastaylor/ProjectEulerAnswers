"""Problem 32 - Pandigital products

Brute force approach with some shortcuts. Make use of sets to check whether
computed answer has correct digits.
"""

from itertools import permutations


def tuple_to_int(tup):
    return int(''.join(map(str, tup)))

S = set()
for length in range(2, 5 + 1):
    for perm in permutations(range(1,10), length):
        target = set(range(1,10)) - set(perm)
        for i in range(1, length // 2 + 1):
            answer = tuple_to_int(perm[:i]) * tuple_to_int(perm[i:])
            if len(str(answer)) == 9 - length and target == {int(d) for d in str(answer)}:
                S.add(answer)
print(sum(S))