"""Problem 43 - Sub-string divisibility

Super clear amiright... Aparet from being very unclear also quite slow!
"""
from itertools import permutations

from eulerlib import get_primes


primes = get_primes(17, sort=True)
answer = 0
for perm in permutations(range(10), 10):
    if all([int("".join([str(n) for n in perm[i + 1:i + 1 + 3]])) % primes[i] == 0 for i in range(7)]):
        answer += int("".join([str(n) for n in perm]))
print(answer)
