import os

input_file = "input.txt"

with open("input.txt", "r") as fp:
    content = fp.readlines()

increased = 0
for i in range(len(content) - 1):
    if (int(content[i+1])-int(content[i]) > 0 ):
        increased += 1

print(increased)