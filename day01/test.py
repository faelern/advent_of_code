input = 'bu1dsoneb3dssixvw2edstwoeightfdcbsixl8seven'
new_input = ''

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
txt_digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


for i, char in enumerate(input):
    if char in digits:
        new_input += char
    else:
        for j, number in enumerate(txt_digits):
            if input[i:i + len(number)] == number:
                new_input += str(j)

print(new_input)
