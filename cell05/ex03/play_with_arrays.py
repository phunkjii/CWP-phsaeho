old_arr = [2, 8, 9, 48, 8, 22, -12, 2]
new_arr = []

for i in old_arr:
    if i > 5:
        new_arr.append(i+2)

thisset = set(new_arr)
print(thisset)