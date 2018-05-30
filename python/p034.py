"""Problem 34 - Digit factorials

Rough upper limit taken as 7 * 9! < 9999999.
"""
from math import factorial


i = 3
upper_limit = 9999999
while i < upper_limit:
    if i == sum([factorial(int(c)) for c in str(i)]):
        print(i)
    i += 1
