n = input("Enter year: ")
y = int(n)

if y % 4 != 0:
    print(False)
elif y % 100 != 0:
    print(True)
elif y % 400 == 0:
    print(True)
