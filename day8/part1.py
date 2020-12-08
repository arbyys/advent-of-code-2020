with open('input.txt') as file:
    data = file.read().split("\n")
    data = data[:-1] # remove last empty line

for idx,x in enumerate(data):
    data[idx] = x.split(" ")

current_index = 0
accumulator = 0
indexes_done = []
while True:
    instruction = data[current_index][0]
    value = data[current_index][1]

    if(current_index in indexes_done):
        print(accumulator)
        break

    if(instruction == "nop"):
        indexes_done.append(current_index)
        current_index += 1
        continue

    elif(instruction == "acc"):
        indexes_done.append(current_index)
        accumulator += int(value)
        current_index += 1
        continue
    else:
        indexes_done.append(current_index)
        current_index += int(value)
        continue
