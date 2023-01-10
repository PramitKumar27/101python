str = input("Enter your string: ")
str1 = ""

for i in range(len(str)):
    if str[i] == ",":
        str1 += "."
    else:
        str1 += str[i]
print(str1)
