list = [1, 1, 1, 4, 5, 6, 7, 2, 3, 9, 3, 9, 4, 5, 6, 7, 8, 4]
unique = []
for item in list:
    if item not in unique:
        unique.append(item)
unique.sort()
list = unique
print(list)
