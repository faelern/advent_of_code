data = []

with open('input.txt') as file:
    for line in file:
        line = line.split(' ')
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

    hex_step = line[2][2:-3]
    direction = line[2][-3]

    step = int(hex_step, 16)

    border += step

    if direction == '3':
        vertices.append((y - step, x))

    elif direction == '1':
        vertices.append((y + step, x))

    elif direction == '2':
        vertices.append((y, x - step))

    elif direction == '0':
        vertices.append((y, x + step))


area = calculate_area(vertices)

cap = area + border / 2 + 1
print(cap)
