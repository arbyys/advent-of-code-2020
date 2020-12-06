with open('input.txt') as file:
    data = file.read().split("\n\n")

sum = 0
for group in data:
    answered_same = []
    answered_yes = []
    index = 0
    group = group.split("\n")
    for person in group:
        for answer in person:
            if(len(answered_yes) != index + 1):
                answered_yes.append([])
            answered_yes[index].append(answer)
        index += 1
    if(len(answered_yes) == 1):
        sum += len(answered_yes[0])
    else:
        for idx, person in enumerate(answered_yes):
            if(idx == 0):
                answered_same.extend(person)
                continue

            answered_same = set(person) & set(answered_same)
        sum += len(answered_same)

print(sum)
