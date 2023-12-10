lines = []

directions = {'|': 'NS', '-': 'EW', 'L': 'NE', 'J': 'NW', '7': 'SW', 'F': 'SE'}

dir_change = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}

start_pos = []
with open('input.txt', 'r') as file:
    for line in file:
        lines.append(line)


loop = []
steps = 1


y = 31
x = 112


char = lines[y][x]
came_from = 'W'
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

print(steps/2)

inner = 0
outer = 0

for y, line in enumerate(lines):
    intersect = 0
    for x, char in enumerate(line):
        if [y, x] in loop:
            intersect += 1
        else:
            if intersect % 2 == 0:
                outer += 1
            else:
                inner += 1

print(inner)

# poziome rury psuja

