# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

# Import math library to get sqrt
import math


# isPrime function - returns True or False
def isPrime(num):
    # Iterates from 2 to sqrt(num)+1 as discussed above
    # Make sure to convert sqrt to int for range
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i == 0):
            return False

    return True


count = 1  # Number of primes
num = 2  # Prime number (count)

# While loop to continue until we reach 100001th prime
while (count < 10001):
    num += 1
    if isPrime(num):
        # print('Found a prime: ' + str(num) + ', prime number: ' + str(count))
        # If a prime is found, increase count and continue
        count += 1

# Print answer
print('The 10001th prime is: ' + str(num))