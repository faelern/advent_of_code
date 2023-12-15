data = ''

with open('input.txt', 'r') as file:
    data = file.read()

data = data.split('\n\n')
data = [pattern.split('\n') for pattern in data]
data[-1] = data[-1][:-1]


def search_for_horizontal(given_pattern):
    size = len(given_pattern)
    cor = [-1 for x in given_pattern]
    for i in range(size - 1):
        for j in range(i + 1, size):
            if given_pattern[i] == given_pattern[j]:
                cor[i] = j - i
                cor[j] = i - j

    print(cor)


def transpone(given_pattern):
    cols = []
    for x in range(len(given_pattern[0])):
        temp = ''
        for y in range(len(given_pattern)):
            temp += given_pattern[y][x]
        cols.append(temp)
    return cols


print(search_for_horizontal(data[0]))

