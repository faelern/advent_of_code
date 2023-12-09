file = open('/home/faelern/PycharmProjects/advent_of_code/day09/input.txt', 'r')
lines = []

for line in file:
    lines.append(line.split(' '))

file.close()

for line in lines:
    line = [int(x) for x in line]

end_values = []


def get_pyramid_row(n):
    pyramid = []
    for i in range(n):
        pyramid.append([])
        for x in range(i + 1):
            if x == 0 or x == i:
                pyramid[i].append(1)
            else:
                pyramid[i].append(pyramid[i - 1][x] + pyramid[i - 1][x - 1])
    return pyramid[n - 1]


def get_history_value(start_values):
    start_values.reverse()
    product = 0
    multipliers = get_pyramid_row(len(start_values))
    for i, value in enumerate(start_values):
        x = value * multipliers[i]
        if i % 2 == 0:
            product += x
        else:
            product -= x
    return product


def get_next_value(last_values):
    temp = 0
    x = 0
    for i in range(1, len(last_values)):
        x = last_values[i] + temp
        temp = x
    return x


x = 0

for line in lines:
    line = [int(x) for x in line]
    end_values = []
    for n in range(len(line)):
        end_values.append(get_history_value(line[n:]))

    x += get_next_value(end_values)

print(x)
