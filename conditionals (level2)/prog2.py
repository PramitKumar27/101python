a = input("Enter a: ")
b = input("Enter b: ")
c = input("Enter c: ")

d = int(a)
e = int(b)
f = int(c)

if d > e and e > f:
    print("Decreasing Order")
elif d < e and e < f:
    print("Increasing Order")
else:
    print("None")
