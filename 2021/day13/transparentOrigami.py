from collections import defaultdict

def y_fold(y,coord,max_y):
    count = 0
    if True:
        for i in range(1,y+1):
            if y-i >=0:
                row = list(set(coord.get(y+i,[]) + coord.get(y-i,[])))
                coord[y-i] = row
                if coord.get(y+i, None):
                    del coord[y+i]
                count += len(row)
                

    return count,coord,y -1

def transpose(coord):
    new_coord = defaultdict(list)
    for key in coord.keys():
        for i in coord[key]:
            new_coord[i].append(key)

    return new_coord

def print_coord(coord, max_x, max_y):
    
    for j in range(max_y+1):
        for i in range(max_x+1):
            if i in coord.get(j,[]):
                print("# ",end="")
            else:
                print("  ",end="")
        print()


with open("input.txt", "r") as fp:

    content = fp.read().splitlines()

folds = []
x_coord = defaultdict(list)

max_x = 0
max_y = 0

for line in content:
    if line == "":
        continue
    elif line.startswith("fold"):
        k,v = line.split()[2].split("=")
        folds.append((k,int(v)))
    else:
        k,v = line.split(",")
        k = int(k)
        v = int(v)
        max_x = k if k > max_x else max_x
        max_y = v if v > max_y else max_y
        x_coord[k].append(v)



x_coord_sys = True
count = 0
for item in folds:
    if item[0]=="x":
        if x_coord_sys:
            count, x_coord, max_x = y_fold(item[1],x_coord, max_x)
        else:
            count, x_coord, max_x = y_fold(item[1],transpose(x_coord), max_x)
            x_coord_sys = True
    elif item[0]=="y":
        if x_coord_sys:
            count, x_coord, max_y = y_fold(item[1],transpose(x_coord), max_y)
            x_coord_sys = False
        else:
            count, x_coord, max_y = y_fold(item[1],x_coord, max_y)
            
if x_coord_sys:
    print_coord(transpose(x_coord),max_x, max_y,)
else:
    print_coord(x_coord,max_x, max_y,)
