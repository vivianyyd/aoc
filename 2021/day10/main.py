with open('input.txt', 'r') as f:
    inp = [line for line in f]

ope = ['(', '[', '{', '<']
close = [')', ']', '}', '>']


def opp(ch):
    if ch in ope:
        return close[ope.index(ch)]
    else:
        return ope[close.index(ch)]


if __name__ == '__main__':
    illeg, autocomp_scores = [], []
    for line in inp:
        unclosed, stacc, delete = [], [], False
        for c in line.strip():
            if c in ope:
                stacc.append(c)
            elif c == opp(stacc[len(stacc) - 1]):
                del stacc[len(stacc) - 1]
            else:
                delete = True
                illeg.append(c)
                break
        if delete:
            continue
        if len(stacc):  # leftover opens
            unclosed.extend(stacc)

        auto_sc = 0  # per-line autocomplete score
        unclosed.reverse()
        for c in unclosed:
            auto_sc *= 5
            auto_sc += 1 if c == '(' else 2 if c == '[' else 3 if c == '{' else 4 if c == '<' else 0
        autocomp_scores.append(auto_sc)

    error_score = 0  # overall syntax error score
    for c in illeg:
        error_score += 3 if c == ')' else 57 if c == ']' else 1197 if c == '}' else 25137 if c == '>' else 0

    print(error_score)
    autocomp_scores.sort()
    print(autocomp_scores[int((len(autocomp_scores) / 2) - 0.5)])
