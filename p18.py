# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
#    3
#   7 4
#  2 4 6
# 8 5 9 3
# That is, 3 + 7 + 4 + 9 = 23.
# Find the maximum total from top to bottom of the triangle below (data/p18.txt).

data = open ( "data/p18" )

triangle = []
for read in data.readlines():
    line = [int(value) for value in read.split()]
    triangle.append(line)

data.close()

triangle.reverse()

for row in range(1,14):
    for index in range(len(triangle[row])):
        triangle[row][index] += max(triangle[row-1][index], triangle[row-1][index+1])

triangle[14][0] += max(triangle[13][0],triangle[13][1])

print(triangle[14][0])