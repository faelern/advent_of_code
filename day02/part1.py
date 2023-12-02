# 12 red, 13 green, 14 blue

file = open('input.txt', 'r')

lines = [line.split(': ')[1] for line in file]

sum = 0

for line in lines:
    line = line.split('; ')
    for hand in line:
        hand = hand.split(', ')


for i, line in enumerate(lines):
    print(line)
    for hand in line:
        pass
        # print(hand)
        # for color in hand:
        #     color = color.split(' ')

file.close()
