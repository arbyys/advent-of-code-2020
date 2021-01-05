with open('i.txt') as file:
    data = file.read().split("\n")
    data = data[:-1] # remove last empty line

for x in data:
    print(x)
