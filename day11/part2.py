with open('input.txt') as file:
    data = file.read().split("\n")
    data = data[:-1] # remove last empty line

def removeIfExists(list, element):
    if(element not in list):
        return False
    list.remove(element)

def checkForOccupied(data, row, seat):
    occupied = 0
    able = ["top", "right", "down", "left", "topright", "downright", "downleft", "topleft"]

    #print(row, seat, data[row][seat])
    if((len(data[row])-1 < seat) or (data[row][seat] == ".")):
        return False
    if(row == 0):
        removeIfExists(able, "top")
        removeIfExists(able, "topleft")
        removeIfExists(able, "topright")
    if(seat == 0):
        removeIfExists(able, "left")
        removeIfExists(able, "topleft")
        removeIfExists(able, "downleft")
    if(seat == len(data[row])-1):
        removeIfExists(able, "right")
        removeIfExists(able, "topright")
        removeIfExists(able, "downright")
    if(row == len(data)-1):
        removeIfExists(able, "down")
        removeIfExists(able, "downleft")
        removeIfExists(able, "downright")

    for dir in able:
        row_growth = 0
        seat_growth = 0
        if(dir == "top"):
            row_growth = -1
        elif(dir == "right"):
            seat_growth = 1
        elif(dir == "down"):
            row_growth = 1
        elif(dir == "left"):
            seat_growth = -1
        elif(dir == "topright"):
            row_growth = -1
            seat_growth = 1
        elif(dir == "downright"):
            row_growth = 1
            seat_growth = 1
        elif(dir == "downleft"):
            row_growth = 1
            seat_growth = -1
        elif(dir == "topleft"):
            row_growth = -1
            seat_growth = -1

        row_addition = row_growth
        seat_addition = seat_growth
        while True:
            if((seat+seat_addition < 0) or (row+row_addition < 0)):
                break
            try:
                if (data[row+row_addition][seat+seat_addition] == "L"):
                    break
                if (data[row+row_addition][seat+seat_addition] == "#"):
                    occupied += 1
                    break
            except:
                break
            row_addition += row_growth
            seat_addition += seat_growth
    return occupied



while True:
    new_data = data.copy()
    for index_row,row in enumerate(data):
        for index_seat,seat in enumerate(row):
            if(seat == "."):
                continue
            elif(seat == "L" and (checkForOccupied(data, index_row, index_seat) == 0)):
                old = new_data[index_row]
                old = [*old]
                old[index_seat] = "#"
                new_data[index_row] = "".join(old)
            elif(seat == "#" and (checkForOccupied(data, index_row, index_seat) >= 5)):
                old = new_data[index_row]
                old = [*old]
                old[index_seat] = "L"
                new_data[index_row] = "".join(old)
    if(data == new_data):
        total = 0
        for x in data:
            for y in x:
                if(y == "#"):
                    total +=1
        print(total)
        break
    data = new_data.copy()
