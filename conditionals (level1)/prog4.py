a = input("Enter a: ")
b = input("Enter b: ")
c = input("Enter c: ")

d = int(a)
e = int(b)
f = int(c)

if d < e and d < f:
    print(d)
elif e < d and e < f:
    print(e)
else:
    print(f)
