"""Problem 20 - Factorial digit sum

TODO: desc
TODO: put factoiral function in lib and handle invalid input
"""

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(sum([int(c) for c in str(factorial(100))]))
