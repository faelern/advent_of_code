file = open('/home/faelern/PycharmProjects/advent_of_code/day03/input.txt', 'r')
input_txt = []

for line in file:
    input_txt.append(line)

file.close()

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
values = []
values_indexes = []
special_chars_indexes = []

values_sum = 0

value = ''
prev_char = False

for line in input_txt:

    line_values = []
    line_values_indexes = []
    line_special_char_indexes = []
    for i, char in enumerate(line):

        if char not in digits:
            if prev_char:
                line_values.append(value)
                line_values_indexes.append(i - len(value))
                value = ''

            prev_char = False

            if char not in ['.', '\n']:
                line_special_char_indexes.append(i)

        else:
            prev_char = True
            value += char

    values.append(line_values)
    values_indexes.append(line_values_indexes)
    special_chars_indexes.append(line_special_char_indexes)

special_chars_indexes.append([])

for i, line in enumerate(values):
    for j, value in enumerate(line):
        correct = False
        possible_indexes = [*range(values_indexes[i][j] - 1, values_indexes[i][j] + len(value) + 1)]

        for possible_index in possible_indexes:
            if (possible_index in special_chars_indexes[i - 1] or
                    possible_index in special_chars_indexes[i] or
                    possible_index in special_chars_indexes[i + 1]):
                correct = True

        if correct:
            values_sum += int(value)

print(values_sum)
