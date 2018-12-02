import collections
import itertools

with open("input.txt") as f:
    count2 = 0
    count3 = 0
    checksums = [x.rstrip() for x in f.readlines()]
    for line in checksums:
        d = list(collections.Counter(line).values())
        if(2 in d):
            count2 += 1
        if(3 in d):
            count3 += 1
    print("Answer 1: " + str(count2 * count3))
    
    for a, b in itertools.combinations(checksums,2):
        l = [i for i,(a1,a2)  in enumerate(zip(a,b)) if a1!=a2]
        if(len(l) == 1):
            print("Answer 2: " + a[:l[0]] + a[l[0]+1:])
            break

