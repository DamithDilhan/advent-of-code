

with open("input.txt", "r") as fp:
    content = fp.read().splitlines()

stack = []

OPEN = ["<","(","[","{",]
CLOSE = [">",")","]","}"]
mapper = {k:v for k,v in zip(OPEN, CLOSE)}
temp = {k:0 for k in CLOSE}

total_cost = []

incomplete_table = {
                    ")": 1 ,
                    "]": 2,
                    "}": 3 ,
                    ">": 4
}

for i in content:
    incomplete = True
    stack = []
    for j in i:
        if j in OPEN:
            stack.append(mapper[j])
        else:
            v = stack.pop()
            if j != v:
                temp[j] += 1
                incomplete =  False
                break
            
    if incomplete and len(stack)>0:
        total = 0
        for i in reversed(stack):
            total = total *5 +incomplete_table[i]
        total_cost.append(total)


point_table = {")":3,
                "]":57,
                "}":1197,
                ">":25137
                }
                
points = sum([ temp[i]*point_table[i] for i in temp.keys()])
print(points) # 358737
total_cost = sorted(total_cost)
print(total_cost[(len(total_cost))//2])

