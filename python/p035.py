"""Problem 35 - Circular primes"""
from collections import deque

from eulerlib import get_primes


primes = get_primes(1000000)
circular_primes = []

for prime in primes:
    d = deque(list(str(prime)))
    circular = True
    for i in range(len(d) - 1):
        d.rotate(1)
        if not int("".join(d)) in primes:
            circular = False
            break
    if circular:
        circular_primes.append(prime)

print(len(circular_primes))
