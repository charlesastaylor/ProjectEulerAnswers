"""Problem 87 - Prime power triples"""
from eulerlib import get_primes

largest_prime = int(50000000**0.5)
primes = get_primes(largest_prime, sort=True)

for square in primes:
    for cube in primes:
        for quad in primes:
            pass
