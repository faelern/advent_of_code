
colors = ['red', 'green', 'blue']

file = open('/home/faelern/PycharmProjects/advent_of_code/day02/input.txt', 'r')

lines = [line.split(': ')[1] for line in file]

power_sum = 0

for i, game in enumerate(lines):
    max_values = [0, 0, 0]
    game = game.split('; ')
    for hand in game:
        hand = hand.split(', ')
        for color_in_hand in hand:
            color_in_hand = color_in_hand.split(' ')
            for j, color in enumerate(colors):
                if color_in_hand[1].startswith(color):
                    value = int(color_in_hand[0])
                    if value > max_values[j]:
                        max_values[j] = value

    power = 1
    for x in max_values:
        power *= x
    power_sum += power

file.close()
print(power_sum)


