strs = ["eat","tea","tan","ate","nat","bat"]

new_stars = []

for i in strs:
    reversed_str = i[::-1]
    if reversed_str in strs:
        new_stars.append([i,reversed_str])

print(new_stars)