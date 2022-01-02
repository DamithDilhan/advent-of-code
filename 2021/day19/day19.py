
import re
from itertools import combinations
from collections import defaultdict, Counter
from typing import NamedTuple

class AxisInfo(NamedTuple):
    diff: int
    axis: int
    sign: int
    
class Scanner(NamedTuple):
    id: int
    points:list

    @classmethod
    def parse(cls,id, beacons: list):
        points = beacons
        return cls(id,points)


def find_x(sc_a, sc_dict):
    x_coords = {}
    y_coords = {}
    z_coords = {}
    for other in sc_dict.values():
        for axis in (0, 1, 2):
            for sign in (-1, 1):
                d_x: Counter[int] = Counter()
                

                for x, _, _ in sc_a.points:
                    for other_pt in other.points:
                        d_x[x - other_pt[axis] * sign] += 1
                        
                (x_diff, n), = d_x.most_common(1)
                if n >= 12:
                    x_coords[other.id] = AxisInfo(
                        axis=axis,
                        sign=sign,
                        diff=x_diff,
                    )
                

    for scanner in x_coords:
        other = sc_dict[scanner]
        for axis in (0, 1, 2):
            for sign in (-1, 1):
                d_y: Counter[int] = Counter()
                d_z: Counter[int] = Counter()
                for _, y, z in sc_a.points:
                    for other_pt in other.points:
                        d_y[y - other_pt[axis] * sign] += 1
                        d_z[z - other_pt[axis] * sign] += 1
                (y_diff, n), = d_y.most_common(1)
                if n >= 12:
                    y_coords[other.id] = AxisInfo(
                        axis=axis,
                        sign=sign,
                        diff=y_diff,
                    )
                (z_diff, n), = d_z.most_common(1)
                if n >= 12:
                    z_coords[other.id] = AxisInfo(
                        axis=axis,
                        sign=sign,
                        diff=z_diff,
                    )
                    

    return x_coords,y_coords,z_coords

        


if __name__=="__main__":
    with open("input.txt", "r") as fp:
        content = fp.read().splitlines()
    report = defaultdict(list)
    for line in content:
        if line.startswith("--"):
            number = int(re.findall(r' \d+ ',line)[0])
        elif line=="":
            continue
        else:
            report[number].append(tuple(map(int,line.split(",")))) 
    scanner_dict = {}
    for scanner in report.keys():
        scanner_dict[scanner] = Scanner.parse(scanner, report[scanner])

    scanner_pos = {0:(0,0,0)}
    beacons = set(scanner_dict[0].points)

    queue = [scanner_dict.pop(0)]
    while queue:
       
        scanner = queue.pop()
        x_plane,y_plane,z_plane = find_x(scanner,scanner_dict)
        
        for key in x_plane:
            origin_x = x_plane[key].diff
            origin_y = y_plane[key].diff
            origin_z = z_plane[key].diff

            scanner_pos[key] = (origin_x, origin_y, origin_z)

            next_scanner = scanner_dict.pop(key)
            next_scanner.points[:] =[
                (
                    origin_x + x_plane[key].sign * pt[x_plane[key].axis],
                    origin_y + y_plane[key].sign * pt[y_plane[key].axis],
                    origin_z + z_plane[key].sign * pt[z_plane[key].axis],
                )
                for pt in next_scanner.points
            ]

            
            beacons.update(next_scanner.points)

            queue.append(next_scanner)

    maximum_dist = 0
    pos = list(scanner_pos.values())
    for i,(x0,y0,z0) in enumerate(pos):
        for x1,y1,z1 in pos[i+1:]:
            maximum_dist = max(
                abs(x1-x0) + abs(y1-y0) + abs(z1 -z0),
            maximum_dist
            )
    
    print(f"number of scanners {len(beacons)} maximum distance {maximum_dist}")
