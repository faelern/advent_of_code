data = ''

with open('input.txt', 'r') as file:
    data = file.read()

data = data.split('\n\n')
data = [pattern.split('\n') for pattern in data]
data[-1] = data[-1][:-1]


def search_for_horizontal(given_pattern):
    size = len(given_pattern)
    for i in range(size - 1):
        if given_pattern[i] == given_pattern[i + 1]:
            mirror = True
            for j in range(min(i + 1, size - i - 1)):
                if not given_pattern[i - j] == given_pattern[i + 1 + j]:
                    mirror = False
            if mirror:
                return i + 1
    return None


def transpone(given_pattern):
    cols = []
    for x in range(len(given_pattern[0])):
        temp = ''
        for y in range(len(given_pattern)):
            temp += given_pattern[y][x]
        cols.append(temp)
    return cols


value = 0
for pattern in data:
    horizontal = search_for_horizontal(pattern)
    if horizontal:
        value += 100 * horizontal
    else:
        value += search_for_horizontal(transpone(pattern))

print(value)