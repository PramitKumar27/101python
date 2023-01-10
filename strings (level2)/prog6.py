
str = input("Enter your string: ")
str1 = str.swapcase()
str1 += " "
str2 = ""
str3 = ""

for i in range(len(str1)):
    str2 += str1[i]
    if str1[i] == " ":
        str3 = str2.replace(" ", "")
        print(str3[::-1], end=" ")
        str2 = ""
