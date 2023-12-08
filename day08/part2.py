file = open('/home/faelern/PycharmProjects/advent_of_code/day08/input.txt', 'r')

directions = file.readline()[:-1]
nodes = {}
current_nodes = []
complete_paths = []

steps = 0

for line in file:
    key = line.split(' = ')[0]
    value = line.split(' = ')[1][1:-2]
    value = value.split(', ')
    nodes[key] = value

file.close()


for node in nodes:
    if node[-1] == 'A':
        current_nodes.append(node)
        complete_paths.append(0)

while 0 in complete_paths:
    for direction in directions:
        if 0 in complete_paths:
            for i, current_node in enumerate(current_nodes):
                if direction == 'L':
                    current_nodes[i] = nodes[current_node][0]
                else:
                    current_nodes[i] = nodes[current_node][1]

                if current_nodes[i][-1] == 'Z':
                    complete_paths[i] = 1
                else:
                    complete_paths[i] = 0
            steps += 1
print(steps)
