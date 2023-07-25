with open('../inputs/day_13.txt', 'r') as f:
    time = int(f.readline().strip())
    ids = [int(i) for i in f.readline().strip().replace('x,', '').split(',')]

'''
What is the ID of the earliest bus you can take to the airport multiplied by the number of minutes you'll need to wait for that bus?
'''


def wait(b):
    return (time // b + 1) * b - time


earliest = 0
for bus in ids:
    print('bus:', bus, '; wait:', wait(bus))
    if earliest == 0 or wait(bus) < wait(earliest):
        earliest = bus
print(earliest * wait(earliest))

# failed day 13 part 2 attempt

# with open('../inputs/day_13.txt', 'r') as f:
#     f.readline()
#     lst = [int(i) for i in f.readline().strip().split(',')]

# prod = 1
# for i in range(len(ids) - 1):
#     prod *= i
