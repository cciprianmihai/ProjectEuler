# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def triplet():
    for a in range(1,1001):
        for b in range(a, 1001):
            c = 1000 - (a + b)
            if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                return a * b * c


print("Product is:", triplet())