from collections import defaultdict

grid = defaultdict(int)
answer_1 = 0
answer_2 = -1
def parse(data):
    x,y = [int(x) for x in data[data.find("@ ")+2:data.find(": ")].split(",")]
    w,h = [int(x) for x in data[data.find(": ")+2:].split("x")]
    id =  data[data.find("#")+1:data.find(" @ ")]
    return (id, x, y, w, h)

with open("input.txt") as f:
    suits = [parse(x) for x in f.readlines()]
    for suit in suits:
        id, x, y, w, h = suit    
        for i in range(w):
            for j in range(h):
                grid[(x + i, y + j)] += 1
    for suit in suits:
        id, x, y, w, h = suit    
        overlapping = False
        for i in range(w):
            for j in range(h):
                if(grid[(x + i, y + j)] > 1):
                    overlapping = True
        if(overlapping == False):
            answer_2 = id

for i in grid.values():
    if(i > 1):
        answer_1 += 1
        
print("Answer 1: " + str(answer_1))
print("Answer 2: " + str(answer_2))
