# In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

# Data - located in data/p11.txt

# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?


from functools import reduce


def readData(file):
    f = open(file, "r")
    rows = f.read().splitlines()
    matrix = []
    for row in rows:
        matrix.append([int(x) for x in row.split(" ")])
    return matrix


def sequence(grid, row, col):
    width = len(grid[row])
    height = len(grid)

    # # left -> right
    if col + 4 <= width:
        yield grid[row][col:col + 4]

    # top -> bottom
    if row + 4 <= height:
        yield list(grid[row + n][col] for n in range(4))

    # diagonally left -> right
    if col + 4 <= width and row + 4 <= height:
        yield list(grid[row + n][col + n] for n in range(4))

    # diagonally left -> right
    if col >= 3 and row + 4 <= height:
        yield list(grid[row + n][col - n] for n in range(4))


def main():
    matrix = readData("data/p11")

    max = 0

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            for line in sequence(matrix, row, col):
                c = reduce(lambda x, y: x * y, line)
                if c > max:
                    max = c

    print(max)

main()