def react(data):
    old = ""
    while data is not old:
        old = data
        for i in range(26):
            data = data.replace(chr(ord("a") + i) + chr(ord("A") + i),"").replace(chr(ord("A") + i) + chr(ord("a") + i),"")
    return data

with open("input.txt") as f:
    data = react(f.read())
    answer_1 = len(data)

    print("Answer 1: " + str(answer_1))

    answer_2 = answer_1
    for i in range(26):
        old = data
        data = data.replace(chr(ord("a") + i),"").replace(chr(ord("A") + i),"")
        data = react(data)
        if len(data) < answer_2:
            answer_2 = len(data)
        data = old
    print("Answer 2: " + str(answer_2))
