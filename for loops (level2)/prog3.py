nn = input("Enter a number: ")
lst = []
n = int(nn)
i = len(nn)
while i > 0:
    a = int(n % 10)
    lst.append(a)
    n = n/10
    i -= 1

for i in lst:
    print(i, end="")
