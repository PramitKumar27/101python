n = input("Enter n: ")


def sumOfDigit(a):
    if len(a) <= 1:
        return int(a)
    else:
        return int(a[len(a)-1]) + sumOfDigit(a[:-1])


print(sumOfDigit(n))
