from math import pow
import numpy as np

with open('input.txt', 'r') as f:
    inp = [line for line in f]


def p1():
    count = 0
    with open('input.txt', 'r') as f:
        for line in f:
            l = line.split('|')
            words = l[1].split(' ')
            for w in words:
                n = len(w.strip())
                if n == 2 or n == 3 or n == 7 or n == 4:
                    count += 1
    print(count)


def add(dic, k, v):  # lib add but for list
    if k in dic:
        dic[k].append(v)
    else:
        dic[k] = [v]


def p2():
    bigs = 0
    with open('input.txt', 'r') as f:
        for line in f:
            poss = {}  # orig: new poss. restraints
            l = line.split('|')
            words = l[0].split(' ')
            words = sorted(words, key=len)
            for w in words:
                w = w.strip()
                n = len(w)
                if n == 2:
                    for c in w:
                        add(poss, 'c', c)
                        add(poss, 'f', c)
                elif n == 3:
                    for c in w:
                        if c not in poss['c'] and c not in poss['f']:
                            add(poss, 'a', c)
                elif n == 4:
                    for c in w:
                        if c not in poss['c'] and c not in poss['f']:
                            add(poss, 'b', c)
                            add(poss, 'd', c)
                elif n == 7:
                    for c in w:
                        if c not in poss['c'] and c not in poss['f'] and c not in poss['b'] and c not in poss['d'] and c not in poss['a']:
                            add(poss, 'e', c)
                            add(poss, 'g', c)
            valid = {'abcefg': 0, 'cf': 1, 'acdeg':2, 'acdfg':3, 'bdcf':4, 'abdfg':5, 'abdefg':6, 'acf':7, 'abcdefg':8, 'abcdfg':9}
            final = {}
            for i in range(8):  # cf bd eg
                eg = i % 2
                i = i >> 1
                bd = i % 2
                i = i >> 1
                cf = i % 2
                print(eg, bd, cf)
                tmp = {'a': poss['a'][0],  # original : new
                       'c': poss['c'][cf], 'f': poss['c'][not cf],
                       'b': poss['b'][bd], 'd': poss['b'][not bd],
                       'e': poss['e'][eg], 'g': poss['e'][not eg]}
                if tryit(tmp):
                    print('tmp', tmp)
                    final = {v: k for k, v in tmp.items()}  # new : original
            outp = l[1].split(' ')
            s = 0
            pv = 3
            for o in outp:
                o = o.strip()
                for digit in o:
                    print(final)
                    res = replacea(digit, final)  # replaces all chars in digit with maps from final
                    num = 0
                    for val in valid.keys():
                        match = True
                        for ch in val:
                            if ch not in res:
                                match = False
                        if match:
                            num = valid[val]
                            s += pow(10, pv) * num
                            break
            bigs += s
        print(bigs)


def replacea(digit, final):
    s = ''
    for ch in digit:
        s += final[ch]
    return s


def tryit(tmp):
    vl = {'abcefg': 0, 'cf': 1, 'acdeg': 2, 'acdfg': 3, 'bdcf': 4, 'abdfg': 5, 'abdefg': 6, 'acf': 7,
          'abcdefg': 8, 'abcdfg': 9}
    new = set()
    for word in vl:
        s = ''
        for ch in word:
            s += tmp[ch]
        new.add(s)
    for s in new:
        if s in vl.keys():
            del vl[s]
        else:
            return False
    return True


if __name__ == '__main__':
    p1()
    p2()
