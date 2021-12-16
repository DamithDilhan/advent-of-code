from collections import defaultdict

content = []
temp = defaultdict(int)
counter = 0
with open("input.txt", "r") as fp:

    while True:
        line = fp.readline()
        if not line:
            break
        counter += 1
        for i in range(len(line)-1):
            temp[i] += int(line[i])

gamma = 0
epsilon = 0
for key in temp.keys():
    if temp[key] > counter - temp[key]:
        gamma += 2**(11-key) * 1
    else:
        epsilon += 2**(11-key) * 1

print(gamma, epsilon, gamma *epsilon)


    
    
        

