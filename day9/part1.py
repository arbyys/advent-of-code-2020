with open('input.txt') as file:
    data = file.read().split("\n")
    data = data[:-1] # remove last empty line

    data = list(map(int, data)) # to int

offset = 25
for index_x,x in enumerate(data):
    if(index_x < offset):
        continue

    temp_data = data[index_x-offset:index_x]

    able = False
    for y in temp_data:
        for z in temp_data:
            if(y == z):
                continue
            if((y + z) == x):
                able = True
    if(not able):
        print(x)
