from tqdm import trange

data = []
with open('/home/faelern/PycharmProjects/advent_of_code/day14/input.txt', 'r') as file:
    for row in file:
        data.append(row[:-1])


def transpone(given_set):
    cols = []
    for x in range(len(given_set[0])):
        temp = ''
        for y in range(len(given_set)):
            temp += given_set[y][x]
        cols.append(temp)
    return cols


def roll(given_set, direction):
    if direction == 'S':
        given_set = transpone(given_set)
        for i, row in enumerate(given_set):
            given_set[i] = row[::-1]
    elif direction == 'N':
        given_set = transpone(given_set)
    elif direction == 'E':
        for i, row in enumerate(given_set):
            given_set[i] = row[::-1]

    for i, row in enumerate(given_set):
        temp = row.split('#')
        given_set[i] = temp

    for i, row in enumerate(given_set):
        for j, seq in enumerate(row):
            rocks = 0
            dots = 0
            for char in seq:
                if char == '.':
                    dots += 1
                elif char == 'O':
                    rocks += 1
            temp = 'O' * rocks + '.' * dots
            given_set[i][j] = temp

    for i, row in enumerate(given_set):
        temp = ''
        for seq in row:
            temp += seq
            temp += '#'
        temp = temp[:-1]
        given_set[i] = temp

    if direction == 'S':
        for i, row in enumerate(given_set):
            given_set[i] = row[::-1]
        given_set = transpone(given_set)
    elif direction == 'N':
        given_set = transpone(given_set)
    elif direction == 'E':
        for i, row in enumerate(given_set):
            given_set[i] = row[::-1]

    return given_set


def calculate_load(given_set):
    product = 0
    for row, multiplier in zip(range(len(given_set)), range(len(given_set), 0, -1)):
        count = 0
        for char in given_set[row]:
            if char == 'O':
                count += 1

        product += count * multiplier

    return product


cycle = ['N', 'W', 'S', 'E']


for i in trange(1000):
    for x in cycle:
        data = roll(data, x)


load = calculate_load(data)

print(load)
