a = int(input("Enter a: "))
b = int(input("Enter b: "))


def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b-1)


print(power(a, b))
