with open('input.txt') as file:
    data = file.read().split("\n")
    data = data[:-1] # remove last empty line

    data = list(map(int, data)) # to int

invalid = 104054607
used_numbers = []
current_index = 0
backup_index = current_index

while True:
    if(len(used_numbers) == 0):
        backup_index = current_index
    used_numbers.append(data[current_index])
    if(sum(used_numbers) == invalid):
        break
    elif(sum(used_numbers) > invalid):
        used_numbers = []
        current_index = backup_index
    current_index+= 1

smallest = min(used_numbers)
largest = max(used_numbers)
print(smallest + largest)
