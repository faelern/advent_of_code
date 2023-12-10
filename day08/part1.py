file = open('input.txt', 'r')

directions = file.readline()[:-1]
nodes = {}
node = 'AAA'
steps = 0

for line in file:
    key = line.split(' = ')[0]
    value = line.split(' = ')[1][1:-2]
    value = value.split(', ')
    nodes[key] = value

file.close()

while node != 'ZZZ':
    for direction in directions:
        if node != 'ZZZ':
            if direction == 'L':
                node = nodes[node][0]
            else:
                node = nodes[node][1]
            steps += 1

print(steps)
