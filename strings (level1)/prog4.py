str = input("Enter your string: ")
n = len(str)

if n < 6:
    print("")
else:
    print(str[:3]+str[-3:-1]+str[-1])
