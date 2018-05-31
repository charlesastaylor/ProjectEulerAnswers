"""Problem 53 - Combinatoric selections"""
from eulerlib import choose


answer = 0
for n in range(1, 101):
    for r in range(0, n + 1):
        if choose(n, r) > 1000000:
            answer += 1
print(answer)
