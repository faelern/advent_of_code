file = open('/home/faelern/PycharmProjects/advent_of_code/day07/input.txt', 'r')

hands = []
bids = []

hands_types = [[], [], [], [], [], [], []]

card_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

for line in file:
    hands.append([line.split(' ')[0], int(line.split(' ')[1][:-1])])

file.close()


for hand in hands:
    x = -1
    species = [0, 0, 0, 0, 0]
    for rank in card_ranks:
        rank_found = False
        for card in hand[0]:
            if card == rank:
                if not rank_found:
                    x += 1
                species[x] += 1
                rank_found = True

    x += 1
    if x == 1:
        hands_types[0].append(hand)
    elif x == 2:
        if max(species) == 4:
            hands_types[1].append(hand)
        else:
            hands_types[2].append(hand)
    elif x == 3:
        if max(species) == 3:
            hands_types[3].append(hand)
        else:
            hands_types[4].append(hand)
    elif x == 4:
        hands_types[5].append(hand)
    else:
        hands_types[6].append(hand)


for hand_type in hands_types:
    if len(hand_type) > 1:
        for passes in range(len(hand_type)):
            for i in range(len(hand_type) - 1):
                solved = False
                for j in range(5):
                    if not solved:
                        left = card_ranks.index(hand_type[i][0][j])
                        right = card_ranks.index(hand_type[i + 1][0][j])

                        if left > right:
                            solved = True

                        if left < right:
                            hand_type[i], hand_type[i + 1] = hand_type[i + 1], hand_type[i]
                            solved = True


sorted_hands = []


for hand_type in hands_types:
    print(hand_type)
    for hand in hand_type:
        sorted_hands.append(hand)

sorted_hands.reverse()

win = 0

for i, hand in enumerate(sorted_hands):
    win += hand[1] * (i + 1)

print(win)