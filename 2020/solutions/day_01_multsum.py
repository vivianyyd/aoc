def sum_multiply_pair(total):
    """
    Find the product of the two entries that sum to a number.
    :param total: the number being checked for
    :return: the product of entries which add to total
    """
    for i, j in unique_groups(len(ls), 2):
        if ls[i] + ls[j] == total:
            print(ls[i] * ls[j])
            break


def sum_multiply_triplet(total):
    """
    Find the product of the three entries that sum to a number.
    :param total: the number being checked for
    :return: the product of entries which add to total
    """
    for i, j, k in unique_groups(len(ls), 3):
        if ls[i] + ls[j] + ls[k] == total:
            print(ls[i] * ls[j] * ls[k])
            break


def unique_groups(nums, group_size):
    """
    Generate all unique subgroups of a certain size.
    :param nums: the group from which subgroups are made
    :param group_size: the size of the subgroups. Requires: either 2 or 3
    :return: the unique subgroups
    """
    for i in range(nums):
        for j in range(i + 1, nums):
            if group_size == 2:
                yield i, j
            else:
                for k in range(j + 1, nums):
                    yield i, j, k


ls = [int(line) for line in open('../inputs/day_01.txt', 'r').read().split('\n')]
sum_multiply_pair(2020)
sum_multiply_triplet(2020)
