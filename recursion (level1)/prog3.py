n = int(input("Enter value of n: "))


def fact(a):
    if a == 0 or a == 1:
        return a
    else:
        return a * fact(a-1)


print(fact(n))
