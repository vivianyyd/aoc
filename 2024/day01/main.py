with open('input.txt', 'r') as f:
    inp = [line.split() for line in f]

l1 = [int(l[0]) for l in inp]
l2 = [int(l[1]) for l in inp]

l1.sort()
l2.sort()


print(sum([l2.count(e)*e for e in set(l1)]))

#dists = [abs(l1[i]-l2[i]) for i in range(len(l1))]
#print(sum(dists))


