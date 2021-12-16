
import math 
translation_table = str.maketrans({k: format(i, "04b") for i, k in enumerate(
    ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"])})


def hex2bin(word):
    return word.translate(translation_table)


def str2bin(word):
    ans = 0
    for i, v in enumerate(word[::-1]):
        ans += int(v) * 2**i
    return ans
def get_version(word):
    return str2bin(word[:3])

def get_type(word):
    return str2bin(word[3:6])

def solve_literal(word):

    start = 0
    temp = []
    val = 0
    for i in range(start,len(word),5):
        if word[i] == "1":
            temp.append(word[i+1:i+5])
            val += 5
        else:
            temp.append(word[i+1:i+5])
            val += 5
           
            break
    return str2bin("".join(temp)), val


def solve3(start,content):
    
    if len(content) < 11:
        
        return 0, len(content),0
    versions = []
    version = get_version(content[start:])
    
    type_id = get_type(content[start:])

    if type_id == 4:
        start += 6
        value, mov = solve_literal(content[start:])
        
        start+=mov
        return version, start, value
    else:
        
        start += 6
        values = []
        if content[start] == "0":
            start += 1
            # 15 bit length 
            length = str2bin(content[start:start+15])
            start += 15
            
            while length >= 11 :
                
                version_,mov,value = solve3(start,content)
                versions.append(version_)
                values.append(value)
                
                length -= (mov - start)
                start = mov

            start += length

        else:
            # 11 bit 
            length = str2bin(content[start+1:start+12])
            start += 12
            
            for _ in range(length):
                version_,mov,value = solve3(start,content)
                versions.append(version_)
                values.append(value)
                start = mov

        if type_id == 0:
            # sum
            return version+sum(versions),start,sum(values)
        elif type_id == 1:
            # product
            return version+sum(versions),start,math.prod(values) 
        elif type_id == 2:
            # minimum value
            return version+sum(versions),start,min(values)
        elif type_id == 3:
            # maximum value
            return version+sum(versions),start,max(values)
        elif type_id == 5:
            # 1 > 2 ? 1 :0
            return version+sum(versions),start,1 if values[0]>values[1] else 0
        elif type_id == 6:
            # 1 < 2 ? 1 : 0
            return version+sum(versions),start,1 if values[0]<values[1] else 0

        elif type_id == 7:
            # 1 == 2 ? 1 : 0
            return version+sum(versions),start,1 if values[0]==values[1] else 0
            
        return version+sum(versions),start,values

if __name__=="__main__":
    with open("input.txt", "r") as fp:
        content = fp.read().splitlines()[0]

    content = hex2bin(content)
    sum_of_versions, _,final_value = solve3(0,content)
    print(f"sum of versions: {sum_of_versions} & final value : {final_value}")
