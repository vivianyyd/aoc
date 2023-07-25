with open('../inputs/day_10.txt', 'r') as f:
    adapters = [int(line) for line in f]  # list of joltages

adapters.append(0)
device = max(adapters) + 3
adapters.append(device)
adapters.sort()
diffs = {}

"""
What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?
"""
for i in range(len(adapters)):  # find all joltage differences
    if i is not len(adapters) - 1:
        diff = adapters[i + 1] - adapters[i]
        if diff in diffs:
            diffs[diff] += 1
        else:
            diffs[diff] = 1
print(diffs[1] * (diffs[3]))

"""
What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device?
"""
# consider unweighted digraph where nodes are adapters and edges are valid connections; find total paths to max
a_ways = {0: 1}  # joltage: ways to reach it
for i in range(1, len(adapters)):
    ways = 0
    for j in range(1, 4):  # possible valid differences
        if i - j >= 0 and adapters[i] - adapters[i - j] < 4:  # check for valid differences
            ways += a_ways[adapters[i - j]]
    a_ways[adapters[i]] = ways
print(a_ways[device])
