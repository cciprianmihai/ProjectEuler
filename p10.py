# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

import math


def is_prime(n):
    """
    Assumes that n is a positive natural number
    """
    # We know 1 is not a prime number
    if n == 1:
        return False

    # This will loop from 2 to sqrt(n)
    for i in range(2, int(math.sqrt(n)) + 1):
        # Check if i divides n, if yes, we return False
        if n % i == 0:
            return False
    return True


print(sum([x for x in range(1, 2000000, 2) if is_prime(x)]) + 2)