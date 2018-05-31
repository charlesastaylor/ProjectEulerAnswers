"""Problem 48 - Self powers"""
sum_ = 0
for i in range(1, 1001):
    sum_ += i**i
print(str(sum_)[-10:])
