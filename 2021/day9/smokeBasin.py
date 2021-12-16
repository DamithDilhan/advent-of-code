

with open("input.txt", "r") as fp:
    content = fp.readlines()

h = len(content)
w = len(content[0]) -1

marked = {}

def checkBorder(i,j):
    if i == len(content[0]) - 1  or j == len(content)  or i == -1 or j == -1 or int(content[j][i]) == 9 :
        return 0
    if marked.get((i,j)):
        return 0
    else:
        
        marked[(i,j)] = 1
        checkBorder(i, j-1)
        checkBorder(i-1, j)
        checkBorder(i, j+1)
        checkBorder(i+1,j)
        


minimum = []
sizes = []
for j in range(h):
    for i in range(w):
        
        u = int(content[j-1][i]) if j > 0 else float("inf")
        d = int(content[j+1][i]) if j < h-1 else float("inf")
        l = int(content[j][i-1]) if i > 0 else float("inf")
        r = int(content[j][i+1]) if i < w -1 else float("inf")

        if int(content[j][i]) < min(u,d,l,r):
            minimum.append(int(content[j][i]))
            checkBorder(i,j)
            sizes.append(len(marked.keys()))
            marked = {}
            


print(sum(minimum) + len(minimum))

if len(sizes) > 3:
    sizes = sorted(sizes,reverse=True)
    print(sizes[0]*sizes[1]*sizes[2])
            
