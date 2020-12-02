data = []
with open('input.txt') as file:
    for line in file:
        line = line.split() #preprocess line
        data.append(line)

def scanPassword(letter, positions, password):

    if((password[positions[0]] == letter) ^ (password[positions[1]] == letter)):
        return True
    return False

valid = 0
for x in data:
    first_position = int(x[0].split("-")[0])-1
    second_position = int(x[0].split("-")[1])-1
    letter = x[1][:-1]
    password = x[2]

    if(scanPassword(letter, [first_position, second_position], password)):
        valid += 1

print(valid)
