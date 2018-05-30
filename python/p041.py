"""Problem 41 - Pandigital prime"""
from itertools import permutations

from eulerlib import is_prime


answer = None
length = 9
while length > 0 and answer is None:
    for perm in permutations(range(length, 0, -1)):
        num = int("".join(str(c) for c in perm))
        if is_prime(num):
            answer = num
            break
    length -= 1

print(answer)
