with open('input.txt') as file:
    data = file.read().split("\n")
    data = data[:-1] # remove last empty line

timestamp = int(data[0])
buses = []
for x in data[1].split(","):
    if(x == "x"):
        continue
    buses.append(int(x))

current = timestamp
while True:
    done = False
    for x in buses:
        if(current % x == 0):
            print(x * (current - timestamp))
            done = True
            break
    if(done):
        break
    current += 1
