"""Problem 26 - Reciprocal cycles

Tried to solve quickly rather than properly, ended up not working.
"""

from decimal import *

PREC = 400
setcontext(Context(prec=PREC))
D=Decimal # shorthand
max = (0, 0) # (d, length of repetend)
for d in range(2, 1000):
    # Do the division, convert to string and strip leading '0.'
    x = str(1 / D(d))[2:]
    
    if len(x) < PREC: continue # non recurring
    
    for start in range(PREC):
        for size in range(1, (PREC - start) // 2):
            repetend = x[start:start + size]
            repetend_found = True
            for i in range(1, 10):
                if x[start + size * i:start + size * (i + 1)] != repetend:
                    if start + size * (i + 1) > len(x) - 1: break
                    repetend_found = False
                    break
            if repetend_found: break
        if repetend_found: break
    if len(repetend) > max[1]:
        max = (d, len(repetend))

print(max)


