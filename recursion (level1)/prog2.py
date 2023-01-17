n = int(input("Enter value of n: "))


def rec(a):
    if a == 0:
        return 0
    else:
        return a + rec(a-1)


print(rec(n))
