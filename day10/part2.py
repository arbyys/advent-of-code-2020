import sys, math

with open('input.txt') as file:
    data = file.read().split("\n")
    data = data[:-1] # remove last empty line

    data = list(map(int, data)) # to int
    data.sort()

trib = {}
def count_possibilities(n):
    try:
        return trib[n]
    except KeyError:
        if(n == 0):
            return 1
        elif(n < 3):
            return n
        else:
            val = count_possibilities(n-1) + count_possibilities(n-2) + count_possibilities(n-3)
            trib[n] = val
            return val

def count_groups(list):
    group = 0
    res = []
    for idx,x in enumerate(list):
        if(x == 1):
            if((idx == len(list) - 1) & (group != 0)):
                group += 1
                res.append(group)
            else:
                group += 1
        else:
            res.append(group)
            group = 0
    return res



differences = []
builtin_rating = max(data) + 3
current_rating = 0

data.insert(0, 0)
while True:
    query = 1
    found = False
    while (query <= 3):
        if(found):
            break
        for x in data:
            if((builtin_rating - current_rating) == 3):
                result = []
                for y in count_groups(differences):
                    result.append(count_possibilities(y))
                print(math.prod(result))
                sys.exit()
            if((x - current_rating) == query):
                differences.append(x - current_rating)
                current_rating += (x - current_rating)
                found = True
                break
        query += 1
