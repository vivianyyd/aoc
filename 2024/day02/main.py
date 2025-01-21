with open('input.txt', 'r') as f:
    inp = [[int(n) for n in line.split()] for line in f]

count = 0
for row in inp:
    if row[1] > row[0]:
        flag = 'inc'
    else:
        flag = 'dec'

    # for each row, make list of differences
    # check if all pos or neg except for 1
    for i in range(len(row) - 1):
        if row[i] > row[i + 1] and flag == 'inc':
            count += 1
            break
        elif row[i] < row[i + 1] and flag == 'dec':
            count += 1
            break
        elif abs(row[i] - row[i + 1]) > 3 or abs(row[i] - row[i + 1]) < 1:
            count += 1
            break
        else:
            continue



print(len(inp) - count)
# l1 = [int(l[0]) for l in inp]
# l2 = [int(l[1]) for l in inp]
#
# l1.sort()
# l2.sort()


# print(sum([l2.count(e)*e for e in set(l1)]))

# dists = [abs(l1[i]-l2[i]) for i in range(len(l1))]
# print(sum(dists))
