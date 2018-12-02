import itertools

base = [0]
with open("input.txt") as f:
    for line in f:
        freq = base[-1] + int(line)
        base.append(freq)
base.pop(0)
mod = [divmod(i,base[-1]) for i in base]
mod_indexes = []
for a, b in itertools.combinations(enumerate(mod),2):
    if(a[1][1] != b[1][1]):
        continue
    mod_indexes.append(((a[0],b[0]), abs(a[1][0] - b[1][0])))
mod_indexes.sort(key=lambda tup: tup[1])
freq = mod_indexes[0]

print("Answer 1: " + str(base[-1]))
print("Answer 2: " + str(freq[1] * base[-1] + base[freq[0][0]]))