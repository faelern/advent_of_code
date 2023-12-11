data = []

with open('/home/faelern/PycharmProjects/advent_of_code/day11/input.txt', 'r') as file:
    for line in file:
        data.append(line)


def expand_by_rows(rows):
    expanded = []
    for row in rows:
        if '#' not in row:
            expanded.append(row)
        expanded.append(row)
    return expanded


data = expand_by_rows(data)

translated_data = []

for x in range(len(data[0])):
    col = ''
    for y in range(len(data)):
        if data[y][x] != '\n':
            col += data[y][x]

    translated_data.append(col)

data = expand_by_rows(translated_data)

galaxies = []

for y, row in enumerate(data):
    for x, char in enumerate(row):
        if char == '#':
            galaxies.append([y, x])

distances = 0
for galaxy1 in galaxies:
    for galaxy2 in galaxies:
        if galaxy1 != galaxy2:
            y1 = galaxy1[0]
            x1 = galaxy1[1]
            y2 = galaxy2[0]
            x2 = galaxy2[1]

            distances += max(x1, x2) - min(x1, x2) + max(y1, y2) - min(y1, y2)

print(distances/2)