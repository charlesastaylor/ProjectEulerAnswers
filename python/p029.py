"""Problem 29 - Distinct powers"""

S = set()
for i in range(2,101):
    for j in range(2,101):
        S.add(i**j)
print(len(S))