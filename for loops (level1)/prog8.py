# prog 7 as while loop

x = input("Enter number: ")
n = int(x)
fact = 1

while n > 0:
    fact *= n
    n -= 1


print(fact)
