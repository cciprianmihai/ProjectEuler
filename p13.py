# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.


def result(file):
    strSum = str(sum([int(n) for n in open(file, "r").read().splitlines()]))[::-1]
    print(strSum[len(strSum)-10:len(strSum)][::-1])


result("data/p13")