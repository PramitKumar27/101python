lst = input("Enter your list: ").split()
lst1 = []
for i in lst:
    a = int(i)
    lst1.append(a)


lst1.sort()

print(lst1[-2])
