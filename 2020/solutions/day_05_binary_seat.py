def seat(fblr, row_col):
    """
    Find the seat row or column number.
    :param fblr: the series of "halves" of the partitions the seat is in
    :param row_col: whether a row or column number is being determined
    :return: the seat's row or column number
    """
    min = 0
    if row_col == 'row':
        max = 127
    elif row_col == 'col':
        max = 7
    for ch in fblr:
        if ch == 'F' or ch == 'L':
            max -= (max - min + 1) / 2
        elif ch == 'B' or ch == 'R':
            min += (max - min + 1) / 2
    return max


high_id = 0
id_list = []
with open('../inputs/day_05.txt', 'r') as f:
    for line in f:
        seat_id = 8 * seat(line[:7], 'row') + seat(line[7:], 'col')
        id_list.append(seat_id)
        if seat_id > high_id:
            high_id = seat_id

print(high_id)  # part 1: find the highest seat ID

id_list.sort()
for i in range(len(id_list) - 2):
    if id_list[i + 1] != id_list[i] + 1:
        print(id_list[i] + 1)  # part 2: find the missing seat ID, given it's in the middle of the plane
