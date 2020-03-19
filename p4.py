# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


def isPal(num):
    numString = str(num)
    for i in range(0, int(len(numString) / 2) + 1):
        if numString[i] != numString[-i - 1]:
            return False
    return True


# Keep track of max product
maxProduct = 0

# Keep track of values used for max product
max1, max2 = 0, 0

# Iterate from 999 to 99 going down for both values
# Generate a product and determine if it's a palindrome
# If it is a palindrome, determine if it is max
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        product = i * j
        if isPal(product):
            if product > maxProduct:
                maxProduct = product
                max1, max2 = i, j

# Print answers
print('The largest palindromic product is: ' + str(maxProduct))
print(str(maxProduct) + ' = ' + str(max1) + ' * ' + str(max2))