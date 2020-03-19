# The sum of the squares of the first ten natural numbers is, 1^2+2^2+...+10^2=385

# The square of the sum of the first ten natural numbers is, (1+2+...+10)^2=55^2=3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# Keep track of the sum of the squares
sumSquare = 0

# Keep track of the the sums
sums = 0

# Iterate through numbers [1:100] 1-100 inclusevely
for i in range(1, 101):
    sumSquare += i * i
    sums += i

# Square the individuals sums to find square of sums
squareSum = sums * sums

# Print answers
print('The sum of the squares is: ' + str(sumSquare))
print('The square of the sums is: ' + str(sums))
print('The difference is: ' + str(squareSum - sumSquare))