# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6
# routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?

# Import factorial from math module
from math import factorial

# import time from time to calculate exection time
from time import time

# time at the start of execution
start = time()

# binomial coefficient function
# https://en.wikipedia.org/wiki/Binomial_coefficient
def nck(n,k):
	# function which will return the binomial coefficient of n,k
	return factorial(n)/(factorial(k)*factorial(n-k))

# Number of lattice paths from (0,0) to (a,b) is given by
# binomial coefficient C(a+b,a)
print('Number of lattice paths is: '+str(nck(20+20,20)))

# time at the end of program execution
end = time()

# Printing the total time
print(end-start)