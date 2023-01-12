import math
a = input("Enter a: ")
b = input("Enter b: ")
c = input("Enter c: ")

d = float(a)
e = float(b)
f = float(c)

disc = (e**2 - 4*d*f)
if disc > 0:
    disc = math.sqrt(e**2 - 4*d*f)

if disc < 0:
    print("Complex Roots")
elif disc == 0:
    print(-e/(2*d))
elif disc > 0:
    print((-e-disc)/(2*d), (-e+disc)/(2*d))
