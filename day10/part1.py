import sys

with open('input.txt') as file:
    data = file.read().split("\n")
    data = data[:-1]  # remove last empty line

    data = list(map(int, data))  # to int

builtin_rating = max(data) + 3
differences = {1: 0, 2: 0, 3: 0}
current_rating = 0

while True:
    query = 1
    found = False
    while (query <= 3):
        if(found):
            break
        for x in data:
            if((builtin_rating - current_rating) == 3):
                differences[3] += 1
                print(differences[1] * differences[3])
                sys.exit()
            if((x - current_rating) == query):
                differences[x - current_rating] += 1
                current_rating += (x - current_rating)
                found = True
                break
        query += 1

# %%
