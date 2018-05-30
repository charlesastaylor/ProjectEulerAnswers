"""Common classes and functions used in project euler problems

TODO: Maybe should use sympy for some number theory stuff, eg has a nice sieve
class.
"""

from functools import partial, lru_cache
from math import sqrt


# Prime numbers
@lru_cache(maxsize=None)
def is_prime(x):
    """Tests if x is a prime number."""
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def get_primes(n):
    """Return set of all primes <= n."""
    if n <= 1:
        raise ValueError("get_primes: no primes <= 1")
    L = [True] * (n + 1)
    for i in range(2, int(sqrt(n) + 1)):
        if L[i]:
            for j in range(i**2, n + 1, i):
                L[j] = False
    return {i for i, prime in enumerate(L) if i > 1 and prime}

def primes(start=1, stop=None, step=1):
    """Prime number generator"""
    i = start
    while stop is None or i < stop:
        if is_prime(i):
            yield i
        i += step

def prime_factors(x):
    """Return list of prime factors of x

    TODO: make better or use sympy
    """
    if x == 1:
        return []

    L = []
    while not is_prime(x):
        for prime in primes():
            if x % prime == 0:
                L.append(prime)
                break
        x //= prime
    L.append(x)
    return L

# Other

def is_palindrome(s):
    # TODO: Might be more efficient for large strings
    # return all([s[i] == s[~i] for i in range(len(s) // 2)])    
    return s == s[::-1]
    