import time


def collatz(start, count=0):
    if start == 1:
        count += 1
        return count
    if start % 2 == 0:
        count += 1
        return collatz(start // 2, count)
    else:  # odd
        count += 1
        return collatz(3 * start + 1, count)


def collatzIter(start):
    count = 1
    while start > 1:
        if start % 2 == 0:  # even
            count += 1
            start = start // 2
            continue
        else:  # odd
            count += 1
            start = 3 * start + 1
            continue
    return count


t0 = time.time()
max = (1, 1)
for i in range(2, 1000000):
    x = collatz(i)
    if x > max[1]:
        max = (i, x)
print(max)
t1 = time.time()
print(t1 - t0)
