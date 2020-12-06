with open('input.txt') as file:
    data = file.read().split("\n\n")

sum = 0
for group in data:
    answered_yes = []
    group = group.split("\n")
    for person in group:
        for answer in person:
            if(answer not in answered_yes):
                answered_yes.append(answer)
    sum += len(answered_yes)

print(sum)
