import math
lst0 = input("Enter the A co-ordinates: ").split()
lst1 = input("Enter the B co-ordinates: ").split()

x1 = float(lst0[0])
y1 = float(lst0[1])
z1 = float(lst0[2])
x2 = float(lst1[0])
y2 = float(lst1[1])
z2 = float(lst1[2])

ab = (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2

print(math.sqrt(ab))
