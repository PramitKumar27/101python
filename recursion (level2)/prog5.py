n = int(input("Enter n: "))


def decToBin(a):
    if a == 0:
        return 0
    else:
        return decToBin(a//2)
        print(a % 2)


print(decToBin(n))
