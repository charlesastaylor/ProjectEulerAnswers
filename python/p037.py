"""Problem 37 - Truncatable primes"""
from eulerlib import is_prime, primes


def truncatable(x):
    s = str(x)
    if len(s) <= 1:
        return False
    for i in range(len(s)):
        if not is_prime(int(s[i:])) or not is_prime(int(s[:i + 1])):
            return False
    return True

L = []
for prime in primes():
    if truncatable(prime):
        L.append(prime)
        print(prime)
        if len(L) == 11:
            break

print(sum(L))
