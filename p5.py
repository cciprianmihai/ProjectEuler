# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


num = 0
keepGoing = True


while keepGoing:
    # increment num by 20 each time
    num += 20

    # NumMultiples keeps track of the number of multiples for num
    numMultiples = 0

    # Iterate from 20 to 11 going down by 1
    for i in range(20, 10, -1):
        if (num % i != 0):
            # If not evenly divisible, break out of for loop
            #  because we know it isn't the LCM
            break
        if (i == 11):
            # If we reached here without breaking, then we've
            #  found the number we're looking for.
            # Change keepGoing to False to break out of while loop
            keepGoing = False
            break

    # Print out current num to keep track (in millions)
    if num % 1000000 == 0:
        print(num / 1000000)

print('The lowest common multiple is: ' + str(num))