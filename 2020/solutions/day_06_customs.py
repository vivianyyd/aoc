count_1, count_2 = 0, 0  # updated after each group
default = set('abcdefghijklmnopqrstuvwxyz')  # set of all possible questions

with open('../inputs/day_06.txt', 'r') as f:
    tmp1 = []
    tmp2 = default
    for line in f:
        line = line[:-1]
        if not line:
            count_1 += len(set(tmp1))
            count_2 += len(tmp2)
            tmp1 = []
            tmp2 = default
        else:
            for e in line:
                tmp1 += e
            tmp2 = tmp2.intersection(set(line))
    if tmp1:  # last line in file not blank
        count_1 += len(set(tmp1))
        count_2 += len(tmp2)

print(count_1)  # the number of questions to which anyone in the group answered yes, summed over all groups
print(count_2)  # the number of questions to which everyone in the group answered yes, summed over all groups
