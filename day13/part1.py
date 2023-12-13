data = ''

with open('/home/faelern/PycharmProjects/advent_of_code/day13/input.txt', 'r') as file:
    data = file.read()

data = data.split('\n\n')
for pattern in data:
    pattern = pattern.split('\n')

print(data)


def search_for_horizontal(given_data):
    size = len(given_data)
    for i in range(size - 1):
        if given_data[i] == given_data[i + 1]:
            mirror = True
            for j in range(min(i, size - 1)):
                if not given_data[i - j] == given_data[i + 1 + j]:
                    mirror = False
            if mirror:
                return i + 1
    return None


