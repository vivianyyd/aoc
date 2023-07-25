import numpy as np

with open('input.txt', 'r') as f:
    inp = [[int(x) for x in line.strip()] for line in f]


def adj(coords):
    """
    I f***ing love generators
    :return: The coordinates of the entries adjacent to [coords], if they
    are in-bounds of inp.
    """
    i, j = coords
    ad = [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j), (i - 1, j - 1),
          (i - 1, j + 1), (i + 1, j + 1), (i + 1, j - 1)]
    for r, c in ad:
        if 0 <= r < len(inp) and 0 <= c < len(inp[0]):
            yield r, c


def step():
    flashes = 0
    flashed = [[0 for c in range(len(inp[0]))] for r in range(len(inp))]
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            inp[i][j] += 1
    orig_flashes = 1  # placeholder because no do-while :(
    while orig_flashes != flashes:
        orig_flashes = flashes
        for i in range(len(inp)):
            for j in range(len(inp[0])):
                if inp[i][j] > 9:
                    for r, c in adj((i, j)):
                        if not flashed[i][j]:
                            inp[r][c] += 1
                    if not flashed[i][j]:
                        flashes += 1
                        flashed[i][j] = 1
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            if flashed[i][j]:
                inp[i][j] = 0
    return flashes


def p1():
    """
    First, the energy level of each octopus increases by 1.
    Then, any octopus with an energy level greater than 9 flashes.
    This increases the energy level of all adjacent octopuses by 1,
    including octopuses that are diagonally adjacent. If this causes
    an octopus to have an energy level greater than 9, it also flashes.
    This process continues as long as new octopuses keep having their
    energy level increased beyond 9. (An octopus can only flash at
    most once per step.)
    Finally, any octopus that flashed during this step has its energy
    level set to 0, as it used all of its energy to flash.
    """
    # print(inp)
    # flash = 0
    # for i in range(100):
    #     print(np.array(inp))
    #     flash += step()
    # print(flash)
    # flashes if path to nearest nine is difference to nine


def p2():
    count = 0
    run = True
    while run:
        count += 1
        step()
        if np.sum(inp) == 0:
            run = False
    print(count)


if __name__ == '__main__':
    p1()
    p2()
