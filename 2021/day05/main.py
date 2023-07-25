from lib import *

points = {}
with open('input.txt', 'r') as f:
    for line in f:
        pts = line.split(' -> ')
        x1, y1 = tuple([int(x) for x in pts[0].split(',')])
        x2, y2 = tuple([int(x) for x in pts[1].split(',')])
        if x1 == x2:  # vertical
            for y in range(min(y1, y2), max(y1, y2) + 1):
                add(points, (x1, y), 1)
        elif y1 == y2:  # horizontal
            for x in range(min(x1, x2), max(x1, x2) + 1):
                add(points, (x, y1), 1)
        # comment out below elif clause for part 1
        elif abs(x1 - x2) == abs(y1 - y2):
            if (x1 < x2 and y1 < y2) or (x2 < x1 and y2 < y1):  # positive slope
                x, y = min(x1, x2), min(y1, y2)
                while x <= max(x1, x2):
                    add(points, (x, y), 1)
                    x, y = x + 1, y + 1
            elif (x1 < x2 and y2 < y1) or (x2 < x1 and y1 < y2):  # negative slope
                x, y = min(x1, x2), max(y1, y2)
                while x <= max(x1, x2):
                    add(points, (x, y), 1)
                    x, y = x + 1, y - 1


if __name__ == '__main__':
    count = 0
    print(sum([1 if n > 1 else 0 for n in points.values()]))
