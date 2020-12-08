with open('input.txt') as file:
    data = file.read().split("\n")
    data = data[:-1] # remove last empty line

class Bag:
    def __init__(self, color, amount):
        self.color = color
        self.amount = amount
    def __str__(self):
        return "{} of {}".format(self.amount, self.color)

bags = {}
for x in data:
    bag = x.split(" bags contain ")[0]
    content = x.split(" bags contain ")[1]
    content = content.replace(".", "")

    bags[bag] = []
    for y in content.split(","):
        y = y.lstrip().rsplit(' ', 1)[0]
        amount = y.split(" ", 1)[0]
        color = y.split(" ", 1)[1]
        if("no other bags" not in content):
            bags[bag].append(Bag(color, amount))

wanted_bags = ["shiny gold"]
selected_bags = []
all_bags = []
while True:
    for key, value in bags.items():
        for bag in value:
            if(bag.color in wanted_bags):
                selected_bags.append(key)

    if(selected_bags == []):
        break
    all_bags.extend(selected_bags)
    wanted_bags = selected_bags.copy()
    selected_bags = []

all_bags = list(dict.fromkeys(all_bags))

print(len(all_bags))
