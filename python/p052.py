"""Problem 52 - Permuted multiples"""


def digits(x):
    return sorted(list(str(x)))


i = 1
answer = None
while answer is None:
    if all(digits(i) == digits(i * j) for j in range(2, 7)):
        answer = i
    i += 1
print(answer)
