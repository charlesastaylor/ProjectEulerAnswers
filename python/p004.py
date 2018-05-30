"""Problem 4 - Largest palindrome product"""
from eulerlib import is_palindrome

largest = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        prod = i*j
        if prod>largest and is_palindrome(str(prod)):
            largest=prod

print(largest)
