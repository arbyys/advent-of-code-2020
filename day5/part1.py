with open('input.txt') as file:
    data = file.read().split("\n")
    data = data[:-1] # remove last empty line

def getPassID(row, column):
    return row * 8 + column

highest_id = 0
for x in data:
    rows = x[:7]
    columns = x[7:]

    row = 0
    column = 0

    rows_range = range(0, 129)
    for r in rows:
        row_min = min(rows_range)
        row_max = max(rows_range)
        if(r == "F"): # front
            rows_range = range(row_min, int(row_max - (row_max - row_min) / 2)+1)
        else:         # back
            rows_range = range(int(row_min + (row_max - row_min) / 2), row_max+1)

    row = rows_range[0]

    columns_range = range(0, 9)
    for c in columns:
        column_min = min(columns_range)
        column_max = max(columns_range)
        if(c == "L"): # right
            columns_range = range(column_min, int(column_max - (column_max - column_min) / 2)+1)
        else:         # left
            columns_range = range(int(column_min + (column_max - column_min) / 2), column_max+1)

    column = columns_range[0]
    passID = getPassID(row, column)
    if(passID > highest_id):
        highest_id = passID
print(highest_id)
