file = open('/home/faelern/PycharmProjects/advent_of_code/day04/input.txt', 'r')

input_txt = []

for line in file:
    input_txt.append(line)

file.close()

matches_list = []
copies_list = []



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

    matches_list.append(matches)
    copies_list.append(1)


for i, card_matches in enumerate(matches_list):
        for j in range(i + 1, i + card_matches + 1):
            copies_list[j] += copies_list[i]


copies_sum = 0
for copy in copies_list:
    copies_sum += copy

print(copies_sum)