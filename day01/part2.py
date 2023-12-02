file = open('input.txt', 'r')

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
txt_digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

sum = 0

for line in file:
    new_line = ''
    for i, char in enumerate(line):
        if char not in digits:
            for j, number in enumerate(txt_digits):
                if line[i:i + len(number)] == number:
                    new_line += str(j)
        else:
            new_line += char

    value = int(new_line[0] + new_line[-1])
    sum += value

print(sum)
file.close()