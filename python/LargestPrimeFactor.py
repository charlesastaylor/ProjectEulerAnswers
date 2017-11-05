def largestPrimeFactor(x):
    for i in range(2, x):
        if (x % i == 0):
            return largestPrimeFactor(x // i)
    return x


if __name__ == "__main__":
    number = int(input("Enter number: "))
    print("largest prime factor: ", largestPrimeFactor(number))
