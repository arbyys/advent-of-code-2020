import math

with open('input.txt') as file:
    data = file.read().split("\n")
    data = data[:-1] # remove last empty line


def rotateWaypoint(direction, degree, x_offset_WP, y_offset_WP):
    if(degree == 180):
        return x_offset_WP*-1, y_offset_WP*-1
    if(direction == "R"):
        if(degree == 90):
            return y_offset_WP, x_offset_WP*-1
        return y_offset_WP*-1, x_offset_WP
    if(direction == "L"):
        if(degree == 90):
            return y_offset_WP*-1, x_offset_WP
        return y_offset_WP, x_offset_WP*-1

def moveWaypoint(direction, amount, x_offset_WP, y_offset_WP):
    if(direction == "W"):
        x_offset_WP -= amount
    elif(direction == "E"):
        x_offset_WP += amount
    elif(direction == "N"):
        y_offset_WP += amount
    elif(direction == "S"):
        y_offset_WP -= amount
    return x_offset_WP, y_offset_WP

def moveToWaypoint(times, x_pos, y_pos, x_offset_WP, y_offset_WP):
    x_move = x_offset_WP * times
    y_move = y_offset_WP * times
    return x_pos+x_move, y_pos+y_move

x_offset_WP = 10
y_offset_WP = 1
x_pos = 0 # W / E position
y_pos = 0 # N / S position

for x in data:
    action = x[:1]
    amount = int(x[1:])
    if(action in ["N", "S", "E", "W"]): # move waypoint in direction
        x_offset_WP, y_offset_WP = moveWaypoint(action, amount, x_offset_WP, y_offset_WP)

    elif(action in ["L", "R"]): # rotate waypoint by given number
        x_offset_WP, y_offset_WP = rotateWaypoint(action, amount, x_offset_WP, y_offset_WP)

    else: # move forward
        x_pos, y_pos = moveToWaypoint(amount, x_pos, y_pos, x_offset_WP, y_offset_WP)

print(abs(x_pos) + abs(y_pos))
