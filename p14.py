# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# Initialize the memo dictionary
memo = {}
def collatz_seq(n):
    # Check if already computed
    if not n in memo:
        # If not compute it
        if n == 1:
            # Cache it
            memo[n] = 1
        elif n % 2 == 0:
            memo[n] = collatz_seq(n // 2) + 1
        else:
            memo[n] = collatz_seq(3*n + 1) + 1
    # Return it
    return memo[n]


max = 0
result = 0
for i in range(2, 1000000):
    seq = collatz_seq(i)
    if seq > max:
        max = seq
        result = i

print("Result:", result)
