"""Problem 47 - Distinct primes factors"""
from eulerlib import prime_factors


L = []
i = 1
while len(L) < 4:
    if len(set(prime_factors(i))) == 4:
        L.append(i)
    else:
        L = []
    i += 1

print(L[0])
