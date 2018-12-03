from collections import defaultdict

grid = defaultdict(int)
answer_2 = -1
def parse(data):
    x,y = [int(x) for x in line[line.find("@ ")+2:line.find(": ")].split(",")]
    w,h = [int(x) for x in line[line.find(": ")+2:].split("x")]
    id =  line[line.find("#")+1:line.find(" @ ")]
    return (id, x, y, w, h)

with open("input.txt") as f:
    for line in f:
        id, x, y, w, h = parse(line)
        for i in range(w):
            for j in range(h):
                grid[(x + i, y + j)] += 1
    f.seek(0)
    for line in f:
        id, x, y, w, h = parse(line)
        overlapping = False
        for i in range(w):
            for j in range(h):
                if(grid[(x + i, y + j)] != 1):
                    overlapping = True
        if(overlapping == False):
            answer_2 = id


overlap_counter = 0
for i in grid.values():
    if(i > 1):
        overlap_counter += 1
print("Answer 1: " + str(overlap_counter))
print("Answer 2: " + str(answer_2))
