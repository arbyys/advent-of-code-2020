import re

with open('input.txt') as file:
    data = file.read().split("\n\n")

numbers = []
errors = []
for x in data:
    for y in x.split("\n"):
        match = re.findall(r"\d+-\d+", y)
        if(len(match) == 0 and "ticket" not in y):
            for number in y.split(","):
                if(number == ""):
                    continue
                if(int(number) not in numbers):
                    errors.append(int(number))
        for item in match:
            lower_range = item.split("-")[0]
            upper_range = item.split("-")[1]
            for number in range(int(lower_range), int(upper_range)+1):
                if(number not in numbers):
                    numbers.append(number)

print(sum(errors))
