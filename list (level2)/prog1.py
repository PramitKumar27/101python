
lst = input("Enter 1st list: ").split()
lst1 = input("Enter 2nd list: ").split()
lst2 = []

for i in lst:
    if i not in lst1:
        lst2.append(i)

print(lst2)
