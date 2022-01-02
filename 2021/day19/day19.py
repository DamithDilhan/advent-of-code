
import re
from itertools import combinations
from collections import defaultdict, Counter

def get_difference(pair1, pair2):
    return ((pair1[0]-pair2[0])**2) +  ((pair1[1]-pair2[1])**2) + ((pair1[2]-pair2[2])**2)

def calculate_distance_matrix(scanner1):
    return {get_difference(pair1,pair2):(pair1,pair2) for pair1,pair2 in  combinations(scanner1,2)}

def find_common(scanner1,scanner2):
    distance_matrix1 = calculate_distance_matrix(scanner1)
    distance_matrix2 = calculate_distance_matrix(scanner2)
    common_keys = set(distance_matrix1.keys()).intersection(set(distance_matrix2))

    distance_map = {distance_matrix1[key]:distance_matrix2[key] for  key in common_keys}
    large_map = defaultdict(list)
    for key in distance_map.keys():
        point1, point2 = key
        pointA, pointB = distance_map[key]
        large_map[point1].append(pointA)
        large_map[point1].append(pointB)
        large_map[point2].append(pointA)
        large_map[point2].append(pointB)
    result = {}
    for key in large_map.keys():
        result[key] = Counter(large_map[key]).most_common()[0][0]

    return result


def find_absolute(mapped_content,place=0):
    differences = []
    for key in mapped_content:
        pointA_x = key[place]
        pointB = mapped_content[key]
        differences.append(pointA_x - pointB[0])
        differences.append(pointA_x - pointB[1])
        differences.append(pointA_x - pointB[2])
        differences.append(pointA_x + pointB[0])
        differences.append(pointA_x + pointB[1])
        differences.append(pointA_x + pointB[2])

    counter = Counter(differences).most_common()[0]
    return counter[0] if counter else 0
        


def find_relative_to_0(mapped_content):
    x = find_absolute(mapped_content,0)
    y = find_absolute(mapped_content,1)
    z = find_absolute(mapped_content, 2)

    return (x,y,z)

def travel(content):
    temp = defaultdict(list)
    
    for i in content:
        temp[i[0]].append(i[1])

    return temp
    

def main(content):
    relative_codes = {}
    relative_beacons = {}
    for key in content.keys():
        for key2 in content.keys():
            if key == key2 or (key2,key) in relative_codes: continue
            mapped_content = find_common(content[key],content[key2])
            if mapped_content == {}:
                continue
            x, y, z = find_relative_to_0(mapped_content)
            relative_codes[(key,key2)] = (x,y,z)
            relative_beacons[(key,key2)] = mapped_content

    # for key in relative_codes.keys():
    #     scanner1, scanner2 = key
    #     if scanner1==0:
    #         beacons += relative_codes[key][1]
    #     else:
    #         x,y,z = (0,0,0)

    max_value = max([ max(key) for key in relative_codes.keys()])
    nodes = travel(relative_codes.keys())
    for point in nodes:
        for end_p in nodes[point]:
            if (0,end_p) in relative_codes:
                continue
            x = relative_codes[(0 ,point)][0] + relative_codes[(point,end_p)][0]
            y = relative_codes[(0 ,point)][1] + relative_codes[(point,end_p)][1]
            z = relative_codes[(0 ,point)][2] + relative_codes[(point,end_p)][2]

            relative_codes[(0,end_p)] = (x,y,z)
    beacons = []
    for key in relative_beacons.keys():
        if key[0] == 0:
            beacons += relative_beacons[key]
        else:
            x,y,z = relative_codes[(0,key[0])]
            for beacon in relative_beacons[key]:
                beacons.append((beacon[0]+x , beacon[1]+y, beacon[2]+z))

    # beacons = set(beacons)
    print(beacons)
    return len(beacons)

    



            



        


if __name__=="__main__":
    with open("input.txt", "r") as fp:
        content = fp.read().splitlines()
report = defaultdict(list)
number = 0
for line in content:
    if line.startswith("--"):
        number = int(re.findall(r' \d+ ',line)[0])
    elif line=="":
        continue
    else:
        report[number].append(tuple(map(int,line.split(",")))) 

print(main(report))