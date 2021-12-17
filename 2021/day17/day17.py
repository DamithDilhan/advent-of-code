
def run_loop(uy, ux):
    sx =0
    sy = 0
    while True:
        sx += ux
        sy += uy
        if uy == 0:
            return sy
        ux -=1 if ux != 0 else 0
        uy -= 1

def run_loop2(uy, ux,min_x,max_x, min_y, max_y):
    sx =0
    sy = 0
    while True:

        if (min_x <= sx <= max_x) and ( max_y <=sy <= min_y):
            return True
        if sy < max_y or sx > max_x:
            return False
        sx += ux
        sy += uy
        if ux < 0:
            ux += 1
        if ux > 0:
            ux -= 1
        
        uy -= 1

def solve1():
    temp = []
    for i in range(0,max_target_x+1):
        for j in range(-1*max_target_y):
            temp.append(run_loop(j,i))

    print(f"solution 1 : {max(temp)}")

def solve2():
    count = 0

    for i in range(0,max_target_x+1):
        for j in range(max_target_y,-1* max_target_y):
            if run_loop2(j,i,min_target_x, max_target_x,min_target_y, max_target_y):
                count+=1
    print(f"solution 2 : {count}")



if __name__=="__main__":
    
    with open("input.txt", "r") as fp:
        content = fp.read().replace(",","").split()

target_x_coordinates = list(map(int,content[2].split("=")[1].split("..")))
target_y_coordinates = list(map(int,content[3].split("=")[1].split("..")))

min_target_x, max_target_x = target_x_coordinates
max_target_y, min_target_y = target_y_coordinates


solve1()
solve2()
