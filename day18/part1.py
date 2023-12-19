data = []

with open('input.txt') as file:
    for line in file:
        line = line.split(' ')[:-1]
        data.append(line)


def calculate_area(vertices):
    area = 0
    for i in range(len(vertices) - 1):
        area += vertices[i][1] * vertices[i + 1][0] - vertices[i][0] * vertices[i + 1][1]
    area += vertices[-1][1] * vertices[0][0] - vertices[-1][0] * vertices[0][1]

    area = abs(area) / 2
    return area


vertices = [(0, 0)]
border = 0

for i, line in enumerate(data):
    y = vertices[i][0]
    x = vertices[i][1]
    step = int(line[1])
    direction = line[0]

    border += step

    if direction == 'U':
        vertices.append((y - step, x))

    elif direction == 'D':
        vertices.append((y + step, x))

    elif direction == 'L':
        vertices.append((y, x - step))

    elif direction == 'R':
        vertices.append((y, x + step))


area = calculate_area(vertices)

cap = area + border / 2 + 1
print(cap)