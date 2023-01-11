lst = [1, 2, 3, 4, 5, 6, [7, 8, 9]]
lst1 = []

for i in lst:
    if isinstance(i, list):
        for nest in i:
            lst1.append(nest)
    else:
        lst1.append(i)

print(lst1)
