f = open('input.txt', 'r')

elves = []
cals = []
total = 0
for calories in f.read().split('\n'):
    cals.append(calories)

for c in cals:
    if c != '':
        total += int(c)
    if c == '':
        elves.append(total)
        total = 0

print(max(elves))
topthree = max(elves)
for i in range(2):
    elves.remove(max(elves))
    topthree += max(elves)

print(topthree)
