lines = []

directions = {'|': 'NS', '-': 'EW', 'L': 'NE', 'J': 'NW', '7': 'SW', 'F': 'SE'}

dir_change = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}

start_pos = []
with open('/home/faelern/PycharmProjects/advent_of_code/day10/input.txt', 'r') as file:
    for line in file:
        lines.append(line)


for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == 'S':
            start_pos = [y, x]


# y = start_pos[0]
# x = start_pos[1]
pos = []
loop = []
steps = 1

# if 'N' in directions[lines[y + 1][x]]:
#     pos = [y + 1, x]
#     came_from = 'N'
#
# if 'E' in directions[lines[y][x - 1]]:
#     pos = [y, x - 1]
#     came_from = 'E'
#
# if 'S' in directions[lines[y - 1][x]]:
#     pos = [y - 1, x]
#     came_from = 'S'
#
#
# if 'W' in directions[lines[y][x + 1]]:
#     pos = [y, x + 1]
#     came_from = 'W'
#
#
# y = pos[0]
# x = pos[1]
y = 31
x = 112


char = lines[y][x]
print(lines[y][x])
came_from = 'W'
print(came_from)
going_to = directions[char].replace(came_from, '')
print(going_to)

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
    if char != 'S':
        came_from = dir_change[going_to]
        going_to = directions[char].replace(came_from, '')
    steps += 1


print(steps/2)
