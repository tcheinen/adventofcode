import queue

def parse(line):
    return (line[5], line[36])

def getNextValue(rules, current):
    blocked =  [i[1] for i in rules if i[0] not in current]
    allowed = next(chr(ord("A") + x) for x in range(26) if chr(ord("A") + x) not in blocked and chr(ord("A") + x) not in current)
    return allowed

with open("input.txt") as f:
    rules = [parse(x) for x in f.readlines()]
    answer_1 = []
    workers = 0
    timer = 0
    while len(answer_1) < 26:
        answer_1 += getNextValue(rules, answer_1)
    print("Answer 1: " + "".join(answer_1))
