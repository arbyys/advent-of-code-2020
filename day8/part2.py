import sys

with open('input.txt') as file:
    data = file.read().split("\n")
    data = data[:-1] # remove last empty line

for idx,x in enumerate(data):
    data[idx] = x.split(" ")


current_index = 0
instruction_to_change = 0
accumulator = 0
indexes_done = []
while True:
    if(instruction_to_change == len(data)):
        break

    indexes_done = []
    accumulator = 0
    current_index = 0

    if(data[instruction_to_change][0] == "nop"):
        data[instruction_to_change][0] = "jmp"
    elif(data[instruction_to_change][0] == "jmp"):
        data[instruction_to_change][0] = "nop"
    else:
        instruction_to_change+=1
        continue

    while True:
        try:
            instruction = data[current_index][0]
            value = data[current_index][1]
        except:
            print(accumulator)
            sys.exit()

        if(current_index in indexes_done):
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

    if(data[instruction_to_change][0] == "nop"):
        data[instruction_to_change][0] = "jmp"
    elif(data[instruction_to_change][0] == "jmp"):
        data[instruction_to_change][0] = "nop"

    instruction_to_change+=1
