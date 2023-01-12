n = input("Enter a number: ")
x = int(n)

print("=== Multiplication table of %d ===" % x)

for i in range(1, 11):
    print("%d X %d = %d " % (x, i, x*i))
