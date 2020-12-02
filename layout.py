with open('../input.txt') as file:
    data = file.read().split("\n")
    data = data[:-1] # remove last empty line test

    data = list(map(int, data)) # to int

print(data)
