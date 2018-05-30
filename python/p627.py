"""Problem 627 - Counting Products"""
from itertools import combinations_with_replacement
from eulerlib import get_primes

def F(m, n):
    S= set()
    for x in combinations_with_replacement(range(1, m + 1), n):
        prod = 1
        for i in x:
            prod *= i
        S.add(prod)
    print(S)
    print(set(range(1,82)) - get_primes(m**n))
    print(S & get_primes(m**n))
    return len(S)

print(F(9, 2))
