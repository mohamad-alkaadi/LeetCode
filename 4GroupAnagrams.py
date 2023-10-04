strs = ["eat","tea","tan","ate","nat","bat"]
new_strs = []
b = []
used_strs = []


for i in strs:
    z = len(i)
    x = ""
    for j in i:
        x = j + x
    if x in used_strs:
        continue
    if x in strs:
        new_strs.append([i,x])
    if x not in strs:
        new_strs.append(i)
    new_strs.append(b)

    print("---------")

# print(reversed_strs)
print(new_strs)
