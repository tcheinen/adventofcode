def parse(line):
    return (line[5], line[36])

with open("input.txt") as f:
    rules = [parse(x) for x in f.readlines()]
    answer_1 = []
    workers = 0
    timer = 0
    while len(answer_1) < 26:
        blocked =  [i[1] for i in rules if i[0] not in answer_1]
        allowed = [x[0] for x in rules if x[0] not in blocked and x[0] not in answer_1]
        if(len(allowed) == 0):
            allowed = [chr(ord("A") + x) for x in range(26) if chr(ord("A") + x) not in answer_1]
        answer_1 += min(allowed)
    print("".join(answer_1))
