"""Problem 26 - Reciprocal cycles

Same approach but slightly more concise than mine -
https://projecteuler.net/thread=26#1698
"""

def len_recurring_cycle(n):
    """Return the length of recurring cycle of 1/n.

    Use long division to calculate the length of the recurring part of the
    decimal representation of the unit fraction 1/n.
    Returns 0 if 1/n is non recurring/
    """
    i = 0
    while 10**i // n <= 0:
        i += 1
    dec = '0' * (i - 1)
    tmp = 10**i
    cache = {}
    while True:
        if tmp == 0:
            return 0
        elif tmp in cache:
            return len(dec[cache[tmp]:])
        dec += str(tmp // n)
        cache[tmp] = len(dec) - 1
        tmp = (tmp % n) * 10 # *10 corresponds to bringing down next 0

d_max = (0, 0)
for d in range(1, 1000):
    _len = len_recurring_cycle(d)
    if _len > d_max[1]:
        d_max = (d, _len)

print(d_max[0])
