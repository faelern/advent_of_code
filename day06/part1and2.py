from math import sqrt

file = open('/home/faelern/PycharmProjects/advent_of_code/day06/input.txt', 'r')

times = file.readline()
distances = file.readline()
file.close()

times = times.split(' ')
distances = distances.split(' ')
times[-1] = times[-1][:-1]
distances[-1] = distances[-1][:-1]

print(times)
print(distances)

product = 1

for t, s in zip(times, distances):
    t = int(t)
    s = int(s)
    delta = sqrt(t ** 2 - 4 * s)
    x2 = (-t - delta)/-2
    x1 = (-t + delta)/-2
    x1 += 0.000000000001
    x2 -= 0.000000000001
    x1 = int(x1) + 1
    x2 = int(x2)
    product *= (x2 - x1 + 1)

print(product)
