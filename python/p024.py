"""Problem 24 - Lexicographic Permutations

Straightfroward use of itertools.
"""
from itertools import permutations, islice
print(''.join(str(e) for e in next(islice(permutations(range(10)), 999999, 1000000))))

