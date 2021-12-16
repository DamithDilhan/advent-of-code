from collections import Counter
from copy import copy

def get_max(str_list,pos):
    str_val = ""
    for i in str_list:
        str_val += i[pos]
    c = Counter(str_val)
    return "1" if c["1"] >= c["0"] else "0"

def filter_list(nums, _max = True):
    temp = copy(nums)
    
    for pos in range(12):
        k = get_max(temp,pos)
        print(f"pos {pos} max {k}")
        ans = []
        for i in temp:
            #consider max
            if _max and k == "1" and i[pos] == "1":
                ans.append(i)
            elif _max and k == "0" and i[pos] == "0":
                ans.append(i)
            #consider min
            if not _max and i[pos] != k:
                ans.append(i)
            
        if len(ans) == 1:
            return ans[0]
        temp = copy(ans)
    return temp[0]

def str2bin(number):
    val =0
    for i in range(12):
        
        val += 2 ** (12 - 1 - i) * int(number[i]) 

    return val

            
        


with open("input.txt","r") as fp:
    content = fp.readlines()


o2 = str2bin(filter_list(content))
co2 = str2bin(filter_list(content,_max= False))
print(o2, co2, o2 * co2)