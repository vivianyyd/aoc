with open('../inputs/day_08.txt', 'r') as f:
    program = [line.strip().split() + [False] for line in f]  # [[key, param, seen]* ]

default_program = [line[:] for line in program]  # construct a default program to reset keys and seen value


def run(accu, i, key):
    """
    Run the i-th line of the program
    :param accu: the current accumulator
    :param i: the line of the program to run
    :param key: the key of the line (may not be equal to program[i])
    :return: the accumulator, index of the next line to run
    """
    global program
    param = int(program[i][1])
    program[i][2] = True
    if key == 'jmp':
        i += param - 1
    elif key == 'acc':
        accu += param
    i += 1
    return accu, i


"""
Run the program until a line is reached which has already been seen; 
print the accumulator immediately before any instruction is executed a second time
"""
accu, i = 0, 0
while not program[i][2]:
    accu, i = run(accu, i, program[i][0])
print('Part 1:', accu)
program = [line[:] for line in default_program]  # reset seen values


switch = []  # indices of jmps and nops to be switched
for r in range(len(program)):
    if program[r][0] == 'jmp' or program[r][0] == 'nop':
        switch.append(r)

"""
Switch each jmp or nop in turn and run until the program exits without looping
"""
for j in switch:
    accu, i = 0, 0
    while not program[i][2]:
        key = program[i][0]
        if i == j:
            if key == 'nop':
                key = 'jmp'
            else:
                key = 'nop'
        accu, i = run(accu, i, key)
        if i == len(program):
            print('Part 2:', accu)
            break
    program = [line[:] for line in default_program]  # reset jmp/nop and seen value
