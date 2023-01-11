lst = input("Enter first list: ").split()
lst1 = input("Enter second list: ").split()

lst2 = []

for i in lst:
    for j in lst1:
        if i == j:
            lst2.append(i)
        continue

print(lst2)
