"""Problem 30 - Digit fifth powers

Just use a time limit to stop looking if we dont find one for 5 seconds since
last. Can set an upper limit mathematically but this works.
"""
from time import time


i = 2
found_time = time()
answer = 0
while time() - found_time < 5:
    if i == sum([int(c)**5 for c in str(i)]):
        answer += i
        found_time = time()
    i += 1

print(answer)
