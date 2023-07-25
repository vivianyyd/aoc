import numpy as np


class Board:
    def __init__(self, n):
        self.nums = n
        self.marks = np.array([[False for i in range(5)] for j in range(5)])


with open('input.txt', 'r') as f:
    draws = [int(n) for n in f.readline().split(',')]
    nums = {}  # number: (b, row, col) at which [number] appears.
    b = 0  # counter
    boards = []  # Board objs
    board = []
    for line in f:
        line = line.strip()
        if len(line) == 0:
            r = 0  # counter
            if len(board):
                boards.append(Board(board))
                b += 1
            board = []
            continue
        row = []
        for c, num in enumerate(line.split()):
            n = int(num)
            row.append(n)
            if n in nums:
                nums[n].append((b, r, c))
            else:
                nums[n] = [(b, r, c)]
        board.append(row)  # numbers
        r += 1
    boards.append(Board(board))

wins = set()  # same set can be used for both p1 and p2, since p1 checks only up to the first win for the same draws.


def mark_all(draw):
    """ Marks all boards which contain [draw]. """
    try:
        for (b, r, c) in nums[draw]:
            boards[b].marks[r, c] = True
    except KeyError:
        pass  # no boards contain draw


def check():
    """
    Returns the index of a board if it alone has newly won.
    Otherwise, returns None.
    Assumes that the first win is the only board to win on that draw, and similar for the last win.
    """
    new = []
    for ind, bd in enumerate(boards):
        if np.any(np.all(bd.marks, axis=0)) or np.any(np.all(bd.marks, axis=1)):
            if ind not in wins:
                wins.add(ind)
                new.append(ind)
    return new[0] if len(new) == 1 else None


def score(ind, draw):
    """ Calculates the score of the board at index [ind] and [draw]. """
    sm = 0
    for r, row in enumerate(boards[ind].nums):
        for c, num in enumerate(row):
            if not boards[ind].marks[r, c]:
                sm += num
    return sm * draw


def p1():
    for draw in draws:
        mark_all(draw)
        win = check()
        if win:
            print(score(win, draw))
            break


def p2():
    last_score = 0
    for draw in draws:
        mark_all(draw)
        win = check()
        if win:  # unique win
            last_score = score(win, draw)  # score at time of win
    print(last_score)


if __name__ == '__main__':
    p1()
    p2()
