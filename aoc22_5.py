import copy

f = open('input.txt', 'r')

fullinput = []

for l in f.read().split('\n'):
    fullinput.append(l)
fullinput.pop(513)

initialcrates = []
for lines in range(8):
    initialcrates.append(fullinput[lines])

stackone = []
for x in range(3, 8):
    stackone.append(initialcrates[x][1])
stacktwo = []
for x in range(2, 8):
    stacktwo.append(initialcrates[x][5])
stackthree = []
for x in range(4, 8):
    stackthree.append(initialcrates[x][9])
stackfour = []
for x in range(0, 8):
    stackfour.append(initialcrates[x][13])
stackfive = []
for x in range(1, 8):
    stackfive.append(initialcrates[x][17])
stacksix = []
for x in range(0, 8):
    stacksix.append(initialcrates[x][21])
stackseven = []
for x in range(5, 8):
    stackseven.append(initialcrates[x][25])
stackeight = []
for x in range(0, 8):
    stackeight.append(initialcrates[x][29])
stacknine = []
for x in range(1, 8):
    stacknine.append(initialcrates[x][33])

stacks = [stackone, stacktwo, stackthree, stackfour, stackfive, stacksix, stackseven, stackeight, stacknine]
initialstacks = copy.deepcopy(stacks)

instructions = fullinput[10:len(fullinput)]

for i in instructions:
    ins = i.split(" ")
    steps = int(ins[1])
    old = int(ins[3])
    new = int(ins[5])
    for x in range(0, steps):
        copy = stacks[old - 1].pop(0)
        stacks[new - 1].insert(0, copy)

output = ""
for x in range(0, 9):
    output += (stacks[x][0])

print("Part 1 solution:", output)

stacks = initialstacks

for i in instructions:
    ins = i.split(" ")
    steps = int(ins[1])
    old = int(ins[3])
    new = int(ins[5])
    copy = []
    for x in range(0, steps):
        copy.append(stacks[old - 1].pop(0))
    copy.reverse()
    for x in range(0, steps):
        stacks[new - 1].insert(0, copy.pop(0))

output = ""
for x in range(0, 9):
    output += (stacks[x][0])

print("Part 2 solution:", output)