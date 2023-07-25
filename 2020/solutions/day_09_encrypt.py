def has_pair(total):
    """
    Check whether there is a pair in the previous 25 numbers which sum to the desired total.
    :param total: the desired total
    :return: true if there is a pair which sums to total, false otherwise
    """
    pair = False
    for i, j in unique_pairs(len(previous_25)):
        if previous_25[i] + previous_25[j] == total:
            pair = True
    return pair


def unique_pairs(nums):
    """
    Generate all unique pairs of numbers in the interval [0, nums).
    :param nums: the upper bound of numbers
    :return: the unique pairs
    """
    for i in range(nums):
        for j in range(i + 1, nums):
            yield i, j


def part_one():
    """
    Find the first number in check after the preamble which is not the sum of two of the 25 numbers before it.
    :return: the desired number
    """
    for i in range(len(check)):
        curr = check[i]
        if not has_pair(curr):
            return curr
        previous_25.pop(0)
        previous_25.append(curr)


def part_two():
    """
    Find a contiguous set of at least two numbers in the data which sum to the invalid number from part 1.
    :return: the sum of the smallest and largest values in the contiguous range
    """
    for i in range(len(ls)):
        currind = i
        summ = ls[currind]
        while summ < part_one_sol:
            currind += 1
            summ += ls[currind]
        rng = ls[i:currind]
        if summ == part_one_sol:
            return max(rng) + min(rng)


ls = [int(line) for line in open('../inputs/day_09.txt', 'r').read().split('\n') if line]
previous_25 = ls[0:25]  # 25 numbers preceding that being checked
check = ls[25:]  # numbers to check begin after the 25-number preamble

part_one_sol = part_one()
print('Part 1:', part_one_sol)
print('Part 2:', part_two())
