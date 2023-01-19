lst = input("Enter list: ").split()
e = int(input("Enter element: "))


def bS(lst, e):
    if str(e) not in lst:
        print(-1)
    elif lst[len(lst)-1] == str(e):
        print(len(lst)-1)
    else:
        lst.remove(lst[len(lst)-1])
        bS(lst, e)


bS(lst, e)
