a = input("Enter a: ")
b = input("Enter b: ")
x = int(a)
y = int(b)
c = input("Enter Operation from 1-6: ")
o = int(c)

if o == 1:
    print(x+y)
elif o == 2:
    print(x-y)
elif o == 3:
    print(x*y)
elif o == 4:
    print(x/y)
elif o == 5:
    print(x//y)
elif o == 6:
    print(x % y)
else:
    print("Invalid Operation")
