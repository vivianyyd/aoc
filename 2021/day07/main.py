with open('input.txt', 'r') as f:
    crabs = [int(x) for x in f.readline().split(',')]


def p1():
    fuel = 0
    crabs.sort()
    position = crabs[round(len(crabs) / 2)]  # median
    for crab in crabs:
        fuel += abs(position - crab)
    print(fuel)


def p2():
    fuel = 0
    position = round(sum(crabs) / len(crabs))  # average. for sample, rounded up. for actual, rounded down. not sure why
    for crab in crabs:
        for dist in range(abs(position - crab)):
            fuel += dist + 1
    print(fuel)


if __name__ == '__main__':
    p1()
    p2()
