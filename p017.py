"""Problem 17 - Number letter counts

Package num2words used for the heavy lifting.
"""

from num2words import num2words

UPPER_LIMIT = 1000

total = 0
for i in range(1, UPPER_LIMIT + 1):
    total += len(num2words(i).replace(' ', '').replace('-', ''))

print("The numbers 1 to {} (inclusive) written as words use:\n"
      "{} letters.".format(UPPER_LIMIT, total)
     )
