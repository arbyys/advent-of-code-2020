data = []
with open('input.txt') as file:
    for line in file:
        line = line.split() #preprocess line
        data.append(line)

def scanPassword(letter, password):
    count = 0
    for i in password:
        if(i == letter):
            count += 1
    return count

valid = 0
for x in data:
    min_value = int(x[0].split("-")[0])
    max_value = int(x[0].split("-")[1])
    letter = x[1][:-1]
    password = x[2]

    if(min_value <= scanPassword(letter, password) <= max_value):
        valid += 1

print(valid)
