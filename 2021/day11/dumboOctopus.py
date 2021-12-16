def increase(i, j, h, w):
    if i < 0 or j < 0 or i >= w or j >= h:
        return 0

    # i-1 j-1
    if i-1 >= 0 and j-1 >= 0:
        content[j-1][i-1] += 1
        if content[j-1][i-1] == 10:
            increase(i-1, j-1, h, w)
    # i-1 j
    if i-1 >= 0 and j >= 0 and j < h:
        content[j][i-1] += 1
        if content[j][i-1] == 10:
            increase(i-1, j, h, w)
    # i-1 j+1
    if i-1 >= 0 and j+1 < h:
        content[j+1][i-1] += 1
        if content[j+1][i-1] == 10:
            increase(i-1, j+1, h, w)
    # i j-1
    if i >= 0 and i < w and j-1 >= 0:
        content[j-1][i] += 1
        if content[j-1][i] == 10:
            increase(i, j-1, h, w)
    # i j+1
    if i >= 0 and i < w and j+1 < h:
        content[j+1][i] += 1
        if content[j+1][i] == 10:
            increase(i, j+1, h, w)
    # i+1 j-1
    if i >= 0 and i+1 < w and j-1 >= 0:
        content[j-1][i+1] += 1
        if content[j-1][i+1] == 10:
            increase(i+1, j-1, h, w)
    # i+1 j
    if i >= 0 and i+1 < w and j >= 0 and j < h:
        content[j][i+1] += 1
        if content[j][i+1] == 10:
            increase(i+1, j, h, w)

    # i+1 j+1
    if i >= 0 and i+1 < w and j >= 0 and j+1 < h:
        content[j+1][i+1] += 1
        if content[j+1][i+1] == 10:
            increase(i+1, j+1, h, w)



with open("input.txt", "r") as fp:
    content = list(map(lambda x: [int(i) for i in x], fp.read().splitlines()))

h = len(content)
w = len(content[0])
total_steps = 500
steps = total_steps-1
flashes = 0

while steps >= 0:
    for j in range(h):
        for i in range(w):
            content[j][i] += 1
            if content[j][i] == 10:
                increase(i, j, h, w)

    for j in range(h):
        for i in range(w):
            if content[j][i] > 9:
                flashes += 1
                content[j][i] = 0
    total = 0
    for j in range(h):
        total += sum(content[j])
    if total == 0:
        break

    steps -= 1


for j in range(h):
    print(content[j])

print(flashes,total_steps -steps)

# each step increase by 1
# if value 10 flashes
# if increase adjacent by 1
# only flash 1 time for step
