"""Problem 36 - Double-base palindromes"""
from eulerlib import is_palindrome


answer = 0
for i in range(1000000):
    if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]):
        answer += i

print(answer)
