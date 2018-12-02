count2 = 0
count3 = 0
import collections
import itertools
import difflib
with open("input.txt") as f:
    for line in f:
        d = collections.Counter(line)
        c2 = False
        c3 = False
        for i in d.values():
            if(i == 2):
                c2 = True
            if(i == 3):
                c3 = True
        if(c2):
            count2 += 1
        if(c3):
            count3 += 1
print("Answer 1: " + str(count2 * count3))
checksums = []
with open("input.txt") as f:
    for line in f:
        checksums.append(line.rstrip())
length = len(checksums[0])
for a, b in itertools.combinations(checksums,2):
    l = [i for i,(a1,a2)  in enumerate(zip(a,b)) if a1!=a2]
    if(len(l) == 1):
        print("Answer 2: " + a[:l[0]] + a[l[0]+1:])

