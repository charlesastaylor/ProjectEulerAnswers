"""Problem 25 1000-digit Fibonacci number

Straightfoward (ugly) brute force method.
"""
n_minus_1 = n_minus_2 = 1
i = 3
while True:
    tmp = n_minus_1
    n_minus_1 = n_minus_1 + n_minus_2
    if len(str(n_minus_1)) == 1000:
        print(i)
        break
    n_minus_2 = tmp
    i += 1