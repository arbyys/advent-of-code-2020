with open('input.txt') as file:
    data = file.read().split("\n")
    data = data[:-1] # remove last empty line

class Bag:
    def __init__(self, color, amount):
        self.color = color
        self.amount = amount
    def __str__(self):
        return "{} of {}".format(self.amount, self.color)

bagsstorage = {}
def countBags(bag):
    if(bag in bagsstorage):
        return bagsstorage[bag]

    num = 0

    for container in bags[bag]:
        num += int(container.amount) + int(container.amount) * countBags(container.color)

    bagsstorage[bag] = num
    return num


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

print(countBags("shiny gold"))
