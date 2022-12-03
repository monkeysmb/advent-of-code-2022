f = open('input.txt', 'r')

rucksacks = []
total = 0

for r in f.read().split('\n'):
    rucksacks.append(r)

rucksacks.pop(300)

for sacks in rucksacks:
    for items in sacks:
        firsthalf = slice(0, len(sacks) // 2)
        secondhalf = slice(len(sacks) // 2, len(sacks))
        if sacks[firsthalf].count(items) and sacks[secondhalf].count(items) != 0:
            if items.islower():
                total += ord(items) - 96
                break
            else:
                total += ord(items) - 38
                break

print("Sum of priorities in part 1:", total)
total = 0

i = 0
for x in range(100):
    for items in rucksacks[i]:
        if i < 300:
            if rucksacks[i].count(items) and rucksacks[i + 1].count(items) and rucksacks[i + 2].count(items) != 0:
                if items.islower():
                    total += ord(items) - 96
                    break
                else:
                    total += ord(items) - 38
                    break
    i += 3

print("Sum of priorities in part 2:", total)