data = ''

with open('/home/faelern/PycharmProjects/advent_of_code/day15/input.txt', 'r') as file:
    data = file.read()
    data = data.split(',')
data[-1] = data[-1][:-1]
print(data)


product = 0
for value in data:
    temp = 0
    for char in value:
        temp += ord(char)
        temp *= 17
        temp %= 256
    product += temp


print(product)