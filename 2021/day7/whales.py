from collections import Counter
with open("input.txt", "r") as fp:
    content = list(map(lambda x: int(x), fp.readline().split(",") ))


temp = Counter(content)

cost = None

# for i in temp.keys():
#     new_cost = sum([ abs(k-i)*temp[k] for k in temp.keys() if k != i])
#     if cost==None :
#         cost = new_cost
#     elif new_cost < cost:
#         cost = new_cost

# print(cost)

def cumm_sum(a):

    return int(a*(a+1)//2)

min_val = min(content)
max_val = max(content)

mid_val = (min_val + max_val)//2

most_common, _ = temp.most_common(1)[0]


for i in range(min([most_common, mid_val]),max([most_common, mid_val])):
    
    
    new_cost = sum([ cumm_sum(abs(k-i)) * temp[k] for k in temp.keys()])
    if cost == None:
        cost= new_cost
    elif new_cost< cost:
        cost = new_cost

    

print(cost)
