from collections import Counter

sample = None
with open("input.txt", "r") as fp:
    content = fp.read().splitlines()

temp = {}

for i in content:
    if not sample:
        sample = i
    elif i=="":
        continue
    else:
        k,v = i.split(" -> ")
        temp[k] = v

record = {k:0 for k in temp.keys()}
count = Counter(sample)

for i in range(1,len(sample)):
    record[sample[i-1:i+1]] += 1

def combine2(record,count):
    new_record = {k:0 for k in record.keys()}
    for key in record:
        if record[key]>0:
            v = temp[key]
            count[v] += record[key]
            new_record[key[0]+v] += record[key]
            new_record[v+key[1]] += record[key]

    return new_record

def combine(word):
    new_word = ""
    for l in range(1,len(word)):
        new_word += word[l-1]+temp[word[l-1:l+1]]
    return  new_word + word[-1]

for i in range(40):
    
    # sample = combine(sample)
    record = combine2(record,count)


count = count.most_common()
print(count[0][1] - count[-1][1])