import re

with open('input.txt') as file:
    data = file.read().split("\n\n")
    data = data[:-1] # remove last empty line

valid = 0
for x in data:
    current_passport = {}
    for y in x.split():
        y_list = y.split(":")
        current_passport[y_list[0]] = y_list[1]

    if(all(item in current_passport for item in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))):
        valid += 1

print(valid)
