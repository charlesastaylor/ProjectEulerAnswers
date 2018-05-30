"""Problem 50 - Conescutive prime sum

Doesnt run for limit > 10000 need new method, maybe start with primes and check
if they can be written as sum somehow.
"""
from itertools import combinations

from eulerlib import get_primes, is_prime

limit = 100000
primes = sorted(get_primes(limit))
length = len(primes)
answer = None
while length > 1 and answer is None:
    for start in range(len(primes) - length):
        sum_ = sum(primes[start:start + length])
        if sum_ < limit and is_prime(sum_):
            answer = sum_
            break
    length -= 1

print(answer)
