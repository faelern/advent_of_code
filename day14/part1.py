data = []
with open('/home/faelern/PycharmProjects/advent_of_code/day14/input.txt', 'r') as file:
    for i, row in enumerate(file):
        data.append([])
        for char in row[:-1]:
            data[i].append(char)


def transpone(given_set):
    cols = []
    for x in range(len(given_set[0])):
        temp = ''
        for y in range(len(given_set)):
            temp += given_set[y][x]
        cols.append(temp)
    return cols


data = transpone(data)

for i, row in enumerate(data):
    temp = row.split('#')
    data[i] = temp

for i, row in enumerate(data):
    for j, seq in enumerate(row):
        rocks = 0
        dots = 0
        for char in seq:
            if char == '.':
                dots += 1
            elif char == 'O':
                rocks += 1
        temp = 'O' * rocks + '.' * dots
        data[i][j] = temp


for i, row in enumerate(data):
    temp = ''
    for seq in row:
        temp += seq
        temp += '#'
    temp = temp[:-1]
    data[i] = temp


data = transpone(data)
product = 0
for row, multiplier in zip(range(len(data)), range(len(data), 0, -1)):
    count = 0
    for char in data[row]:
        if char == 'O':
            count += 1

    product += count * multiplier

print(product)
