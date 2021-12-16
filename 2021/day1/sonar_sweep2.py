import os

input_file = "input.txt"
temp = []
with open("input.txt", "r") as fp:
    content = fp.readlines()
#1608
increased = 0
for i in range(len(content) - 2):
    temp.append(int(content[i+2]) + int(content[i+1]) + int(content[i]))
'''
for j in range(len(temp) - 1):
    if (int(temp[j+1])-int(temp[j]) > 0 ):
        increased += 1
'''
for j in range(len(content)-3):
    if (int(content[j+3])-int(content[j]) > 0 ):
        increased += 1

print(increased)