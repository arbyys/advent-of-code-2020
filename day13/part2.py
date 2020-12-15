with open('input.txt') as file:
    data = file.read().split("\n")
    data = data[:-1] # remove last empty line

def primeCheck(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))

buses = []
busesints = []

for x in data[1].split(","):
    buses.append(x)
    if(x == "x"):
        continue
    busesints.append(int(x))

current = 600000000000000
highest = max(busesints)
highest_index = buses.index(str(highest))
buses_first = buses[:highest_index]
buses_first.reverse()
buses_second = buses[highest_index:]
buses_second = buses_second[1:]

while True:
    if(current % highest == 0):
        break
    current += 1

while True:
    done = True
    remember = current

    for idx,x in enumerate(buses_first):
        if(not done):
            break
        if(x == "x"):
            continue
        if(((current-idx-1) % int(x)) == 0 ):
            done = True
        else:
            done = False

    if(done):
        for idx,x in enumerate(buses_second):
            if(not done):
                break
            if(x == "x"):
                continue
            if(((current+idx+1) % int(x)) == 0 ):
                done = True
            else:
                done = False

    if(done):
        print("RES:", remember-highest_index)
        break
    current = remember + highest
