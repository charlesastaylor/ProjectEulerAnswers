"""Problem 40 - Champernowne's constant"""
s = ""
i = 0
while len(s) <= 1000000:
    s += str(i)
    i += 1
answer = 1
for i in range(7):
    answer *= int(s[10**i])
print(answer)
