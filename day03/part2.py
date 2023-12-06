file = open('/home/faelern/PycharmProjects/advent_of_code/day03/input.txt', 'r')
input_txt = []

for asterisk_line in file:
    input_txt.append(asterisk_line)

file.close()

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

asterisks_indexes = []
gears_indexes = []
values = []
values_indexes = []
value = ''
prev_char_digit = False


for y, asterisk_line in enumerate(input_txt):
    values.append([])
    values_indexes.append([])
    asterisks_indexes.append([])
    for x, char in enumerate(asterisk_line):
        if char not in digits:
            if prev_char_digit:
                values[y].append(value)
                values_indexes[y].append(x - len(value))
                value = ''
            prev_char_digit = False

            if char == '*':
                asterisks_indexes[y].append(x)
        else:
            prev_char_digit = True
            value += char


ratios_sum = 0
adj_values = []

for y, asterisk_line in enumerate(asterisks_indexes):
    for asterisk_index in asterisk_line:
        adj_values = []
        for i, value_line in enumerate(values_indexes):
            if i in [y - 1, y, y + 1]:
                for j, index in enumerate(value_line):
                    if index <= asterisk_index + 1 and index + len(values[i][j]) >= asterisk_index:
                        adj_values.append(values[i][j])

        if len(adj_values) == 2:
            product = 1
            for x in adj_values:
                product *= int(x)
            ratios_sum += product

print(ratios_sum)

