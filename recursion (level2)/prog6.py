lst = input("Enter list: ").split()
e = int(input("Enter element: "))


def bS(lst, e):
    if str(e) not in lst:
        return 0
    elif str(e) == lst[len(lst)-1]:
        return
