import re

with open('input.txt') as file:
    data = file.read().split("\n")
    data = data[:-1] # remove last empty line

def applyMask(bitnum, mask):
    bitnum = [*bitnum]
    for i,x in enumerate(bitnum):
        if(mask[i] == "0"):
            continue

        if(mask[i] == "1"):
            bitnum[i] = "1"
        elif(mask[i] == "X"):
            bitnum[i] = "X"

    return "".join(bitnum)

def findIndexes(str, ch):
    yield [i for i, c in enumerate(str) if c == ch]

def swapNumber(num):
    if(str(num) == "0"):
        return "1"
    return "0"

mask = ""
values = {}

for x in data:
    if("mask" in x):
        mask = x.split("mask = ")[1]
    else:
        idx  = ' '.join(re.findall(r"\[(\d+)\]",x))
        idx = format(int(idx), '036b')
        value = format(int(x.split(" = ")[1]), '036b')
        aftermask = applyMask(idx, mask)

        results = []
        results_indexes = []

        for y in range(2 ** (aftermask.count("X"))):
            results.append(aftermask)
            results_indexes.append(value)

        if("X" in aftermask):
            indexes = list(findIndexes(aftermask, "X"))
            indexes[0].reverse()
            indexes = indexes[0]

            current_swap = 1

            current_x_index = 0

            while True:
                current_index = 0
                current_mask_index = 0
                current_x = 0

                if(all("X" not in el for el in results)):
                    break

                for y in range(2 ** (aftermask.count("X"))):
                    reset = False

                    results[current_mask_index] = [*results[current_mask_index]]

                    if(current_index == current_swap):
                        reset = True
                        current_x = swapNumber(current_x)
                        current_index = 1

                    results[current_mask_index][indexes[current_x_index]] = current_x
                    results[current_mask_index] = "".join(str(zz) for zz in results[current_mask_index])

                    current_mask_index += 1
                    if(not reset):
                        current_index += 1

                current_swap = current_swap * 2
                current_x_index += 1
        else:
            results.append(aftermask)

        values.update(dict(zip(results, results_indexes)))


total = 0
for key,value in values.items():
    total += int(value,2)

print(total)
