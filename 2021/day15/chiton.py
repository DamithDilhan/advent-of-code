import sys
import heapq
sys.setrecursionlimit(1500)

with open("input.txt", "r") as fp:
    content = fp.read().splitlines()

l = len(content)
grid = {(0,0):0}

def part2_value(row, col):
    
    

    ans =  int(content[row%l][col%l]) + row//l + col//l
    return (ans % 9)  if ans > 9 else ans


# for i in range(1,l):
#         grid[(i,0)] = grid[(i-1,0)] + int(content[0][i])

# for j in range(1,l):
#     grid[(0,j)] = grid[(0,j-1)] + int(content[j][0])

# DP = {}
# def dp(r,c):
#     if (r,c) in DP:
#         return DP[(r,c)]
#     if r<0 or r>=l or c<0 or c>= l :
#         return 1e9
#     if r == l-1 and c == l-1:
#         return int(content[r][c])
#     ans = int(content[r][c]) + min(dp(r+1,c), dp(r,c+1))
#     DP[(r,c)] = ans

#     return ans
"""Part 2"""
for i in range(1,l*5):
        grid[(i,0)] = grid[(i-1,0)] + part2_value(i,0)

for j in range(1,l*5):
    grid[(0,j)] = grid[(0,j-1)] + part2_value(0,j)

DP = {}
def dp(r,c):
    if (r,c) in DP:
        return DP[(r,c)]
    if r<0 or r>=l*5 or c<0 or c>= l*5 :
        return 1e9
    if r == (5*l)-1 and c == (5*l)-1:
        return part2_value(r,c)
    ans = part2_value(r,c) + min(dp(r+1,c), dp(r,c+1),dp(r-1,c), dp(r,c-1))
    DP[(r,c)] = ans

    return ans  

def solve():
    DR = [-1,0,1,0]
    DC = [0,1,0,-1]

    Q = [ (0,0,0)]
    while Q:
        dist,r,c = heapq.heappop(Q)
        if r<0 or r>=l*5 or c< 0 or c>=l*5:
            continue

        rc_cost = dist + part2_value(r,c)
        if (r,c) not in DP or rc_cost < DP[(r,c)]:
            DP[(r,c)] = rc_cost
        else:
            continue
        if r==l*5 -1 and c==l*5 -1:
            break
        for d in range(4):
            rr = r + DR[d]
            cc = c + DC[d]
            heapq.heappush(Q, (DP[(r,c)],rr,cc))

    return DP[((l*5) -1,(l*5) -1)] - int(content[0][0])

# print(dp(0,0) - int(content[0][0])) #456

print(solve())

# for i in range(l*5):
#     for j in range(l*5):
#         print(part2_value(i,j),end="")

#     print()




