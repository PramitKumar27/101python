n = int(input("Enter n: "))


def decToBin(a):
    if a >= 1:
        decToBin(a//2)
        b = a % 2
        if b is not None:
            print(b, end="")


print(decToBin(n))
