data = ''

with open('/home/faelern/PycharmProjects/advent_of_code/day15/input.txt', 'r') as file:
    data = file.read()
    data = data.split(',')
data[-1] = data[-1][:-1]

boxes = [{} for x in range(256)]


def find_label(value):
    temp = 0
    for char in value:
        temp += ord(char)
        temp *= 17
        temp %= 256
    return temp


for step in data:
    if '-' in step:
        label = find_label(step[:-1])
        boxes[label].pop(step[:-1], None)

    else:
        label = find_label(step[:-2])
        boxes[label][step[:-2]] = int(step[-1:])

print(boxes)
focus_power = 0
for i, box in enumerate(boxes):
    if box != {}:
        for j, lens in enumerate(box):
            focus_power += (i + 1) * (j + 1) * box[lens]

print(focus_power)