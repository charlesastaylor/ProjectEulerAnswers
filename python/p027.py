"""Problem 27 - Quadratic primes.

Can use sieve to generate primes up to 1000 then look use this set rather than
use is_prime method at every step which halfs run time. But, can't think of a 
way to limit primes. Using primes < 1000 works but can't prove it.
"""

from itertools import count
from eulerlib import is_prime

ans = (0, 0, 0) # (a, b, #primes)
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        for n in count(0):
            if not is_prime(n**2 + a*n + b):
                if n > ans[2]:
                    ans = (a, b, n)
                break
print(ans[0] * ans[1])
