str = input("Enter your string: ")
curr = input("Enter your curr char: ")
new = input("Enter your new char: ")
str1 = ""
for i in range(len(str)):
    if str[i] == curr:
        str1 += new
    else:
        str1 += str[i]

print(str1)
