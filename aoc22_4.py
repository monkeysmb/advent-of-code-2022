f = open('input.txt', 'r')

assignments = []
total = 0

for a in f.read().split('\n'):
    assignments.append(a)

assignments.pop(1000)

for a in assignments:
    cur = a.split(",")

    firstfullsplit = cur[0].split("-")
    secondfullsplit = cur[1].split("-")
    firstintfirst = int(firstfullsplit[0])
    firstintsecond = int(firstfullsplit[1])
    secondintfirst = int(secondfullsplit[0])
    secondintsecond = int(secondfullsplit[1])

    if cur[0] == cur[1]:
        total += 1
    else:
        if firstintfirst >= secondintfirst and firstintsecond <= secondintsecond:
            total += 1
        if secondintfirst >= firstintfirst and secondintsecond <= firstintsecond:
            total += 1

print("Part 1:", total)
total = 0

for a in assignments:
    cur = a.split(",")

    firstfullsplit = cur[0].split("-")
    secondfullsplit = cur[1].split("-")
    firstintfirst = int(firstfullsplit[0])
    firstintsecond = int(firstfullsplit[1])
    secondintfirst = int(secondfullsplit[0])
    secondintsecond = int(secondfullsplit[1])

    if secondintfirst <= firstintfirst <= secondintsecond or secondintfirst <= firstintsecond <= secondintsecond or firstintfirst <= secondintfirst <= firstintsecond or firstintfirst <= secondintsecond <= firstintsecond:
        total += 1

print("Part 2:", total)

