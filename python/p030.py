"""Problem 30 - Digit fifth powers

Can't brute force it in reasonale time. Maybe look at combinations of digits
that power sum to in the correct then see if they permute to a suitable digit
"""

POW = 4
# for i in range(2, 10000000):
#     if i == sum([int(d)**POW for d in str(i)]): print(i)

for i in range(0, 10):
    print("No digits: {}  Number: {} - {}  Power sum: {} - {}".format(
        i + 1, 10**i, 10**(i + 1) - 1, 1 * (i + 1), 9**POW * (i + 1))
        )

