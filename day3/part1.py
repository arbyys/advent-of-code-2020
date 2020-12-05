with open('input.txt') as file:
    data = file.read().split("\n")
    data = data[:-1] # remove last empty line

current_position = 0
one_row = len(data[0])
trees = 0

for x in data:
    if(current_position > one_row-1):
        current_position = current_position - one_row
    if(x[current_position] == "#"):
        trees += 1
    current_position += 3

print(trees)
