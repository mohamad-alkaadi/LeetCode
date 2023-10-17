counter = {}
nums = [-1,-1]
k = 2
for i in nums:
    if i in counter:
        counter[i] += 1
    elif i not in counter:
        counter[i] = 1

print(counter)

largest_keys = []

count = set(counter.values())
count.sorted(count, reverse=True)

for i in count[:k]:
    if i in counter.values():
        largest_keys.append(counter[i])

print(largest_keys)
