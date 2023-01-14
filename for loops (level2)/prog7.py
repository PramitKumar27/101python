n = int(input("Enter a number: "))
a = 65
for i in range(1, n+1):
    for j in range(0, i):
        str = chr(a)
        print(str, end=" ")
    a += 1
    print("")
