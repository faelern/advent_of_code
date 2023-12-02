file = open('input.txt', 'r')

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

sum = 0

for line in file:
    newline = ''
    for char in line:
        if char in digits:
            newline += char
    print(newline)

    value = int(newline[0] + newline[-1])
    print(value)
    sum += value
    print()

print(sum)
file.close()