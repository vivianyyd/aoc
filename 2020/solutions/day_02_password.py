"""
Part 1:
    The password policy indicates the lowest and highest number of times a given letter must appear in a valid password.
    For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.
Part 2:
    The policy describes two positions in the password, where the password is 1-indexed.
    Exactly one of these positions must contain the given letter.
"""
ls = []
valid1, valid2 = 0, 0
for line in open('../inputs/day_02.txt', 'r').read().split('\n'):
    first, line = line.replace(':', '').split('-')
    second, letter, password = line.split(' ')
    if int(first) <= password.count(letter) <= int(second):
        valid1 += 1
    if (password[int(first) - 1] == letter) ^ (password[int(second) - 1] == letter):
        valid2 += 1

print(valid1)  # the number of valid passwords for part 1
print(valid2)  # the number of valid passwords for part 2
