f = open('input.txt', 'r')

fullinput = f.read()

lastthree = fullinput[0:3]
partoneinput = fullinput[3:len(fullinput)]
total = 3

def unique(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return False
    return True

for c in partoneinput:
    lastthree += c
    if unique(lastthree):
        total += 1
        print("Part 1 output:", total)
        print("First unique string: ", lastthree)
        break
    lastthree = lastthree[1:4]
    total += 1

total = 13

lastthirteen = fullinput[0:13]
parttwoinput = fullinput[13:len(fullinput)]

for c in parttwoinput:
    lastthirteen += c
    if unique(lastthirteen):
        total += 1
        print("Part 2 output:", total)
        print("First unique string: ", lastthirteen)
        break
    lastthirteen = lastthirteen[1:14]
    total += 1

