with open('input.txt', 'r') as f:
    inp = [[int(n) for n in line.strip()] for line in f]


def adj(coords):
    i, j = coords
    ad = [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]
    for r, c in ad:
        if 0 <= r < len(inp) and 0 <= c < len(inp[0]):
            yield r, c


low = set()


def p1():
    s = 0
    for i, row in enumerate(inp):
        for j, val in enumerate(row):
            lower = True
            for r, c in adj((i, j)):
                if val >= inp[r][c]:
                    lower = False
            if lower:
                low.add((i, j))
                risk = val + 1
                s += risk
    print(s)


def p2():
    sizes = []
    for r, c in low:  # bfs for each low point
        basin = {(r, c)}
        frontier = [pair for pair in adj((r, c))]
        while len(frontier):
            i, j = frontier[0]
            if inp[i][j] != 9:
                basin.add(frontier[0])
                frontier.extend(pair for pair in adj(frontier[0]) if pair not in basin)
            del frontier[0]
        sizes.append(len(basin))
    prod = 1
    sizes.sort(reverse=True)
    for s in sizes[0:3]:
        prod *= s
    print(prod)


if __name__ == '__main__':
    p1()
    p2()
