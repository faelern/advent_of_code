data = []
with open('/home/faelern/PycharmProjects/advent_of_code/day16/input.txt', 'r') as file:
    for line in file:
        data.append(line[:-1])

beams = []
grid = [[[] for y in range(len(data[0]))] for x in range(len(data))]
xmax = len(data[0]) - 1
ymax = len(data) - 1
energized = set()
history = set()
values = []

change_dir = {'/': {'n': 'e', 'e': 'n', 's': 'w', 'w': 's'},
              '\\': {'n': 'w', 'e': 's', 's': 'e', 'w': 'n'},
              '-': {'n': 'ew', 'e': 'e', 's': 'ew', 'w': 'w'},
              '|': {'n': 'n', 'e': 'ns', 's': 's', 'w': 'ns'}}

start_pos_list = []
for y in range(ymax + 1):
    start_pos_list.append([y, 0, 'e'])
    start_pos_list.append([y, xmax + 1, 'w'])

for x in range(xmax + 1):
    start_pos_list.append([0, x, 's'])
    start_pos_list.append([ymax + 1, x, 'n'])


for start_pos in start_pos_list:
    beams = [start_pos]

    while beams:
        for i, beam in enumerate(beams):
            # print(i, beam)
            y, x, d = beam
            temp = (y, x, d)
            if temp in history:
                beams.pop(i)
                continue

            elif d == 'n' and y > 0:
                y -= 1
            elif d == 's' and y < ymax:
                y += 1
            elif d == 'e' and x < xmax:
                x += 1
            elif d == 'w' and x > 0:
                x -= 1
            else:
                beams.pop(i)
                continue

            char = data[y][x]
            energized.add((y, x))

            if char != '.':
                next_dir = change_dir[char][d]
                if len(next_dir) == 1:
                    d = next_dir
                else:
                    d = next_dir[0]
                    beams.append([y, x, next_dir[1]])

            beams[i] = [y, x, d]
            history.add(temp)

        values.append(len(energized) + 1)

print(max(values))
