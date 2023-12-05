file = open('input.txt', 'r')
input_txt = []

for line in file:
    input_txt.append(line)

file.close()

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

gears_indexes = []


for line in input_txt:
    line_gear_indexes = []
    for x, char in enumerate(line):
        if char == '*':
            line_gear_indexes.append(x)

    gears_indexes.append(line_gear_indexes)


for y, line in enumerate(gears_indexes):
    for x, gear_index in enumerate(line):
        if (input_txt[y][x - 1] in digits or input_txt[y][x + 1] in digits or
                input_txt[y - 1][x - 1] in digits or input_txt[y - 1][x] in digits or input_txt[y - 1][x + 1] in digits or
                input_txt[y + 1][x - 1] in digits or input_txt[y + 1][x] in digits or input_txt[y + 1][x + 1] in digits):
            pass

