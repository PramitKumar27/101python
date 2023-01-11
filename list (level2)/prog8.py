lst = input("Enter a list: ").split()
i = 0
n = len(lst)
lst1 = []
for l in lst:
    if i == n-1:
        print(lst1)
    else:
        print(lst1)
        lst[i], lst[i+1] = lst[i+1], lst[i]
        lst1.append(lst)
        i += 1
