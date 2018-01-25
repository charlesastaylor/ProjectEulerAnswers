"""Problem 44 - Pentagon numbers

beururhgh
"""

from itertools import combinations

def pent_num(n):
    return int(n * (3*n - 1) / 2)

pent_nums = set([pent_num(x) for x in range(1, 10000)])
d_min=10000
for c in combinations(pent_nums, 2):
    diff = abs(c[0]-c[1])
    if c[0]+c[1] in pent_nums and diff in pent_nums:
        print(c[0], c[1], diff)