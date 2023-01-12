x = input("Enter number: ")
n = int(x)
fact = 1
for i in range(n, 0, -1):
    fact *= i

print(fact)
