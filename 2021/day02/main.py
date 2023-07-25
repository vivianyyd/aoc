depth1 = 0
hor1 = 0
depth2 = 0
hor2 = 0
aim = 0

with open('input.txt', 'r') as f:
    for line in f:
        direc = line.strip().split()[0]
        val = int(line.strip().split()[1])
        if direc == 'forward':
            hor1 += val
            hor2 += val
            depth2 += aim * val
        elif direc == 'down':
            depth1 += val
            aim += val
        elif direc == 'up':
            depth1 -= val
            aim -= val

print(hor1 * depth1)
print(hor2 * depth2)
