with open('day1/input.txt', 'r') as f:
    inp = [int(line) for line in f]

count1 = 0
for i, v in enumerate(inp):
    count1 += 1 if v > inp[i - 1] and i > 0 else 0
print(count1)

count2 = 0
for i, v in enumerate(inp):
    count2 += 1 if sum(inp[i - 3:i]) > sum(inp[i - 4:i - 1]) and i > 2 else 0
print(count2)
