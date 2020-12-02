with open('../input.txt') as file:
    data = file.read().split("\n")
    data = data[:-1] # remove last empty line

    data = list(map(int, data)) # to int

min_value = min(data)
result = 0

for x in data:
    if(result != 0):
        break
    if((x + min_value) > 2020):
        continue
    for i in data:
        if(i == x):
            continue
        for z in data:
            if(z == i):
                continue
            if(x + i + z == 2020):
                result = x * i * z
                break

print(result)
