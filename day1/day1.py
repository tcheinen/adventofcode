dupe = -1
frequencies = [0]
with open("input.txt") as f:
    for line in f:
        freq = frequencies[-1] + int(line)
        frequencies.append(freq)
    print("ANSWER 1: " + str(frequencies[-1]))
    while(dupe == -1):
        for i in range(10):
            f.seek(0)
            for line in f:
                freq = frequencies[-1] + int(line)
                frequencies.append(freq)
        set_ = set()
        for item in frequencies:
            if item in set_:
                dupe = item
                break
            set_.add(item)
    print("ANSWER 2: " + str(dupe))

