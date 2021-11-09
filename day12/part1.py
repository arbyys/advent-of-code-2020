import math

with open('input.txt') as file:
    data = file.read().split("\n")
    data = data[:-1] # remove last empty line.


def changeDirection(direction, degree, current_direction):

    dirs_dict = {"N": 0, "E": 90, "S": 180, "W": 270}

    opposite = {"N": "S", "S": "N", "W": "E", "E": "W"}

    if(degree == 180):
        if(direction == "L"):
            angle = abs(dirs_dict[current_direction] - degree)

        return opposite[current_direction]

    dirs = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
            "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]

    if(direction == "R"):
        angle = abs(dirs_dict[current_direction] + degree)
    elif(direction == "L"):
        angle = abs(dirs_dict[current_direction] + degree + 180)

    ix = int(((angle) + 11.25) / 22.5)
    return dirs[ix % 16]

def moveInDirection(direction, amount, x_pos, y_pos):
    if(direction == "W"):
        x_pos -= amount
    elif(direction == "E"):
        x_pos += amount
    elif(direction == "N"):
        y_pos += amount
    elif(direction == "S"):
        y_pos -= amount
    return x_pos, y_pos

current_direction = "E"
x_pos = 0 # W / E position
y_pos = 0 # N / S position

for x in data:
    action = x[:1]
    amount = int(x[1:])
    if(action in ["N", "S", "E", "W"]): # move in direction
        x_pos, y_pos = moveInDirection(action, amount, x_pos, y_pos)

    elif(action in ["L", "R"]): # turn by given number
        current_direction = changeDirection(action, amount, current_direction)

    else: # move forward
        x_pos, y_pos = moveInDirection(current_direction, amount, x_pos, y_pos)

print(abs(x_pos) + abs(y_pos))
