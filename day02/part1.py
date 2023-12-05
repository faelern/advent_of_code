# 12 red, 13 green, 14 blue

colors = ['red', 'green', 'blue']
max_values = [12, 13, 14]

file = open('/home/faelern/PycharmProjects/advent_of_code/day02/input.txt', 'r')

lines = [line.split(': ')[1] for line in file]

sum = 0
game_possible = True
for i, game in enumerate(lines):
    game_possible = True
    game = game.split('; ')
    for hand in game:
        hand = hand.split(', ')
        for color_in_hand in hand:
            color_in_hand = color_in_hand.split(' ')
            for j, color in enumerate(colors):
                if color_in_hand[1].startswith(color):
                    if int(color_in_hand[0]) > max_values[j]:
                        game_possible = False


    if game_possible:
        sum += i + 1

file.close()
print(sum)


