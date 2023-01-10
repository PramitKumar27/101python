str = input("Enter a string: ")
str1 = str.lower()
str1 += " "
str2 = ""
str3 = ""
for i in range(len(str1)):
    str2 += str1[i]
    if str1[i] == " ":
        str3 = "".join(sorted(str2))
        str4 = str3.strip()
        print(str4, end=" ")
        str2 = ""
