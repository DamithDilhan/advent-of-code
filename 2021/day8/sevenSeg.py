from collections import Counter


def map_seq(pattern):
    temp = {i: "" for i in range(9)}
    count = Counter("".join(pattern))
    temp_map = {}
    for i in pattern:
        if len(i) == 2:
            temp[1] = i
        elif len(i) == 3:
            temp[7] = i
        elif len(i) == 4:
            temp[4] = i
        elif len(i) == 7:
            temp[8] = i

    for i in count.most_common():
        l, k = i
        if k == 9:
            temp_map[2] = l
        elif k == 6:
            temp_map[5] = l
        elif k == 4:
            temp_map[4] = l
        elif k == 8:
            if l not in temp[1]:
                temp_map[0] = l
            else:
                temp_map[1] = l
        elif k == 7:
            if l not in temp[4]:
                temp_map[3] = l
            else:
                temp_map[6] = l

    for i in pattern:
        if i in temp.values():
            continue
        else:
            val = set(i)
            if val == set([temp_map[k] for k in [0, 1, 2, 3, 4, 5]]):
                temp[0] = i
            elif val == set([temp_map[k] for k in [0, 1, 3, 4, 6]]):
                temp[2] = i
            elif val == set([temp_map[k] for k in [0, 1, 2, 3, 6]]):
                temp[3] = i
            elif val == set([temp_map[k] for k in [0, 5, 6, 2, 3]]):
                temp[5] = i
            elif val == set([temp_map[k] for k in [0, 5, 6, 2, 3, 4]]):
                temp[6] = i
            else:
                temp[9] = i
    return temp_map


def translate(word, temp_map):

    val = set(word)
    l = len(word)
    if l == 2:
        return 1
    elif l == 3:
        return 7
    elif l == 4:
        return 4
    elif l == 7:
        return 8
    if val == set([temp_map[k] for k in [0, 1, 2, 3, 4, 5]]):
        return 0
    elif val == set([temp_map[k] for k in [0, 1, 3, 4, 6]]):
        return 2
    elif val == set([temp_map[k] for k in [0, 1, 2, 3, 6]]):
        return 3
    elif val == set([temp_map[k] for k in [0, 5, 6, 2, 3]]):
        return 5
    elif val == set([temp_map[k] for k in [0, 5, 6, 2, 3, 4]]):
        return 6
    else:
        return 9


content_right = []
content_left = []

# with open("input.txt", "r") as fp:
#     while True:
#         line = fp.readline()
#         if not line:
#             break
#         content_right += line.split("|")[1].split()
#         content_left += line.split("|")[0].split()


# count = 0

# for i in content:
#     if len(i) in [2,3,4,7]:
#         count += 1

# print(count)


with open("input.txt", "r") as fp:
    while True:
        line = fp.readline()
        if not line:
            break
        content_right.append(line.split("|")[1].split())
        content_left.append(line.split("|")[0].split())

count = 0
for i in range(len(content_left)):
    mapper = map_seq(content_left[i])
    

    count += translate(content_right[i][0], mapper)*1000 + translate(content_right[i][1], mapper)*100 + translate(content_right[i][2], mapper)*10 + translate(content_right[i][3], mapper)

print(count)
