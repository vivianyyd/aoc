with open('../inputs/day_11.txt', 'r') as f:
    seat_rows = [line.strip() for line in f]
seats = {}
for row in range(len(seat_rows)):
    for seat in range(len(seat_rows[0])):
        seats[(row, seat)] = seat_rows[row][seat]


def print_seats(seating, rows, cols):
    for i in range(rows):
        r = ''
        for j in range(cols):
            r += seating[i, j]
        print(r)
    print('\n')


'''
If a seat is empty (L) and there are no adjacent occupied seats, the seat becomes occupied.
If a seat is occupied (#) and four or more adjacent occupied seats, the seat becomes empty.
'''


def adj(seating, i, j):
    xmin = i - 1 if i > 0 else 0
    xmax = i + 2 if i + 2 <= len(seat_rows) else len(seat_rows)
    ymin = j - 1 if j > 0 else 0
    ymax = j + 2 if j + 2 <= len(seat_rows[0]) else len(seat_rows[0])
    count_adj = 0
    for ind in range(xmin, xmax):
        for jnd in range(ymin, ymax):
            if (ind, jnd) != (i, j) and seating[(ind, jnd)] == '#':
                count_adj += 1
    return count_adj


def new_seats(curr):
    n_seats = {}
    for i, j in curr.keys():
        if curr[(i, j)] == '#' and adj(curr, i, j) >= 4:
            n_seats[(i, j)] = 'L'
        elif curr[(i, j)] == 'L' and adj(curr, i, j) == 0:
            n_seats[(i, j)] = '#'
        else:
            n_seats[(i, j)] = curr[(i, j)]
    return n_seats


def changed(a, b):
    for i, j in a.keys():
        if a[(i, j)] != b[(i, j)]:
            return True


def copy(dic):
    cpy = {}
    for i, j in dic.keys():
        cpy[(i, j)] = dic[(i, j)]
    return cpy


'''
Simulate your seating area by applying the seating rules repeatedly until no seats change state. 
How many seats end up occupied?
'''
old = copy(seats)
new = new_seats(old)
while changed(new, old):
    old = copy(new)
    new = new_seats(old)
count = 0
for key in new.keys():
    if new[key] == '#':
        count += 1
print(count)


'''
Instead, consider the first visible seat in each of those eight directions. 
It now takes five or more visible occupied seats for an occupied seat to become empty. 
'''


def visible(seating, i, j):
    count_vis = 0
    count_vis += in_line(seating, i, j, -1, -1)  # up left
    count_vis += in_line(seating, i, j, -1, 0)  # up
    count_vis += in_line(seating, i, j, -1, 1)  # up right
    count_vis += in_line(seating, i, j, 0, -1)  # mid left
    count_vis += in_line(seating, i, j, 0, 1)  # mid right
    count_vis += in_line(seating, i, j, 1, -1)  # down left
    count_vis += in_line(seating, i, j, 1, 0)  # down
    count_vis += in_line(seating, i, j, 1, 1)  # down right
    return count_vis


def in_line(seating, i, j, del_i, del_j):
    i, j = i + del_i, j + del_j
    while 0 <= i < len(seat_rows) and 0 <= j < len(seat_rows[0]):
        if seating[(i, j)] == '#':
            return 1
        elif seating[(i, j)] == 'L':
            return 0
        i, j = i + del_i, j + del_j
    return 0


def new_seats_1(curr):
    n_seats = {}
    for i, j in curr.keys():
        if curr[(i, j)] == '#' and visible(curr, i, j) >= 5:
            n_seats[(i, j)] = 'L'
        elif curr[(i, j)] == 'L' and visible(curr, i, j) == 0:
            n_seats[(i, j)] = '#'
        else:
            n_seats[(i, j)] = curr[(i, j)]
    return n_seats


'''
Once equilibrium is reached, how many seats now end up occupied?
'''
old = copy(seats)
new = new_seats_1(old)
while changed(new, old):
    old = copy(new)
    new = new_seats_1(old)
count = 0
for key in new.keys():
    if new[key] == '#':
        count += 1
print(count)
