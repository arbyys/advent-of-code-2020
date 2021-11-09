with open('input.txt') as file:
    data = file.read().split(",")

    data = list(map(int, data)) # to int

last_time_spoken = {}
before_spoken = {}
last_spoken = 0
flag = False

for x in range(1, 2022):
    if(x == 2021):
        print(last_spoken)
    if(x <= len(data)):
        last_spoken = data[x-1]
        last_time_spoken[last_spoken] = x
        continue
    if(x == len(data)+1):
        last_spoken = 0
        if(last_spoken in last_time_spoken):
            before_spoken[last_spoken] = last_time_spoken[last_spoken]
            last_time_spoken[last_spoken] = x
        else:
            flag = True
            last_time_spoken[last_spoken] = x
        continue
    if(flag):
        last_spoken = 0
        before_spoken[last_spoken] = last_time_spoken[last_spoken]
        last_time_spoken[last_spoken] = x
        flag = False
        continue
    if(last_spoken in last_time_spoken):
        last_spoken = last_time_spoken[last_spoken] - before_spoken[last_spoken]
        if(last_spoken in last_time_spoken):
            before_spoken[last_spoken] = last_time_spoken[last_spoken]
            last_time_spoken[last_spoken] = x
        else:
            flag = True
            last_time_spoken[last_spoken] = x
        continue
    else:
        last_spoken = 0
        before_spoken[last_spoken] = last_time_spoken[last_spoken]
        last_time_spoken[last_spoken] = x
        continue
