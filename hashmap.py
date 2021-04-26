duplicate_list = [-1, 2, 3, 4, -1, 2]

hashmap = {}
for item in duplicate_list:
    if (item in hashmap):
        print(item)
        break
    else:
        hashmap[item] = 1
print(hashmap)