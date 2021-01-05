with open('i.txt') as file:
    data = file.read().split("\n")

for idx,instruction in enumerate(data):
    if("a" in instruction): # rules
        continue

    else: # messages
        num = instruction.split(": ")[0]
        content = instruction.split(": ")[1]
        next = []
        if("|" in content):
            next.append(content.split("|")[0].split(" "))
            next.append(content.split("|")[1].split(" "))
        else:
            next.append(content.split(" "))
        #print(next)
        print(instruction)
