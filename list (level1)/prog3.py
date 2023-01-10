import math
lst = input("Enter a list: ").split()
a = None
b = None
for i in lst:
    if a is None:
        a = i
        continue
    if i > a:
        a = i

for i in lst:
    if b is None:
        b = i
        continue
    if i < b:
        b = i

print(a, b)
