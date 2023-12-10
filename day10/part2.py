lines = []

directions = {'|': 'NS', '-': 'EW', 'L': 'NE', 'J': 'NW', '7': 'SW', 'F': 'SE'}

dir_change = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}

bends = ['L', 'J', '7', 'F', 'S']

start_pos = []
with open('input.txt', 'r') as file:
    for line in file:
        lines.append(line)


loop = []
steps = 1

y = 1
x = 2

start_pos = [y, x]

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

print('steps', steps/2)

loop.append(start_pos)
# inner = 0
# outer = 0
#
# for y, line in enumerate(lines):
#     intersect = 0
#     for x, char in enumerate(line):
#         if [y, x] in loop:
#             intersect += 1
#         else:
#             if intersect % 2 == 0:
#                 outer += 1
#             else:
#                 inner += 1

vertices = [point for point in loop if lines[point[0]][point[1]] in bends]

# vertices.append(vertices[0])

area = 0
for i in range(len(vertices) - 1):
    area += vertices[i][1] * vertices[i + 1][0] - vertices[i][0] * vertices[i + 1][1]
    print('foo')
area += vertices[-1][1] * vertices[0][0] - vertices[-1][0] * vertices[0][1]

print('loop', len(loop))
area = abs(area) / 2
print('area', area)


inner = area - len(loop)/2 + 1
print('inner', inner)
