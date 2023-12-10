lines = []

directions = {'|': 'NS', '-': 'EW', 'L': 'NE', 'J': 'NW', '7': 'SW', 'F': 'SE', '.': '', 'S': ''}

dir_change = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}

bends = ['L', 'J', '7', 'F', 'S']

start_pos = []
with open('/home/faelern/PycharmProjects/advent_of_code/day10/input.txt', 'r') as file:
    for line in file:
        lines.append(line)

x_limit = len(lines[0])
y_limit = len(lines)
loop = []
steps = 1

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == 'S':
            start_pos = [i, j]

came_from = '#'
found = False
for going_to in ['N', 'E', 'S', 'W']:

    if not found:
        y = start_pos[0]
        x = start_pos[1]
        if going_to == 'N' and y > 0:
            y -= 1
            came_from = 'S'
        elif going_to == 'E' and x < x_limit:
            x += 1
            came_from = 'W'
        elif going_to == 'S' and y < y_limit:
            y += 1
            came_from = 'N'
        elif going_to == 'W' and x > 0:
            x -= 1
            came_from = 'E'

        if came_from in directions[lines[y][x]]:
            found = True

char = lines[y][x]
loop.append([y, x])
going_to = directions[char].replace(came_from, '')

while char != 'S':
    if going_to == 'N':
        y -= 1
    if going_to == 'E':
        x += 1
    if going_to == 'S':
        y += 1
    if going_to == 'W':
        x -= 1

    char = lines[y][x]
    loop.append([y, x])
    if char != 'S':
        came_from = dir_change[going_to]
        going_to = directions[char].replace(came_from, '')
    steps += 1

print('steps', steps / 2)


vertices = [point for point in loop if lines[point[0]][point[1]] in bends]


area = 0
for i in range(len(vertices) - 1):
    area += vertices[i][1] * vertices[i + 1][0] - vertices[i][0] * vertices[i + 1][1]
area += vertices[-1][1] * vertices[0][0] - vertices[-1][0] * vertices[0][1]

print('loop', len(loop))
area = abs(area) / 2
print('area', area)

inner = area - len(loop) / 2 + 1
print('inner', inner)
