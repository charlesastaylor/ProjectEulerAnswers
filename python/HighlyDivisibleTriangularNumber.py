from math import sqrt


def numFactors(x):
    count = 0
    for i in range(1, int(sqrt(x)) + 1):
        if x % i == 0:
            if x // i == i:
                count += 1
            else:
                count += 2
    return count


i = 1
while True:
    tri = (i ** 2 + i) // 2
    if numFactors(tri) > 500:
        break
    i += 1
print(tri)
