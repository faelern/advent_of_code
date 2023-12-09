from math import gcd

def lcm(a, b):
    return (a * b) / gcd(a, b)


file = open('input.txt', 'r')

directions = file.readline()[:-1]
nodes = {}
current_nodes = []
paths = []

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

print(current_nodes)


for current_node in current_nodes:
    while not current_node[-1] == 'Z':
        for direction in directions:
            if not current_node[-1] == 'Z':
                if direction == 'L':
                    current_node = nodes[current_node][0]
                else:
                    current_node = nodes[current_node][1]
                steps += 1
    paths.append(steps)
    steps = 0

print(paths)
x = paths[0]
for i in range(len(paths) - 1):
    x = lcm(int(x), int(paths[i + 1]))
print(x)
