f = open('input.txt', 'r')

rounds = []
total = 0

for r in f.read().split('\n'):
    rounds.append(r)

for game in rounds:
    if game != '':
        if game[0] == 'A':
            if game[2] == 'X':
                total += 4
            if game[2] == 'Y':
                total += 8
            if game[2] == 'Z':
                total += 3
        if game[0] == 'B':
            if game[2] == 'X':
                total += 1
            if game[2] == 'Y':
                total += 5
            if game[2] == 'Z':
                total += 9
        if game[0] == 'C':
            if game[2] == 'X':
                total += 7
            if game[2] == 'Y':
                total += 2
            if game[2] == 'Z':
                total += 6

print("Part 1 answer:")
print(total)
total = 0

for game in rounds:
    if game != '':
        if game[0] == 'A':
            if game[2] == 'X':
                total += 3
            if game[2] == 'Y':
                total += 4
            if game[2] == 'Z':
                total += 8
        if game[0] == 'B':
            if game[2] == 'X':
                total += 1
            if game[2] == 'Y':
                total += 5
            if game[2] == 'Z':
                total += 9
        if game[0] == 'C':
            if game[2] == 'X':
                total += 2
            if game[2] == 'Y':
                total += 6
            if game[2] == 'Z':
                total += 7

print("Part 2 answer:")
print(total)