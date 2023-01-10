lst = input("Enter the list: ").split()
fact = int(input("Enter factor: "))
lst1 = []
for n in lst:
    try:
        a = int(n)
        b = a*fact
        lst1.append(b)
    except:
        lst1.append(fact*n)

print(lst1)
