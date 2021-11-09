with open('input.txt') as file:
    data = file.read().split("\n")
    data = data[:-1] # remove last empty line

one_row = len(data[0])
trees = []
right_growth = [1, 3, 5, 7, 1]
down_growth = [1, 1, 1, 1, 2]

for i in range(len(right_growth)):
    current_position = 0

    for u,x in enumerate(data):
        if(len(trees) != i+1):
            trees.append(0)
        if(current_position > one_row-1):
            current_position = current_position - one_row

        if((x[current_position] == "#") and not ((down_growth[i] == 2) & (u % 2 == 1))):
                trees[i] += 1

        if((down_growth[i] == 2) & (u % 2 == 1)):
            continue
        current_position += right_growth[i]

result = 1
for x in trees:
    result = result * x
print(result)
