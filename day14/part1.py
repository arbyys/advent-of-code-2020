import re

with open('input.txt') as file:
    data = file.read().split("\n")
    data = data[:-1] # remove last empty line

def applyMask(bitnum, mask):
    bitnum = [*bitnum]
    for i,x in enumerate(bitnum):
        if(mask[i] == "X"):
            continue

        if(x == "0" and mask[i] == "1"):
            bitnum[i] = "1"
        elif(x == "1" and mask[i] == "0"):
            bitnum[i] = "0"

    return "".join(bitnum)

mask = ""
values = {}

for x in data:
    if("mask" in x):
        mask = x.split("mask = ")[1]
    else:
        idx  = ' '.join(re.findall(r"\[(\d+)\]",x))
        value = format(int(x.split(" = ")[1]), '036b')
        values[idx] = applyMask(value, mask)


total = 0
for key,value in values.items():
    total += int(value,2)

print(total)
