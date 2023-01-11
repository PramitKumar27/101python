lst = [["a", 1], ["b", 2], ["c", 3], ["d", 4]]
dict = {}
lst1 = []
for i in lst:
    for l in i:
        lst1.append(l)
p = 0
while p < len(lst1):
    if p % 2 != 0:
        a = lst1[p-1]
        b = lst1[p]
        dict[a] = b
    p += 1

print(dict)
