"""Problem 3 - Largest prime factor"""
def largest_prime_factor(x):
    for i in range(2, x):
        if (x % i == 0):
            return largest_prime_factor(x // i)
    return x

print(largest_prime_factor(600851475143))
