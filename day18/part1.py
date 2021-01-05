import re

with open('input.txt') as file:
    data = file.read().split("\n")
    data = data[:-1] # remove last empty line

def calculateExpression(ex):
    result = ex.split(" ")
    while True:
        if(len(result) == 1):
            break
        if(result[1] == "+"):
            calculated = int(result[0]) + int(result[2])
        else:
            calculated = int(result[0]) * int(result[2])
        del result[0:2]
        result[0] = calculated
    return result[0]

def removeBrackets(ex):
    while True:
        if("(" not in ex):
            break
        startScan = False
        for idx,x in enumerate(ex):
            if(x == ")" and startScan):
                bracket_end = idx
                break
            if(x == "("):
                bracket_start = idx
                startScan = True
        solved = calculateExpression(ex[bracket_start+1:bracket_end])
        ex = [*ex]
        del ex[bracket_start:bracket_end]
        ex[bracket_start] = str(solved)
        ex = "".join(ex)
    return ex

sumresult = 0
for x in data:
    sumresult += calculateExpression(removeBrackets(x))
print(sumresult)
