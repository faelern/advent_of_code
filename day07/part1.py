file = open('/home/faelern/PycharmProjects/advent_of_code/day07/input.txt', 'r')

hands = []
bids = []

hands_types = [[], [], [], [], [], [], []]

values = [0.5, 1.6, 1.7, 2.7, 2.8, 3.8, 4.9]
card_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

for line in file:
    hands.append([line.split(' ')[0], int(line.split(' ')[1][:-1])])

file.close()


def calculate_hand_value(given_hand):
    cards_in_type_count = [0 for x in range(len(card_ranks))]
    type_counts = 0
    for card in given_hand:
        for i, card_type in enumerate(card_ranks):
            if card == card_type:
                cards_in_type_count[i] += 1

    for card_type in cards_in_type_count:
        if card_type > 0:
            type_counts += 1
    return type_counts - 0.1 * max(cards_in_type_count)


for hand in hands:
    hand_value = calculate_hand_value(hand[0])
    for i, value in enumerate(values):
        if hand_value == value:
            hands_types[i].append(hand)


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
    for hand in hand_type:
        sorted_hands.append(hand)

sorted_hands.reverse()

win = 0

for i, hand in enumerate(sorted_hands):
    win += hand[1] * (i + 1)

print(win)
