from collections import defaultdict

def display(content,x):
    for r in range(x+1):
        for c in range(x+1):
            print(f"{content[(c,r)]} ", end ="")
        print()

def solve1(start,end):        
    x = max(start + end)
    l = len(start) 

    temp = defaultdict()

    for i in range(x+1):
        for j in range(x+1):
            temp[(i,j)] = 0

    for i in range(0,l,2):

        if start[i] == end[i]:
            for k in range(min(start[i+1],end[i+1]), max(start[i+1],end[i+1])+1):
                temp[(start[i], k)] += 1 
        elif start[i+1] == end[i+1]:
            for k in range(min(start[i],end[i]), max(start[i],end[i])+1):
                temp[(k,start[i+1])] += 1 
        


    count = 0
    for element in temp.values():
        if element >= 2:
            count += 1
    print(f"solution 1 {count}")

def solve2(start,end):        
    x = max(start + end)
    l = len(start) 

    temp = defaultdict()

    for i in range(x+1):
        for j in range(x+1):
            temp[(i,j)] = 0

    for i in range(0,l,2):

        if start[i] == end[i]:
            for k in range(min(start[i+1],end[i+1]), max(start[i+1],end[i+1])+1):
                temp[(start[i], k)] += 1 
        elif start[i+1] == end[i+1]:
            for k in range(min(start[i],end[i]), max(start[i],end[i])+1):
                temp[(k,start[i+1])] += 1 
        else:
            x_change = start[i] - end[i]
            y_change = start[i+1] - end[i+1]

            x_dir = -1 if x_change >= 0 else 1
            y_dir = -1 if y_change >= 0 else 1
            # second part -----------------------------------
            for k in range(abs(x_change) +1):
                temp[(start[i]+(k*x_dir), start[i+1] + (k*y_dir)) ] += 1
            #------------------------------------------------


    count = 0
    for element in temp.values():
        if element >= 2:
            count += 1
    print(f"solution 2 {count}")

if __name__=="__main__":
    start = []
    end = []
    with open("input.txt", "r") as fp:

        while True:
            line = fp.readline()
            if not line: break
            line = line.split("->")
            start += list(map(lambda x :int(x), line[0].split(",")))
            end += list(map(lambda x :int(x), line[1].split(",")))
    
    solve1(start, end)
    solve2(start, end)