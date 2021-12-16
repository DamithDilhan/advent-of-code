from collections import Counter

with open("input.txt", "r") as fp:
    content = map(lambda x: int(x), fp.readline().split(","))

temp = [0 for _ in range(9)]
temp2 = Counter(content)
for i in temp2.keys():
    temp[i] = temp2[i]

days = 256

for day in range(days):
    val = temp.pop(0)
    temp.append(val)
    temp[6] += val

print(sum(temp))