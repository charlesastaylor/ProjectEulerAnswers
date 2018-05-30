"""Problem 50 - Conescutive prime sum"""
from itertools import combinations

from eulerlib import get_primes, is_prime

limit = 1000000
primes = sorted(get_primes(limit))

# Find maximum length worth considering by looking at sum of smallest primes
for i in range(limit):
    if sum(primes[:i]) > limit:
        length = i - 1
        break

answer = None
while length > 1 and answer is None:
    for start in range(len(primes) - length):
        sum_ = sum(primes[start:start + length])
        if sum_ >= limit:
            break
        elif is_prime(sum_):
            answer = sum_
            break
    length -= 1

print(answer)

