import os

input_file = "input.txt"

with open(input_file, "r") as fp:
    content = fp.readlines()
horizontal = 0
depth = 0

for line in content:
    word = line.split()
    key = word[0]
    value = word[1]
    if key=="forward":
        horizontal += int(value)
    if key=="down":
        depth += int(value)
    if key=="up":
        depth -= int(value)


print(f"horizontal = {horizontal} , depth = {depth} , multi = {horizontal * depth}")


