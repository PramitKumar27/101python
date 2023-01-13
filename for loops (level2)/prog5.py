n = int(input("Enter integer: "))

for i in range(0, n):
    for j in range(0, n):
        for k in range(n-1, 0, -1):
            print("-", end="")
        print("*", end="")
    print("")
