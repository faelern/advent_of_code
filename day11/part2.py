data = []

with open('/home/faelern/PycharmProjects/advent_of_code/day11/input.txt', 'r') as file:
    for line in file:
        data.append(line)

empty_rows = []
empty_cols = []
galaxies = []


def find_empty_rows(data):
    for i, row in enumerate(data):
        if '#' not in row:
            empty_rows.append(i)


def find_empty_cols(data):
    for x in range(len(data[0]) - 1):
        count = 0
        for y in range(len(data)):
            if data[y][x] == '#':
                count += 1

        if count == 0:
            empty_cols.append(x)


def find_expansion(coord, direction):
    expansion = 0
    if direction == 'v':
        for row in empty_rows:
            if coord > row:
                expansion += 1

    elif direction == 'h':
        for col in empty_cols:
            if coord > col:
                expansion += 1

    return expansion * 999999


find_empty_rows(data)
find_empty_cols(data)


for y, row in enumerate(data):
    for x, char in enumerate(row):
        if char == '#':
            galaxies.append([y, x])


distances = 0
for galaxy1 in (galaxies):
    for galaxy2 in galaxies:
        if galaxy1 != galaxy2:
            y1 = galaxy1[0] + find_expansion(galaxy1[0], 'v')
            x1 = galaxy1[1] + find_expansion(galaxy1[1], 'h')
            y2 = galaxy2[0] + find_expansion(galaxy2[0], 'v')
            x2 = galaxy2[1] + find_expansion(galaxy2[1], 'h')

            distances += max(x1, x2) - min(x1, x2) + max(y1, y2) - min(y1, y2)

print(distances/2)

