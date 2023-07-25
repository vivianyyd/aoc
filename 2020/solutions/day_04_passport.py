class Passport:
    """
    A passport which stores its data and checks for validity.
    """
    def __init__(self, data_dict):
        self.data = data_dict

    def byr(self):
        return 1920 <= int(self.data['byr']) <= 2002

    def iyr(self):
        return 2010 <= int(self.data['iyr']) <= 2020

    def eyr(self):
        return 2020 <= int(self.data['eyr']) <= 2030

    def hgt(self):
        h = False  # not all inputs have in/cm
        if self.data['hgt'][-2:] == 'cm':
            h = 150 <= int(self.data['hgt'][:-2]) <= 193
        elif self.data['hgt'][-2:] == 'in':
            h = 59 <= int(self.data['hgt'][:-2]) <= 76
        return h

    def hcl(self):
        return self.data['hcl'][0] == '#' and all(c in '0123456789abcdef' for c in self.data['hcl'][1:])

    def ecl(self):
        return self.data['ecl'] in 'amb blu brn gry grn hzl oth'.split()

    def pid(self):
        return self.data['pid'].isdigit() and len(self.data['pid']) == 9

    def valid(self):
        return self.byr() and self.iyr() and self.eyr() and self.hgt() and self.hcl() and self.ecl() and self.pid()


passports = []
with open('../inputs/day_04.txt', 'r') as f:
    tmp = {}
    for line in f:
        info = line.split()
        if not info:
            passports.append(Passport(tmp))
            tmp = {}
        for e in info:
            key, value = e.split(':')
            tmp[key] = value
    if tmp:  # last line may not be newline, need to add its info
        passports.append(Passport(tmp))

count1 = 0
count2 = 0

for passport in passports:
    if len(set(passport.data.keys()).intersection({'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'})) == 7:
        count1 += 1
        if passport.valid():
            count2 += 1

print(count1)  # part 1: the number of passports with all required fields
print(count2)  # part 2: the number of passports with valid information
