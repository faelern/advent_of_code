file = open('/home/faelern/PycharmProjects/advent_of_code/day04/input.txt', 'r')

input_txt = []

for line in file:
    input_txt.append(line)

file.close()

points = 0

for line in input_txt:
    line = line.split(': ')[1]
    win_numbers = line.split(' | ')[0].split(' ')
    your_numbers = line.split(' | ')[1].split(' ')
    win_numbers = [number for number in win_numbers if number != '']
    your_numbers = [number for number in your_numbers if number != '']
    your_numbers[-1] = your_numbers[-1][:-1]

    matches = 0
    for number in your_numbers:
        if number in win_numbers:
            matches += 1

    if matches:
        points += 2 ** (matches - 1)

print(points)