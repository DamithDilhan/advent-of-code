from __future__ import annotations
import re
from collections import defaultdict


pattern = r"([-]?\d+)..([-]?\d+)"

def set_bound(coord:tuple):

    x0 = -50
    x1 = 50
    if coord[0] > 50 or coord[1] < -50:
        return None
    if -50 <= coord[0] <= 50  :
        x0 = coord[0]
    if -50 <= coord[1] <= 50 :
        x1 = coord[1]

    return(x0, x1)


class Cube():
    def __init__(self,coord:tuple):
        

        self.x = coord[0][0]
        self.y = coord[1][0]
        self.z = coord[2][0]
        self.lx = coord[0][1] - self.x +1
        self.ly = coord[1][1] - self.y +1
        self.lz = coord[2][1] - self.z +1

    def num_of_switches(self):
        return (self.lx)*(self.ly )*(self.lz)

    def intersect_x(self,cube:Cube):
        x = cube.x
        end_x = cube.lx + x - 1
        if end_x < self.x or x > self.x + self.lx:
            return False
        
        return True
        
        

    def intersect_y(self,cube:Cube):
        y = cube.y
        end_y = cube.ly + y - 1
        if end_y < self.y:
            return False
        if y > self.y + self.ly:
            return False
        return True

    def intersect_z(self,cube:Cube):
        z = cube.z
        end_z = cube.lz + z - 1
        if end_z < self.z:
            return False
        if z > self.z + self.lz:
            return False
        return True

    def intersect(self,cube:Cube):
        if self.intersect_x(cube) and self.intersect_y(cube) and self.intersect_z(cube):
            return (
                (max(self.x, cube.x), min(self.x+self.lx-1, cube.x + cube.lx -1)),
                (max(self.y, cube.y), min(self.y+self.ly-1, cube.y + cube.ly -1)),
                (max(self.z, cube.z), min(self.z+self.lz-1, cube.z + cube.lz -1))
            )
        else:
            return None

def solve(instructions:list, bounded:bool = False):

    cubes = []
    
    for line in instructions:
        match = re.findall(pattern, line)
        cube = list(map(lambda x: (int(x[0]),int(x[1])) ,match))

        if bounded:
            x_coord, y_coord, z_coord = (set_bound(cube[0]), set_bound(cube[1]), set_bound(cube[2]))
            if x_coord == None or y_coord== None or z_coord == None:
                continue
            cube = (x_coord, y_coord, z_coord)

        if line.startswith("on"):
            cubes.append((1,Cube(cube)))
           
            
        else:
            cubes.append((0,Cube(cube)))

    count = defaultdict(int)
    for item in range(len(cubes)):
        state, cube = cubes[item]
        
        new_count = defaultdict(int)
        keys = set(count.keys())


        for other_cube in keys:
            
            overlap = cube.intersect(other_cube)
            if overlap == None:
                continue

            new_count[Cube(overlap)] -= count[other_cube]
        if state:
            new_count[cube] += 1
        
        for c in new_count:
            count[c] += new_count[c]

    on_switches = 0
    for cube in count:
        on_switches += cube.num_of_switches() * count[cube]
    
    return on_switches

def solve1(instructions:list):
    result = solve(instructions, True)
    print(f"solution 1 {result}")

def solve2(instructions:list):
    result = solve(instructions)
    print(f"solution 2 {result}")

if __name__ == "__main__":
    with open("input.txt", "r") as fp:
        content = fp.read().splitlines()
    
    solve1(content)
    solve2(content)

       


