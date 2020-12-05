import re

with open('input.txt') as file:
    data = file.read().split("\n\n")
    data = data[:-1] # remove last empty line

def formatHeight(item):
    for i, letter in enumerate(item, 0):
        if letter.isalpha():
            return [item[:i],item[i:]]

valid = 0
for x in data:
    current_passport = {}
    for y in x.split():
        y_list = y.split(":")
        current_passport[y_list[0]] = y_list[1]

    if(all(item in current_passport for item in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))):
        if ((len(current_passport["byr"]) == 4) & (1920 <= int(current_passport["byr"]) <= 2002)):
            if ((len(current_passport["iyr"]) == 4) & (2010 <= int(current_passport["iyr"]) <= 2020)):
                if ((len(current_passport["eyr"]) == 4) & (2020 <= int(current_passport["eyr"]) <= 2030)):
                    formatted_height = formatHeight(current_passport["hgt"])
                    if(formatted_height != None):
                        if ((formatted_height[0].isdigit())):
                            if (((formatted_height[1] == "cm") & (150 <= int(formatted_height[0]) <= 193)) | ((formatted_height[1] == "in") & (59 <= int(formatted_height[0]) <= 76))):
                                if(re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', current_passport["hcl"])):
                                    if(current_passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
                                        if((current_passport["pid"].isdigit()) & (len(current_passport["pid"]) == 9)):
                                            valid += 1


print(valid)
