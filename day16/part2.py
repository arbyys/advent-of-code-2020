import re

with open('input.txt') as file:
    data = file.read().split("\n\n")

nums = {}
numbers = []
allnumbers = []
errors = []
valid_tickets = []

for x in data:
    for y in x.split("\n"):
        match = re.findall(r"\d+-\d+", y)
        if(len(match) == 0 and "ticket" not in y):
            for number in y.split(","):
                if(number == ""):
                    continue
                if(int(number) not in allnumbers):
                    if(y in valid_tickets):
                        valid_tickets.remove(y)
                    break
                if(y not in valid_tickets):
                    valid_tickets.append(y)
        numbers = []
        for idx,item in enumerate(match):
            if(idx == 0):
                name = y.split(":")[0]
            lower_range = item.split("-")[0]
            upper_range = item.split("-")[1]
            for number in range(int(lower_range), int(upper_range)+1):
                if(number not in numbers):
                    numbers.append(number)
                    allnumbers.append(number)
            if(idx == 1):
                nums[name] = numbers
possibilities = list(nums.keys())
able_possibilities = possibilities.copy()
results = {}
your_ticket = valid_tickets[0]
valid_tickets = valid_tickets[1:]

current_index = 0
for y in range(len(valid_tickets[0].split(","))):
    able_possibilities = list(nums.keys())
    for x in valid_tickets:
        for z in possibilities:
            curr = x.split(",")[current_index]
            if(int(curr) not in nums[z]):
                if(z in able_possibilities):
                    able_possibilities.remove(z)
    results[y] = able_possibilities
    current_index += 1


while True:
    keepGoing = False

    for key,value in results.items():
        if(len(value) == 1):
            remember = value[0]
            for key,value in results.items():
                if(remember in value and len(value) != 1):
                    value.remove(remember)

    for key,value in results.items():
        if(len(value) != 1):
            keepGoing = True
    if(not keepGoing):
        break

mult = 1
for idx,x in enumerate(your_ticket.split(",")):
    if("departure" in (results[idx][0])):
        mult = mult*int(x)

print(mult)
