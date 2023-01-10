lst = input("Enter your list: ").split()
n = input("Element to remove: ")

lst1 = []

for i in lst:
    if i == n:
        continue
    lst1.append(i)

print(lst1)
