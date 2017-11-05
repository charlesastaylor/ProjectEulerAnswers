def isPalindrome(s):
    return all([s[i] == s[~i] for i in range(len(s) // 2)])

largest = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        prod = i*j
        if prod>largest and isPalindrome(str(prod)):
            largest=prod

print(largest)