import math

with open('../inputs/day_12.txt', 'r') as f:
    insns = [(line.strip()[0], int(line.strip()[1:])) for line in f]
pos = [0, 0, 0]  # degree starts from +x axis

"""
What is the Manhattan distance between that location and the ship's starting position?
"""


def move(instruction):
    direc, val = instruction
    if direc == 'N':
        pos[1] += val
    elif direc == 'S':
        pos[1] -= val
    elif direc == 'E':
        pos[0] += val
    elif direc == 'W':
        pos[0] -= val
    elif direc == 'L':
        pos[2] = (pos[2] + val) % 360
    elif direc == 'R':
        pos[2] = (pos[2] - val) % 360
    elif direc == 'F':
        ang = math.radians(pos[2])
        pos[0] += val * math.cos(ang)
        pos[1] += val * math.sin(ang)


for insn in insns:
    move(insn)
print(abs(pos[0]) + abs(pos[1]))


"""
The instructions actually indicate how to move a waypoint which is relative to the ship's position.
What is the Manhattan distance between that location and the ship's starting position?
"""
ship = [0, 0]
wp = [10, 1]


def move_wp(instruction):
    direc, val = instruction
    if direc == 'N':
        wp[1] += val
    elif direc == 'S':
        wp[1] -= val
    elif direc == 'E':
        wp[0] += val
    elif direc == 'W':
        wp[0] -= val
    elif direc == 'L' or direc == 'R':
        if direc == 'R':
            val = 360 - val
        ang = math.radians(val)
        np = [math.cos(ang) * wp[0] - math.sin(ang) * wp[1], math.sin(ang) * wp[0] + math.cos(ang) * wp[1]]
        wp[0], wp[1] = np[0], np[1]
    elif direc == 'F':
        for i in range(val):
            ship[0] += wp[0]
            ship[1] += wp[1]


for insn in insns:
    move_wp(insn)
print(abs(ship[0]) + abs(ship[1]))
