"""Problem 49 - Prime permutations

TODO: pretty slow atm ~30s
"""
from itertools import combinations

from eulerlib import get_primes


four_digit_primes = sorted(get_primes(9999) - get_primes(999))

for sequence in combinations(four_digit_primes, 3):
    if (sequence[1] - sequence[0] == sequence[2] - sequence[1]
        and sorted(str(sequence[0])) == sorted(str(sequence[1]))
        and sorted(str(sequence[0])) == sorted(str(sequence[2]))):
        if sequence == (1487, 4817, 8147):
            continue
        else:
            print(int("".join([str(num) for num in sequence])))
            break
