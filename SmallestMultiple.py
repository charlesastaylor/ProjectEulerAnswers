limit = int(input("Upper Limit:"))

n = 2520

while not all([n % i == 0 for i in range(2, limit + 1)]):
    n += 2520

print(n)


#232792560