with open('input.txt', 'r') as f:
    inp = [[int(char) for char in line.strip()] for line in f]


def common(nums):
    """
    Returns a mapping from bit indices to the most common value in the corresponding bit in numbers in :param nums.
    """
    if len(nums) == 0:
        return {}
    return {k: (1 if sum(num[k] for num in nums) >= len(nums) / 2 else 0) for k in range(len(nums[0]))}


def to_string(lst):
    return ''.join(['1' if b == 1 else '0' for b in lst])


def p1():
    gamma = ''
    ep = ''
    for i, c in sorted(common(inp).items()):
        gamma += '1' if c else '0'
        ep += '0' if c else '1'
    gamma, ep = int(gamma, 2), int(ep, 2)
    print(gamma * ep)


def p2():
    oxy, co, o, c = inp, inp, '0', '0'
    for i in range(len(inp[0])):
        try:
            ocommon = common(oxy)[i]
            ccommon = common(co)[i]
        except KeyError:
            pass  # empty num list only happens when o, c already obtained
        oxy = list(filter(lambda n: n[i] == ocommon, oxy))
        co = list(filter(lambda n: n[i] != ccommon, co))
        if len(oxy) == 1:
            o = int(to_string(oxy[0]), 2)
        if len(co) == 1:
            c = int(to_string(co[0]), 2)
    print(o * c)


if __name__ == '__main__':
    p1()
    p2()
