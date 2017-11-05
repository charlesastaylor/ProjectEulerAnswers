''' Could have just used first 11 digits of each number as 12th+ digits
    can never affect the resulting sum.
'''
file=open("numbers.txt")
numbers=[int(line) for line in file]

print(str(sum(numbers))[:10])