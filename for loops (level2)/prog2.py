n = input("Enter number: ")
numb = int(n)

for i in range(1, numb+1):
    for j in range(0, i):
        print("* ", end="")
    print("\n")

# n = int(input("Enter the value of 'n': "))

# for i in range(1, n+1):
#     print("*" * i)
