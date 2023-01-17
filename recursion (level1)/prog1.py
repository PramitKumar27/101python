# lst = input("Enter list: ").split()
lst = [1, 2, 3, 4]


def sum(s):
    if len(s) == 0:
        return 0
    else:
        return s[0] + sum(s[1:])


print(sum(lst))
